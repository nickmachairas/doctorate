# -- Imports ---------------------------------------------------------------- #
import os
import pandas as pd
from tqdm import tqdm
from app import db
from .aux import data_owner
from app.models import Locations, Projects, Piles, LoadTests, StaticTests, \
    InterpCapacities, Borings


# -- File Paths ------------------------------------------------------------- #
LAPTLD_DATA_DIR = os.path.join('app', 'etl', '_data_sources', 'lapltd')
dt_projects_path = os.path.join(LAPTLD_DATA_DIR, 'dtProjects.txt')
dt_staticdata_path = os.path.join(LAPTLD_DATA_DIR, 'dtStaticData.txt')
dt_testevents_path = os.path.join(LAPTLD_DATA_DIR, 'dtTestEvents.txt')
dt_testpiles_path = os.path.join(LAPTLD_DATA_DIR, 'dtTestPiles.txt')
lst_parishes_path = os.path.join(LAPTLD_DATA_DIR, 'lstParishes.txt')
lst_contractors_path = os.path.join(LAPTLD_DATA_DIR, 'lstContractors.txt')
lst_piletype_path = os.path.join(LAPTLD_DATA_DIR, 'lstPileType.csv')


# -- Creating Pandas DataFrames --------------------------------------------- #
dt_projects = pd.read_csv(dt_projects_path)
dt_staticdata = pd.read_csv(dt_staticdata_path)
dt_testevents = pd.read_csv(dt_testevents_path)
dt_testpiles = pd.read_csv(dt_testpiles_path)
lst_parishes = pd.read_csv(lst_parishes_path)
lst_contractors = pd.read_csv(lst_contractors_path)
lst_piletype = pd.read_csv(lst_piletype_path)


# -- Helper Functions ------------------------------------------------------- #
def add_loc_proj(prj_id, pile_id):
    """ Compiles location and project data given an index for the tbl_project
    DataFrame
    """
    # -- Adding Location Data ----------------------------------------------- #
    parish_id = int(dt_projects['Parish_1'][dt_projects.ID == prj_id])
    parish = lst_parishes['Parish_Name'][lst_parishes.ID == parish_id].values[0]
    lat = dt_testpiles['Latitude'][dt_testpiles.ID == pile_id].values[0]
    lon = dt_testpiles['Longitude'][dt_testpiles.ID == pile_id].values[0]
    loc = Locations(
        county=parish,
        state='Louisiana',
        country='USA',
        latitude=lat,
        longitude=lon
    )
    db.session.add(loc)

    # -- Adding Project Data ------------------------------------------------ #
    contr_id = int(dt_projects['Contractor'][dt_projects.ID == prj_id])
    contractor = lst_contractors['Contractor'][
        lst_contractors.ID == contr_id].values[0]
    source_ref = 'From: {}'.format(
        source_dic[dt_projects['Source'][dt_projects.ID == prj_id].values[0]])
    number = '{}; {}'.format(
        dt_projects['Project_Num_H'][dt_projects.ID == prj_id].values[0],
        dt_projects['Project_Num_old'][dt_projects.ID == prj_id].values[0])
    prj = Projects(
        location=loc,
        user_id=data_owner().id,
        source_db='LTRC LAPLTD',
        source_id=prj_id,
        source_ref=source_ref,
        number=number,
        title=dt_projects['Project_Name'][dt_projects.ID == prj_id].values[0],
        site_name=dt_projects['Route'][dt_projects.ID == prj_id].values[0] if
        not pd.isna(dt_projects['Route'][dt_projects.ID == prj_id].values[0])
        else None,
        contractor=contractor
    )

    return prj


def add_pile_data(pile_id, prj):
    """ Compiles the pile data
    """
    ptype_id = dt_testpiles['Pile_Type'][dt_testpiles.ID == pile_id].values[0]
    ptype = lst_piletype['Pile_Type'][lst_piletype.ID == ptype_id].values[0]
    shape = lst_piletype['Pile_Shape'][lst_piletype.ID == ptype_id].values[0] \
        if not pd.isna(
        lst_piletype['Pile_Shape'][lst_piletype.ID == ptype_id].values[0]) \
        else None
    diam = lst_piletype['Diam_Pile'][lst_piletype.ID == ptype_id].values[0] \
        if not pd.isna(
        lst_piletype['Diam_Pile'][lst_piletype.ID == ptype_id].values[0]) \
        else None
    dvoid = lst_piletype['Diam_Void'][lst_piletype.ID == ptype_id].values[0] \
        if not pd.isna(
        lst_piletype['Diam_Void'][lst_piletype.ID == ptype_id].values[0]) \
        else None
    thickness = (diam - dvoid)/2 if dvoid else None
    circ = lst_piletype['Perimeter'][lst_piletype.ID == ptype_id].values[0]/12 \
        if not pd.isna(
        lst_piletype['Perimeter'][lst_piletype.ID == ptype_id].values[0]) \
        else None
    scirc = lst_piletype['HP Box Perimeter'][
                lst_piletype.ID == ptype_id].values[0]/12 if not pd.isna(
        lst_piletype['HP Box Perimeter'][
            lst_piletype.ID == ptype_id].values[0]) else None
    area = lst_piletype['Area_Gross'][lst_piletype.ID == ptype_id].values[0] \
        if not pd.isna(
        lst_piletype['Area_Gross'][lst_piletype.ID == ptype_id].values[0]) \
        else None

    pile = Piles(
        project=prj,
        type=ptype,
        shape=shape,
        diameter=diam,
        wall_thickness=thickness,
        circumference=circ,
        square_circ=scirc,
        cross_area=area,
        name=dt_testpiles['Pile_Name'][dt_testpiles.ID == pile_id].values[0],
        date_driven=pd.to_datetime(
            dt_testpiles['Date_Driven'][
                dt_testpiles.ID == pile_id].values[0]),
        length=dt_testpiles['Length'][dt_testpiles.ID == pile_id].values[0],
        remarks=dt_testpiles['Notes'][dt_testpiles.ID == pile_id].values[0]
        if not pd.isna(
            dt_testpiles['Notes'][dt_testpiles.ID == pile_id].values[0])
        else None,
        modulus=dt_testpiles['Modulus'][
            dt_testpiles.ID == pile_id].values[0] if not pd.isna(
            dt_testpiles['Modulus'][dt_testpiles.ID == pile_id].values[0])
        else None,
        design_load=dt_testpiles['Load_Design'][
            dt_testpiles.ID == pile_id].values[0] * 2 if not pd.isna(
            dt_testpiles['Load_Design'][dt_testpiles.ID == pile_id].values[0])
        else None
    )

    return pile


def add_boring_data(pile_id, prj):
    """ Compiles the few available boring data
    """
    near_bor = dt_testpiles['Near_Boring'][
        dt_testpiles.ID == pile_id].values[0] if not pd.isna(
        dt_testpiles['Near_Boring'][dt_testpiles.ID == pile_id].values[0]) \
        else None
    near_cpt = dt_testpiles['Near_CPT'][
        dt_testpiles.ID == pile_id].values[0] if not pd.isna(
        dt_testpiles['Near_CPT'][dt_testpiles.ID == pile_id].values[0]) \
        else None
    if near_bor and not near_cpt:
        bor_name = near_bor
    elif not near_bor and near_cpt:
        bor_name = near_cpt
    elif not near_bor and not near_cpt:
        bor_name = None
    else:
        bor_name = near_bor + '; ' + near_cpt

    boring = Borings(
        project=prj,
        name=bor_name,
        predom_soil=soil_dict[dt_testpiles['Soil_Type'][
            dt_testpiles.ID == pile_id].values[0]] if not pd.isna(
            dt_testpiles['Soil_Type'][dt_testpiles.ID == pile_id].values[0]
        ) else None,
        elevation=dt_testpiles['Elev_GS'][dt_testpiles.ID == pile_id].values[0]
    )

    return boring


def add_static_test_data(test_event_id, load_test):
    """ Compiles the static test data
    """
    slt_points = dt_staticdata[dt_staticdata.lt_Event == test_event_id]
    i_lt = 1
    for i in slt_points.index:
        slt = StaticTests(
            load_test=load_test,
            index=i_lt,
            load=slt_points['lt_Load'][i] * 2,
            displacement=slt_points['lt_Deflection'][i]
        )
        i_lt += 1
        db.session.add(slt)


def add_interp_data(i, load_test):
    """ Compiles the interpreted capacity data
    """
    load = dt_testevents['Capacity_Ult'][i] * 2 \
        if not pd.isna(dt_testevents['Capacity_Ult'][i]) else None
    if load:
        method = dt_testevents['Ult_Cap_Method'][i] if not \
            pd.isna(dt_testevents['Ult_Cap_Method'][i]) else None
        if method == 'Davisson':
            method = 'Standard Davisson'
        elif method is None:
            method = 'Unknown/Not Specified'
        capacity = InterpCapacities(
            load_test=load_test,
            load=load,
            type=method,
            origin='source DB'
        )
        db.session.add(capacity)


# -- Main Import Function --------------------------------------------------- #
def load_lapltd_records():
    """ Iterates through source files and adds the LTRC LAPLTD records to the
    database
    """
    print('--- Importing LTRC LAPLTD records ---')
    for i in tqdm(range(len(dt_testevents))):
        test_event_id = int(dt_testevents['ID'][i])
        pile_id = int(dt_testevents['Pile_Name'][i])
        prj_id = int(dt_testpiles['Project_ID'][dt_testpiles.ID == pile_id])
        # print(test_event_id, 'Project ID:', prj_id, 'Pile_ID:', pile_id)

        # -- Adding Project Data -------------------------------------------- #
        prj = add_loc_proj(prj_id, pile_id)
        db.session.add(prj)

        # -- Adding Pile Data ----------------------------------------------- #
        pile = add_pile_data(pile_id, prj)
        db.session.add(pile)

        # -- Adding Boring Data --------------------------------------------- #
        boring = add_boring_data(pile_id, prj)
        db.session.add(boring)

        # -- Adding Load Test Data ------------------------------------------ #
        load_test = LoadTests(
            pile=pile,
            direction=lt_dir[dt_testevents['Event_Type'][i]],
            remarks=dt_testevents['Notes'][i]
            if not pd.isna(dt_testevents['Notes'][i]) else None,
        )
        db.session.add(load_test)

        # -- Adding Static Test Data ---------------------------------------- #
        add_static_test_data(test_event_id, load_test)

        # -- Adding Interpreted Data ---------------------------------------- #
        add_interp_data(i, load_test)

    db.session.commit()
