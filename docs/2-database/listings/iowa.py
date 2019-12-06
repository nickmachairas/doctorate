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


# -- Description to Soil Type Dictionary ------------------------------------ #
iowa_soil_dict = {
    '4" Crushed Stone to Dark Clayey Silt': "CLSI",
    "Boulder": "GRAV",
    "Boulders": "GRAV",
    "Bouldery Clay": "GVCL",
    "Bouldery Gravel": "GRAV",
    "Broken Limestone": "ROCK",
    "Broken Limestone w/occ. Hard Layer": "ROCK",
    "Cemented Fine Sand": "SAND",
    "Clay": "CLAY",
    "Clayey Sand": "CLSA",
    "Clayey Silt": "CLSI",
    "Clayey Silt to Silty Clay": "CLSI",
    "Coarse Gavelly Sand": "GVSA",
    "Coarse Gravel": "GRAV",
    "Coarse Gravelly Sand": "GVSA",
    "Coarse Gravelly Sand w/ Boulders": "GVSA",
    "Coarse Gravelly Sand w/ Clay": "GVSA",
    "Coarse Gravelly Sand w/occ. Small Boulders": "GVSA",
    "Coarse Sand": "SAND",
    "Coarse Sand and Gravel": "SAGV",
    "Coarse Sand w/ Gravel": "SAGV",
    "Coarse Sand w/occ. Boulders": "SAGV",
    "Coarse Sand w/occ. Small Boulders": "SAGV",
    "Coarse and Gravelly Sand": "GVSA",
    "Concrete": "ROCK",
    "Dark Brown Silty Clay": "SICL",
    "Dark Brown Silty Clay Loam": "SICL",
    "Dark Gray Silty Loam": "SICL",
    "Dark Yellow Brown Silty Clay Loam": "SICL",
    "Dense Fine Sand": "SAND",
    "Dense Fine to Coarse Sand - Trace Gravel": "SAND",
    "Dense Sand": "SAND",
    "Dense, Gray Medium Sand w/ Clay Lenses": "SAND",
    "Dense, Gray, Saturated Coarse Sand": "SAND",
    "Fine Sand": "SAND",
    "Fine Sand - Slightly Cemented": "SAND",
    "Fine Sand - Some Clay Binder": "SAND",
    "Fine Sand - Traces of Gravek": "SAND",
    "Fine Sand - Traces of Gravel": "SAND",
    "Fine Sand w/ Silty Clay": "CLSA",
    "Fine Sand w/ Thin Clay Layers": "CLSA",
    "Fine Sand w/occ. Clay": "CLSA",
    "Fine Sand w/occ. Thin Clay Layers": "CLSA",
    "Fine Silty Sand": "SAND",
    "Fine to Coarse Sand": "SAND",
    "Fine to Medium Sand": "SAND",
    "Firm Clay": "CLAY",
    "Firm Glacial Clay": "CLAY",
    "Firm Glacial Clay Fill": "CLAY",
    "Firm Gumbotil": "CLAY",
    "Firm Mixed Clay - Fill": "CLAY",
    "Firm Sand and Glacial Clay": "SACL",
    "Firm Sand w/ Silty Clay": "SACL",
    "Firm Sandy Clay": "SACL",
    "Firm Sandy Clay Fill": "SACL",
    "Firm Sandy Glacial Clay": "SACL",
    "Firm Sandy Glacial Clay - Very Wet": "SACL",
    "Firm Sandy Glacial Clay Fill": "SACL",
    "Firm Sandy Silty Clay": "SACL",
    "Firm Shale": "SHEL",
    "Firm Shale w/occ. Medium Hard Layers": "SHEL",
    "Firm Silt": "SILT",
    "Firm Silt w/occ. Sand Seams": "SASI",
    "Firm Silty Clay": "SICL",
    "Firm Silty Clay Fill": "SICL",
    "Firm Silty Clay w/ Very Firm Layers": "SICL",
    "Firm Silty Clay w/occ. Thin Sand Layers": "SICL",
    "Firm Silty Glacial Clay": "SICL",
    "Firm Silty Glacial Clay w/occ. Sand Seams": "SICL",
    "Firm Silty Sandy Clay": "SICL",
    "Firm Silty Sandy Clay Fill": "SICL",
    "Firm to Very Firm Glacial Clay": "CLAY",
    "Firm to Very Firm Glacial Clay w/occ. Sand Seams": "CLAY",
    "Firm to Very Firm Sandy Glacial Clay": "CLAY",
    "Firm to Very Firm Sandy Silty Clay - Travel Gravel": "SICL",
    "Glacial Clay": "CLAY",
    "Glacial Till": "CLAY",
    "Gravel": "GRAV",
    "Gravelly Coarse Sand": "GVSA",
    "Gravelly Sand": "GVSA",
    "Gravelly Sand w/ Boulders": "GVSA",
    "Gravelly Sand w/occ. Boulders": "GVSA",
    "Gravelly Sand w/occ. Small Boulders and Thin Clay Layers": "GVSA",
    "Hard, Gray, Moist Clay Loam": "CLAY",
    "Large Boulders": "GRAV",
    "Light Brown Gray Silty Clay Loam": "SICL",
    "Loose Brown Fine Sand": "SAND",
    "Loose Brown Sandy Silt": "SASI",
    "Loose Brown Silt": "SILT",
    "Loose Gravelly Fine to Coarse Sand - Trace Silt": "SAND",
    "Loose Sand": "SAND",
    "Loose, Brown, Wet Medium Sand": "SAND",
    "Medium Coarse Sand": "SAND",
    "Medium Compact Brown and Gray Fine Sand (Organic at 41.0')": "SAND",
    "Medium Compact Brown and Gray Fine Sand w/ Organic Material": "SAND",
    "Medium Compact Brown and Gray Sand": "SAND",
    "Medium Dense Sand": "SAND",
    "Medium Dense to Dense, Gray Brown, Moist Sand": "SAND",
    "Medium Fine Sand": "SAND",
    "Medium Gray Clay": "CLAY",
    "Medium Gray Gravelly Sandy Loam": "SACL",
    "Medium Gray Silty Clay Loam": "SICL",
    "Medium Gray Silty Loam": "SICL",
    "Medium Hard Limestone": "ROCK",
    "Medium Packed Sand": "SAND",
    "Medium Sand": "SAND",
    "Medium Sand w/ Boulders": "GVSA",
    "Medium Sand w/ Clay": "CLSA",
    "Medium Sand w/ Silt": "SISA",
    "Medium Sand w/ Silt Seams": "SISA",
    "Medium Sand w/occ. Clay": "CLSA",
    "Medium Sand w/occ. Clay Layers": "CLSA",
    "Medium Sand w/occ. Gravel": "GVSA",
    "Medium Sand w/occ. Gravel and Boulder Layers": "GVSA",
    "Medium Stiff Gray Clay": "CLAY",
    "Medium Stiff Gray Clay w/ Fine Sand Band": "SACL",
    "Medium Yellow Brown Gravelly Sand": "SAND",
    "Medium to Coarse Sand": "SAND",
    "Organic Silt": "SILT",
    "Packed Sand": "SAND",
    "Peat": "PEAT",
    "Railroad Fill": "SAND",
    "Rip Rap": "GRAV",
    "Sand": "SAND",
    "Sand - Trace of Gravel": "SAND",
    "Sand - Traces of Gravel": "SAND",
    "Sand - Traces of Gravel (Very Slightly Cemented)": "SAND",
    "Sand and Boulders": "GVSA",
    "Sand and Gravel": "SAGV",
    "Sand and Gravel w/ Numerous Boulders": "SAGV",
    "Sand and Gravel w/occ. Small Boulders": "SAGV",
    "Sand to Silty Sand": "SISA",
    "Sand w/ Trace Gravel": "GVSA",
    "Sand w/ Traces of Gravel": "GVSA",
    "Sand w/ Traces of Gravel Very Slightly Cemented": "GVSA",
    "Sand w/occ. 0.1 Foot Thick Clay Layers": "CLSA",
    "Sand w/occ. Clay Layer": "CLSA",
    "Sand w/occ. Clay Layers": "CLSA",
    "Sand w/occ. Gravel": "GVSA",
    "Sand w/occ. Thin Clay Layers": "CLSA",
    "Sand w/occ. Very Thin Clay Layer": "CLSA",
    "Sand w/occ. Very Thin Clay Layers": "CLSA",
    "Sandstone": "ROCK",
    "Sandy Glacial Clay Till": "SACL",
    "Sandy Gravel w/occ. Boulders": "GVSA",
    "Sandy Silt to Clayey Silt": "SASI",
    "Sandy Silty Clay": "SICL",
    "Sensitive Fine Grained": "SISA",
    "Shale": "SHEL",
    "Silt": "SILT",
    "Silty Clay": "SICL",
    "Silty Clay to Clay": "SICL",
    "Silty Sand": "SISA",
    "Silty Sand to Sand": "SISA",
    "Silty Sand to Sandy Silt": "SISA",
    "Slightly Packed Sand": "SAND",
    "Soft Sandy Clay": "SACL",
    "Soft Sandy Silty Clay": "SICL",
    "Soft Sandy Silty Clay w/ Sand Layers": "SACL",
    "Soft Silty Clay": "SICL",
    "Soft Silty Clay w/ Sand Seams": "SICL",
    "Soft Silty Clay w/ Sand Streaks": "SICL",
    "Soft Silty Sandy Clay": "SICL",
    "Soft Stiff Sandy Silty Clay": "SICL",
    "Soft to Stiff Sandy Clay": "SACL",
    "Soft to Stiff Sandy Silty Clay": "SACL",
    "Soft to Stiff Silt": "SILT",
    "Soft to Stiff Silty Clay": "SICL",
    "Soft to Stiff Silty Clay w/ Silty Sand Lenses": "SICL",
    "Soft to Stiff Silty Sand": "SISA",
    "Soft to Stiff Silty Sandy Clay": "SACL",
    "Soft, Yellow-Brown, Very Moist Silty Clay Loam": "SICL",
    "Stiff Black-Brown Sandy Clayey Fill": "SACL",
    "Stiff Brown Gray Silt": "SILT",
    "Stiff Clay Fill": "CLAY",
    "Stiff Dark Brown Silt": "SILT",
    "Stiff Firm Sandy Glacial Clay": "CLAY",
    "Stiff Firm Silty Clay": "SICL",
    "Stiff Gray Glacial Clay": "CLAY",
    "Stiff Olive Gray Silt": "SILT",
    "Stiff Sand and Clay": "SACL",
    "Stiff Sand and Silty Clay": "SICL",
    "Stiff Sand w/ Silt": "SISA",
    "Stiff Sandy Clay": "SACL",
    "Stiff Sandy Clay Fill": "SACL",
    "Stiff Sandy Clay w/occ. Sand Seams": "SACL",
    "Stiff Sandy Glacial Clay": "SACL",
    "Stiff Sandy Silty Clay": "SACL",
    "Stiff Silt": "SILT",
    "Stiff Silt Sloughing w/occ. Small Sand Seams": "SASI",
    "Stiff Silty Clay": "SICL",
    "Stiff Silty Clay (Sloughing)": "SICL",
    "Stiff Silty Clay - Dike Fill": "SICL",
    "Stiff Silty Clay Fill": "SICL",
    "Stiff Silty Clay Road Fill": "SICL",
    "Stiff Silty Clay w/ Traces of Sand": "SICL",
    "Stiff Silty Sand": "SISA",
    "Stiff Silty Sandy Clay": "SICL",
    "Stiff Soft Silty Clay": "SICL",
    "Stiff to Firm Sand and Clay": "SACL",
    "Stiff to Firm Silt": "SILT",
    "Stiff to Firm Silty Clay": "SICL",
    "Stiff, Black, Moist Silty Clay": "SICL",
    "Stiff, Gray, Moist Silty Clay": "SICL",
    "Stiff, Gray, Saturated Silty Clay": "SICL",
    "Very Compact Gray Fine Sand": "SAND",
    "Very Compact Gray Sand and Gravel": "SAGV",
    "Very Firm Glacial Clay": "CLAY",
    "Very Firm Glacial Clay w/ Boulders": "CLAY",
    "Very Firm Glacial Clay w/ Sand Seams": "SACL",
    "Very Firm Glacial Clay w/occ. Boulders": "CLAY",
    "Very Firm Glacial Clay w/occ. Hard Layers": "CLAY",
    "Very Firm Glacial Clay w/occ. Sand Seams": "SACL",
    "Very Firm Glacial Clay w/occ. Small Boulders": "CLAY",
    "Very Firm Sand and Glacial Clay": "SACL",
    "Very Firm Sandy Clay": "SACL",
    "Very Firm Sandy Glacial Clay": "SACL",
    "Very Firm Shale": "SHEL",
    "Very Firm Silt": "SILT",
    "Very Firm Silty Clay": "SICL",
    "Very Firm Silty Glacial Clay": "SICL",
    "Very Firm to Hard Sandy Silty Clay - Trace Gravel": "SICL",
    "Very Soft Gray Shale w/ Coal Seam": "SHEL",
    "Very Soft Silt": "SILT",
    "Very Soft Silty Clay": "SICL",
    "Very Soft to Soft Sandy Silt": "SASI",
    "Very Stiff Brown Gray Silt": "SILT",
    "Very Stiff Clay Loam": "CLAY",
    "Very Stiff Dark Gray Silt": "SILT",
    "Very Stiff Silty Clay": "SICL",
    "Very Stiff, Dark Brown, Moist Silty Clay": "SICL",
    "Very Stiff, Gray, Moist Clay Loam": "CLAY",
    "Wood": "PEAT",
}


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
            ].iloc[0],
            emb_length=emb_pile_length,
            length=pile_length,
            diameter=pile_types.loc[
                pile_types['ID'] == plt_records['Pile Type'][i], 'Diameter'
            ].iloc[0],
            cross_area=plt_records['Pile Cross-Sectional Area'][i],
            weight=plt_records['Weight of Pile'][i],
            predrill_depth=plt_records['Initial Bored Hole Depth'][i] if
            plt_records['Initial Bored Hole Depth'][i] != 0 else None,
            predrilled=True if plt_records['Initial Bored Hole Depth'][i] != 0
            else None,
            date_driven=pd.to_datetime(
                plt_records['Date Driven'][i] if not
                pd.isna(plt_records['Date Driven'][i]) else None),
            design_load=plt_records['Design Load'][i],
            toe_elevation=plt_records['Pile Toe Elevation'][i],
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
                index=layers['Soil Layer'][l],
                soil_type=iowa_soil_dict[layers['Material Description'][l]] if
                not pd.isna(layers['Material Description'][l]) else None,
                description=layers['Material Description'][l],
                height=layers['Thickness'][l],
                nval=layers['NAVG'][l],
                iowa_unit_friction=layers['Unit Friction'][l],
                iowa_total_friction=layers['Total Friction'][l],
            )
            db.session.add(layer)

        # -- Adding load test data ------------------------------------------ #
        load_test = LoadTests(
            pile=pile,
            direction='COMP',
            tested_by=plt_records['Tested By'][i],
            date_tested=pd.to_datetime(
                plt_records['Date Tested'][i] if not
                pd.isna(plt_records['Date Tested'][i]) else None),
            rebound_time=plt_records['Rebound Time Duration'][i],
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
            iowa_borehole_count=plt_records['Total Number of Boreholes'][i],
            iowa_spt_count=plt_records['Boreholes With SPT Data'][i],
            iowa_borehole_near_pile=plt_records[
                'Borehole at Test Pile Location'][i]
        )
        db.session.add(misc)

    db.session.commit()
