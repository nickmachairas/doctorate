import re
from app import db
from .aux import data_owner
from app.models import Locations, Projects, Misc, Borings, Layers, \
    Piles, LoadTests, StaticTests, InterpCapacities


def extract_olson_records(fname):
    """ Extracts all records from the Olson Raw file as a list of strings
    """
    records = []
    with open(fname, 'r') as f:
        for record in re.findall(r'LTN Blank(.*?)\n\s+\n', f.read(), re.S):
            # the split removes the first line
            records.append(record.split('\n', 1)[1])

    return records


def extract_olson_values(record):
    """ Given a raw record, this function will extract all record values.
    Returns a dictionary.
    """
    val_dict = {}
    description = ''
    warning = ''
    line_count = 0

    # Extract description and warning, if any
    for line in record.splitlines():
        if line[0] == '!':
            description += line[2:]
            description = re.sub(' +', ' ', description)
            line_count += 1
        elif line[0] == '*':
            warning += line[2:]
            warning = re.sub(' +', ' ', warning)
            line_count += 1
    val_dict['description'] = description if description else None
    val_dict['warning'] = warning if warning else None

    # Extract first line of LTN data
    ltn_line = record.splitlines()[:][line_count].split()
    if len(ltn_line) > 12:
        loc = []
        while len(ltn_line) > 11:
            loc.append(ltn_line.pop(-1))
        ltn_line += [' '.join(loc[::-1])]
    val_dict['source_id'] = int(ltn_line[0])
    val_dict['type'] = ltn_line[1]
    val_dict['shape'] = ltn_line[2]
    val_dict['direction'] = ltn_line[3]
    val_dict['length'] = float(ltn_line[4])
    val_dict['emb_length'] = float(ltn_line[4]) - float(ltn_line[5])
    val_dict['dratio'] = float(ltn_line[6])
    val_dict['tapered'] = True if ltn_line[7] == 'T' else False
    val_dict['aeol'] = int(ltn_line[8])
    val_dict['weight'] = float(ltn_line[9])
    val_dict['site_name'] = eval(ltn_line[10])
    val_dict['location'] = ltn_line[11]
    line_count += 1

    # Extract (tapered) dimensions
    first_dim_line = record.splitlines()[:][line_count].split()
    # if len(first_dim_line) == 2:
    if not val_dict['tapered']:
        val_dict['diameter'] = float(first_dim_line[0])
        val_dict['circumference'] = float(first_dim_line[1])
        if len(first_dim_line) == 3:
            val_dict['square_circ'] = float(first_dim_line[2])
        else:
            val_dict['square_circ'] = None
        val_dict['taper_dims'] = None
        line_count += 1
    else:
        val_dict['square_circ'] = None
        taper_dict = {'diameter': [], 'length': [], 'circumference': []}
        val_dict['diameter'] = float(first_dim_line[0])
        val_dict['circumference'] = float(first_dim_line[2])
        for line in record.splitlines()[:][line_count:]:
            if line.split()[0] != '-1.00':
                taper_dict['diameter'].append(float(line.split()[0]))
                taper_dict['length'].append(float(line.split()[1]))
                taper_dict['circumference'].append(float(line.split()[2]))
                line_count += 1
            else:
                line_count += 1
                break
        val_dict['taper_dims'] = taper_dict

    # Extract mid line data
    mid_line = record.splitlines()[:][line_count].split()
    val_dict['predom_soil'] = mid_line[0]
    val_dict['layer_count'] = int(mid_line[1])
    val_dict['ewt'] = float(mid_line[2])
    val_dict['sqf'] = int(mid_line[3])
    val_dict['i_code'] = float(mid_line[4])
    val_dict['vibro'] = True if mid_line[5] == 'T' else False
    val_dict['reo_check'] = True if mid_line[6] == 'T' else False
    val_dict['ts_check'] = True if mid_line[7] == 'T' else False
    val_dict['ut_boring'] = True if mid_line[8] == 'T' else False
    val_dict['ut_sounding'] = True if mid_line[9] == 'T' else False
    val_dict['cased'] = True if mid_line[10] == 'T' else False
    val_dict['predrilled'] = True if mid_line[11] == 'T' else False
    val_dict['relief_drilled'] = True if mid_line[12] == 'T' else False
    val_dict['jetted'] = True if mid_line[13] == 'T' else False
    line_count += 1

    # Extract layer data
    layer_dict = {
        'index': [], 'soil_type': [], 'height': [], 'evso': [], 'tuw': [],
        'water_content': [], 'liquid_limit': [], 'plasticity': [], 'ssuu': [],
        'ssfv': [], 'ssms': [], 'ssqt': [], 'nval': [], 'cnval': [], 'qc': [],
        'fsl': []}
    li = 0
    for line in record.splitlines()[:][line_count:-1]:
        li += 1
        ll = [i if i not in ['0', '0.00', '0.000']
              else None for i in line.split()]
        layer_dict['index'].append(li)
        layer_dict['soil_type'].append(ll[0])
        layer_dict['height'].append(float(ll[1]))
        layer_dict['evso'].append(float(ll[2]) if ll[2] else None)
        layer_dict['tuw'].append(float(ll[3]) * 1000 if ll[3] else None)
        layer_dict['water_content'].append(int(ll[4]) if ll[4] else None)
        layer_dict['liquid_limit'].append(int(ll[5]) if ll[5] else None)
        layer_dict['plasticity'].append(int(ll[6]) if ll[6] else None)
        layer_dict['ssuu'].append(float(ll[7]) if ll[7] else None)
        layer_dict['ssfv'].append(float(ll[8]) if ll[8] else None)
        layer_dict['ssms'].append(float(ll[9]) if ll[9] else None)
        layer_dict['ssqt'].append(float(ll[10]) if ll[10] else None)
        layer_dict['nval'].append(int(ll[11]) if ll[11] else None)
        layer_dict['cnval'].append(int(ll[12]) if ll[12] else None)
        layer_dict['qc'].append(int(ll[13]) if ll[13] else None)
        layer_dict['fsl'].append(float(ll[14]) if ll[14] else None)
        line_count += 1
    val_dict['layers'] = layer_dict

    # Extract final line od data
    end_line = record.splitlines()[:][line_count].split()
    val_dict['half_inch_capacity'] = int(end_line[0]) \
        if end_line[0] != '0' else None
    val_dict['davisson_capacity'] = int(end_line[1]) \
        if end_line[1] != '0' else None
    val_dict['max_load'] = int(end_line[2]) \
        if end_line[2] != '0' else None
    val_dict['brown_capacity'] = int(end_line[3]) \
        if end_line[3] != '0' else None
    val_dict['davisson_displacement'] = float(end_line[4]) \
        if end_line[4] != '0.00' else None
    val_dict['max_displacement'] = float(end_line[5]) \
        if end_line[5] != '0.00' else None
    val_dict['dqf'] = int(end_line[6])
    val_dict['setup_time'] = int(end_line[7])
    val_dict['source_ref'] = int(end_line[8])

    return val_dict


def add_olson_data(record, qs=None):
    """ Accepts an Olson record as extracted from ``extract_olson_values()``
    and commits this record to the database.
    """
    loc = Locations(
        description=record['location'])
    db.session.add(loc)

    prj = Projects(
        user_id=data_owner().id,
        source_db='Olson APC',
        source_id=record['source_id'],
        description=record['description'],
        warning=record['warning'],
        source_ref=record['source_ref'],
        dqf=record['dqf'],
        location=loc)
    db.session.add(prj)

    misc = Misc(
        reo_check=record['reo_check'],
        ts_check=record['ts_check'],
        ut_boring=record['ut_boring'],
        ut_sounding=record['ut_sounding'],
        i_code=record['i_code'],
        project=prj)
    db.session.add(misc)

    boring = Borings(
        predom_soil=record['predom_soil'],
        layer_count=record['layer_count'],
        ewt=record['ewt'],
        sqf=record['sqf'],
        project=prj
    )
    db.session.add(boring)

    cnt = len(record['layers']['index'])
    for i in range(cnt):
        layer = Layers(
            index=record['layers']['index'][i],
            soil_type=record['layers']['soil_type'][i],
            height=record['layers']['height'][i],
            evso=record['layers']['evso'][i],
            tuw=record['layers']['tuw'][i],
            water_content=record['layers']['water_content'][i],
            nval=record['layers']['nval'][i],
            cnval=record['layers']['cnval'][i],
            ssuu=record['layers']['ssuu'][i],
            ssfv=record['layers']['ssfv'][i],
            ssms=record['layers']['ssms'][i],
            ssqt=record['layers']['ssqt'][i],
            qc=record['layers']['qc'][i],
            fsl=record['layers']['fsl'][i],
            liquid_limit=record['layers']['liquid_limit'][i],
            plasticity=record['layers']['plasticity'][i],
            boring=boring)
        db.session.add(layer)

    pile = Piles(
        type=record['type'],
        shape=record['shape'],
        length=record['length'],
        emb_length=record['emb_length'],
        diameter=record['diameter'],
        circumference=record['circumference'],
        square_circ=record['square_circ'],
        aeol=record['aeol'],
        weight=record['weight'] * 1000,
        dratio=record['dratio'],
        tapered=record['tapered'],
        vibro=record['vibro'],
        cased=record['cased'],
        predrilled=record['predrilled'],
        relief_drilled=record['relief_drilled'],
        jetted=record['jetted'],
        project=prj
    )
    db.session.add(pile)

    load_test = LoadTests(
        direction='Compression (Static)' if record['direction'] == 'COMP'
        else 'Tension (Static)',
        setup_time=record['setup_time'],
        pile=pile
    )
    db.session.add(load_test)

    if qs:
        i_slt = 1
        for i in qs:
            static_test = StaticTests(
                index=i_slt,
                load=i[0],
                displacement=i[1],
                load_test=load_test
            )
            db.session.add(static_test)
            i_slt += 1

    if record['half_inch_capacity']:
        ic = InterpCapacities(
            load=record['half_inch_capacity'],
            displacement=0.5,
            type='Load @ 0.5 inches',
            origin='source DB',
            load_test=load_test
        )
        db.session.add(ic)

    if record['davisson_capacity']:
        ic = InterpCapacities(
            load=record['davisson_capacity'],
            displacement=record['davisson_displacement'],
            type='Standard Davisson',
            origin='source DB',
            load_test=load_test
        )
        db.session.add(ic)

    if record['brown_capacity']:
        ic = InterpCapacities(
            load=record['brown_capacity'],
            type='Brown',
            origin='source DB',
            load_test=load_test
        )
        db.session.add(ic)

    if record['max_load']:
        ic = InterpCapacities(
            load=record['max_load'],
            type='Maximum Load',
            origin='source DB',
            load_test=load_test
        )
        db.session.add(ic)

    if record['max_displacement']:
        ic = InterpCapacities(
            displacement=record['max_displacement'],
            type='Maximum Displacement',
            origin='source DB',
            load_test=load_test
        )
        db.session.add(ic)

    db.session.commit()
