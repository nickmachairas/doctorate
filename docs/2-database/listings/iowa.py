# -- Imports ---------------------------------------------------------------- #
import os
import pandas as pd
from app import db
from .aux import data_owner
from app.models import Locations, Projects, Piles, Borings, Layers, LoadTests, \
    StaticTests, InterpCapacities, CalcCapacities, Attachments, Misc
from tqdm import tqdm


# -- File Paths ------------------------------------------------------------- #
IOWA_DATA_DIR = os.path.join('app', 'etl', '_data_sources', 'iowa')
plt_records_path = os.path.join(IOWA_DATA_DIR, 'Pile Load Test Records.txt')
counties_path = os.path.join(IOWA_DATA_DIR, 'Iowa Counties.txt')
pile_types_path = os.path.join(IOWA_DATA_DIR, 'Pile Types.txt')
avg_soil_path = os.path.join(IOWA_DATA_DIR, 'Average Soil Profile.txt')
slt_path = os.path.join(IOWA_DATA_DIR, 'Static Load Test Results.txt')


# -- Main Import Function --------------------------------------------------- #
def load_iowa_records():
    """ Iterates through source files and adds the Iowa PILOT records to the
    database
    """
    plt_records = pd.read_csv(plt_records_path)
    counties = pd.read_csv(counties_path)
    pile_types = pd.read_csv(pile_types_path)
    avg_soil = pd.read_csv(avg_soil_path)
    slt_results = pd.read_csv(slt_path)

    print('--- Importing Iowa PILOT records ---')
    for i in tqdm(range(len(plt_records))):

        # -- Adding Location Data ------------------------------------------- #
        loc = Locations(
            county=counties.loc[
                counties['ID'] == plt_records['County'][i], 'County'].iloc[0],
            township=plt_records['Township'][i],
            description=plt_records['Pile Location'][i])
        db.session.add(loc)

        # -- Adding Project Data -------------------------------------------- #
        wt_loc = plt_records['Water Table Location'][i]
        if pd.isna(wt_loc):
            desc = None
        else:
            desc = 'Water Table ' + str(wt_loc)
        prj = Projects(
            user_id=data_owner().id,
            source_db='Iowa PILOT',
            source_id=int(plt_records['ID'][i]),
            contractor=plt_records['Contractor'][i],
            number=plt_records['Project Number'][i],
            description=desc,
            location=loc)
        db.session.add(prj)

        # -- Adding Pile Data ----------------------------------------------- #
        emb_pile_length = plt_records['Embedded Pile Length'][i]
        pile_length = plt_records['Pile Length'][i]
        if pd.isna(pile_length):
            pile_length = pile_types.loc[
                    pile_types['ID'] == plt_records['Pile Type'][i], 'Length'
            ].iloc[0]
        if pd.isna(pile_length):
            pile_length = emb_pile_length
        pile = Piles(
            project=prj,
            type=pile_types.loc[
                pile_types['ID'] == plt_records['Pile Type'][i], 'Type'
            ].iloc[0],
            shape=pile_types.loc[
                pile_types['ID'] == plt_records['Pile Type'][i], 'Shape'
            ].iloc[0] if not pd.isna(pile_types.loc[
                pile_types['ID'] == plt_records['Pile Type'][i], 'Shape'
            ].iloc[0]) else None,
            emb_length=emb_pile_length,
            length=pile_length,
            diameter=pile_types.loc[
                pile_types['ID'] == plt_records['Pile Type'][i], 'Diameter'
            ].iloc[0] if not pd.isna(pile_types.loc[
                pile_types['ID'] == plt_records['Pile Type'][i], 'Diameter'
            ].iloc[0]) else None,
            cross_area=plt_records['Pile Cross-Sectional Area'][i] if not
            pd.isna(plt_records['Pile Cross-Sectional Area'][i]) else None,
            weight=plt_records['Weight of Pile'][i] if not pd.isna(
                plt_records['Weight of Pile'][i]) else None,
            predrill_depth=plt_records['Initial Bored Hole Depth'][i] if
            plt_records['Initial Bored Hole Depth'][i] != 0 else None,
            predrilled=True if plt_records['Initial Bored Hole Depth'][i] != 0
            else None,
            date_driven=pd.to_datetime(
                plt_records['Date Driven'][i] if not
                pd.isna(plt_records['Date Driven'][i]) else None),
            design_load=plt_records['Design Load'][i] if not
            pd.isna(plt_records['Design Load'][i]) else None,
            toe_elevation=plt_records['Pile Toe Elevation'][i] if not
            pd.isna(plt_records['Pile Toe Elevation'][i]) else None,
        )
        db.session.add(pile)

        # -- Adding Soil Data ----------------------------------------------- #
        soil_class = {1: 'CLAY', 2: 'SAND', 3: 'SACL'}
        p_soil = plt_records['Test Site Soil Classification'][i]
        boring = Borings(
            project=prj,
            name='Average Soil Profile',
            predom_soil=soil_class[p_soil] if not pd.isna(p_soil) else None,
            remarks=plt_records['Borehole Numbers at Test Pile Location'][i],
        )
        db.session.add(boring)

        layers = avg_soil[avg_soil['Record ID'] == i+1]
        for l in layers.index:
            layer = Layers(
                boring=boring,
                index=layers['Soil Layer'][l] if not
                pd.isna(layers['Soil Layer'][l]) else None,
                soil_type=iowa_soil_dict[layers['Material Description'][l]] if
                not pd.isna(layers['Material Description'][l]) else None,
                description=layers['Material Description'][l],
                height=layers['Thickness'][l],
                nval=layers['NAVG'][l]
                if not pd.isna(layers['NAVG'][l]) else None,
                iowa_unit_friction=layers['Unit Friction'][l],
                iowa_total_friction=layers['Total Friction'][l],
            )
            db.session.add(layer)

        # -- Adding load test data ------------------------------------------ #
        load_test = LoadTests(
            pile=pile,
            direction='Compression (Static)',
            tested_by=plt_records['Tested By'][i],
            date_tested=pd.to_datetime(
                plt_records['Date Tested'][i] if not
                pd.isna(plt_records['Date Tested'][i]) else None),
            rebound_time=plt_records['Rebound Time Duration'][i] if not
            pd.isna(plt_records['Rebound Time Duration'][i]) else None,
            rebound_displacement=plt_records['Rebound Gauge Reading'][i],
            remarks=plt_records['Static Load Test Remarks'][i],
            reliable=True
            if plt_records['Load Test Reliability Classification'][i] == 1
            else False,
        )
        db.session.add(load_test)

        static_test = slt_results[slt_results['Record ID'] == i+1]
        i_slt = 1
        for p in static_test.index:
            slt_point = StaticTests(
                index=i_slt,
                load=static_test['Load (Tons)'][p] * 1000,
                displacement=static_test['Gauge Reading (in)'][p],
                load_test=load_test
            )
            db.session.add(slt_point)
            i_slt += 1

        # -- Adding Interpreted Capacity Data ------------------------------- #
        interp_dict = {
            'Maximum Applied Load': 'Maximum Load',
            'Highest Gauge Reading': 'Maximum Displacement',
            'Davisson Pile Capacity': 'Standard Davisson'
        }

        for key in interp_dict:
            ival = plt_records[key][i]
            if not pd.isna(ival) and float(ival) > 0:
                ic = InterpCapacities(
                    load=float(ival) * 2 if key != 'Highest Gauge Reading'
                    else None,
                    displacement=float(ival) if key == 'Highest Gauge Reading'
                    else None,
                    type=interp_dict[key],
                    origin='source DB',
                    load_test=load_test)
                db.session.add(ic)

        # -- Adding Calculated Capacity Data -------------------------------- #
        calc_dict = {
            'Formula Bearing': 'Iowa DOT Modified ENR (bearing)',
            'Theoretical End Bearing': 'Iowa Theoretical End Bearing',
            'Theoretical Pile Capacity': 'Iowa Theoretical Capacity',
            'Blue Book Capacity': 'Iowa Blue Book Method',
            'SPT Capacity': 'Meyerhof',
            'Alpha Capacity': 'API 1984',
            'Beta Capacity': 'Beta Burland 1973',
            'Nordland Capacity': 'Nordlund',
            'ENR Capacity': 'ENR Formula',
            'Modified ENR Capacity': 'Iowa DOT Modified ENR',
            'Gates Capacity': 'Gates Formula',
            'FHWA Modified Gates Capacity': 'FHWA Modified Gates Formula',
            'Janbu Capacity': 'Janbu Formula',
            'PCUBC Capacity': 'Pacific Coast Uniform BC Formula',
            'WSDOT Capacity': 'Washington DOT Formula'
        }

        for key in calc_dict:
            cval = plt_records[key][i]
            if not pd.isna(cval) and float(cval) > 0:
                cc = CalcCapacities(
                    load=float(cval) * 2,
                    type=calc_dict[key],
                    origin='source DB',
                    pile=pile)
                db.session.add(cc)

        # -- Adding Attachments --------------------------------------------- #
        attach_attr = ['Attachments (1)', 'Attachments (2)', 'Attachments (3)',
                       'Attachments (4)', 'Attachments (5)', 'Attachments (6)']
        for attr in attach_attr:
            val = plt_records[attr][i]
            if not pd.isna(val):
                fname = val.split('#')[0]
                furl = val.split('#')[1]
                attachment = Attachments(
                    project=prj,
                    file_name=fname,
                    file_url=furl
                )
                db.session.add(attachment)

        # -- Adding Miscellaneous Data -------------------------------------- #
        misc = Misc(
            project=prj,
            iowa_test_folder=plt_records['Test Folder'][i],
            iowa_lab_number=plt_records['Lab Number'][i],
            iowa_design_number=plt_records['Design Number'][i],
            iowa_section=plt_records['Section'][i],
            iowa_date_reported=pd.to_datetime(
                plt_records['Date Reported'][i] if not
                pd.isna(plt_records['Date Reported'][i]) else None),
            iowa_record_complete=plt_records['Record Complete'][i],
            iowa_borehole_count=plt_records['Total Number of Boreholes'][i]
            if not pd.isna(
                plt_records['Total Number of Boreholes'][i]) else None,
            iowa_spt_count=plt_records['Boreholes With SPT Data'][i] if not
            pd.isna(plt_records['Boreholes With SPT Data'][i]) else None,
            iowa_borehole_near_pile=plt_records[
                'Borehole at Test Pile Location'][i]
        )
        db.session.add(misc)

    db.session.commit()
