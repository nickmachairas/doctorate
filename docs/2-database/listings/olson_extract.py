import re


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
        ll = [i if i not in ['0', '0.00', '0.000'] else None for i in line.split()]
        layer_dict['index'].append(li)
        layer_dict['soil_type'].append(ll[0])
        layer_dict['height'].append(float(ll[1]))
        layer_dict['evso'].append(float(ll[2]) if ll[2] else None)
        layer_dict['tuw'].append(float(ll[3]) * 1000 if ll[3] else None)  # UNITS!!!
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
