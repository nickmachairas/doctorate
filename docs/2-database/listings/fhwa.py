# -- Imports ---------------------------------------------------------------- #
import os
import pandas as pd
from tqdm import tqdm
from app import db
from .aux import data_owner
from app.models import Locations, Projects, Piles, LoadTests, StaticTests, \
    InterpCapacities, Borings, Layers
pd.options.mode.chained_assignment = None


# -- File Paths ------------------------------------------------------------- #
FHWA_DATA_DIR = os.path.join('app', 'etl', '_data_sources', 'fhwa')
tbl_project_path = os.path.join(FHWA_DATA_DIR, 'tbl_Project.txt')
lkp_StateAndFHWADistrict_path = os.path.join(
    FHWA_DATA_DIR, 'lkp_StateAndFHWADistrict.txt')
tbl_country_path = os.path.join(FHWA_DATA_DIR, 'lkp_Country.txt')
tbl_deepfoundation_path = os.path.join(FHWA_DATA_DIR, 'tbl_DeepFoundation.txt')
tbl_descaugercast_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionAugerCast.txt')
tbl_descconccylinder_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionCylinderConcrete.txt')
tbl_descdrilledshaft_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionDrilledShaft.txt')
tbl_deschpile_path = os.path.join(FHWA_DATA_DIR, 'tbl_DescriptionHPile.txt')
tbl_descmonotube_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionMonotube.txt')
tbl_descpolyconc_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionPolyConcrete.txt')
tbl_descsteelpipe_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionSteelPipe.txt')
tbl_descsteptaper_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_DescriptionStepTaper.txt')
tbl_desctimber_path = os.path.join(FHWA_DATA_DIR, 'tbl_DescriptionTimber.txt')
tbl_loadtest_path = os.path.join(FHWA_DATA_DIR, 'tbl_LoadTest.txt')
tbl_statictest_path = os.path.join(FHWA_DATA_DIR, 'tbl_LoadTestStatic.txt')
tbl_interp_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_LoadTestNominalResistance.txt')
tbl_exploration_path = os.path.join(FHWA_DATA_DIR, 'tbl_Exploration.txt')
tbl_explsoilboring_path = os.path.join(
    FHWA_DATA_DIR, 'tbl_ExplorationSoilLayerBoring.txt')
tbl_explboring_path = os.path.join(FHWA_DATA_DIR, 'tbl_ExplorationBoring.txt')
tbl_expllab_path = os.path.join(FHWA_DATA_DIR, 'tbl_ExplorationLabResults.txt')


# -- Creating Pandas DataFrames --------------------------------------------- #
tbl_project = pd.read_csv(tbl_project_path)
lkp_stateandfhwadistrict = pd.read_csv(lkp_StateAndFHWADistrict_path)
tbl_country = pd.read_csv(tbl_country_path)
tbl_deepfoundation = pd.read_csv(tbl_deepfoundation_path)
tbl_descaugercast = pd.read_csv(tbl_descaugercast_path)
tbl_descconccylinder = pd.read_csv(tbl_descconccylinder_path)
tbl_descdrilledshaft = pd.read_csv(tbl_descdrilledshaft_path)
tbl_deschpile = pd.read_csv(tbl_deschpile_path)
tbl_descmonotube = pd.read_csv(tbl_descmonotube_path)
tbl_descpolyconc = pd.read_csv(tbl_descpolyconc_path)
tbl_descsteelpipe = pd.read_csv(tbl_descsteelpipe_path)
tbl_descsteptaper = pd.read_csv(tbl_descsteptaper_path)
tbl_desctimber = pd.read_csv(tbl_desctimber_path)
tbl_loadtest = pd.read_csv(tbl_loadtest_path)
tbl_statictest = pd.read_csv(tbl_statictest_path, low_memory=False)
tbl_interp = pd.read_csv(tbl_interp_path)
tbl_exploration = pd.read_csv(tbl_exploration_path)
tbl_explsoilboring = pd.read_csv(tbl_explsoilboring_path)
tbl_explsoilboring = tbl_explsoilboring[
    tbl_explsoilboring['dbl_KeyDepthToBottom'] != 0]
tbl_explsoilboring.reset_index(inplace=True, drop=True)
tbl_explsoilboring['txt_KeyExplorationName'] = tbl_explsoilboring[
    'txt_KeyExplorationName'].str.strip()
tbl_explboring = pd.read_csv(tbl_explboring_path)
tbl_explboring['txt_KeyExplorationName'] = tbl_explboring[
    'txt_KeyExplorationName'].str.strip()
tbl_expllab = pd.read_csv(tbl_expllab_path)
tbl_expllab['txt_KeyExplorationName'] = tbl_expllab[
    'txt_KeyExplorationName'].str.strip()


# -- Helper Functions ------------------------------------------------------- #
def add_loc_proj(i, warning=None):
    """ Compiles location and project data given an index for the tbl_project
    DataFrame
    """
    # -- Adding Location Data ----------------------------------------------- #
    state_code = tbl_project['txt_StateCode'][i]
    state_name = lkp_stateandfhwadistrict.loc[
        lkp_stateandfhwadistrict['txt_StateCode'] == state_code,
        'txt_StateName'].values[0] if not pd.isna(state_code) else None
    country_code = tbl_project['txt_CountryCode'][i]
    country_name = tbl_country.loc[
        tbl_country['txt_CountryCode'] == country_code,
        'txt_CountryDescription'].values[0]
    loc = Locations(
        address=tbl_project['txt_Address'][i]
        if not pd.isna(tbl_project['txt_Address'][i]) else None,
        city=tbl_project['txt_City'][i]
        if not pd.isna(tbl_project['txt_City'][i]) else None,
        county=tbl_project['txt_County'][i]
        if not pd.isna(tbl_project['txt_County'][i]) else None,
        state=state_name,
        country=country_name,
        latitude=tbl_project['dbl_Latitude'][i]
        if abs(tbl_project['dbl_Latitude'][i]) < 100 else None,
        longitude=tbl_project['dbl_Longitude'][i]
        if abs(tbl_project['dbl_Longitude'][i]) < 100 else None,
    )
    db.session.add(loc)

    # -- Adding Project Data ------------------------------------------------ #
    prj = Projects(
        location=loc,
        user_id=data_owner().id,
        source_db='FHWA DFLTD v.2',
        source_id=int(tbl_project['lng_KeyProject'][i]),
        description=tbl_project['mem_Remarks'][i]
        if not pd.isna(tbl_project['mem_Remarks'][i]) else None,
        site_name=tbl_project['txt_ProjectName'][i]
        if not pd.isna(tbl_project['txt_ProjectName'][i]) else None,
        source_ref=tbl_project['txt_Publication'][i]
        if not pd.isna(tbl_project['txt_Publication'][i]) else None,
        contractor=tbl_project['txt_GeneralContractor'][i]
        if not pd.isna(tbl_project['txt_GeneralContractor'][i]) else None,
        number=tbl_project['txt_ProjectID'][i]
        if not pd.isna(tbl_project['txt_ProjectID'][i]) else None,
        title=tbl_project['txt_Title'][i]
        if not pd.isna(tbl_project['txt_Title'][i]) else None,
        date_added=pd.to_datetime(
            tbl_project['dte_AddDate'][i] if not
            pd.isna(tbl_project['dte_AddDate'][i]) else None),
        warning=warning
    )

    return prj


def pile_dims(ptype, prj_id, pile_id):
    """ Fetches relevant pile data from the "Description" tables for each
    pile type
    """
    diameter = None
    wall_thickness = None
    modulus = None
    weight_ft = None
    cross_area = None
    shape = None
    square_circ = None
    circumference = None
    conc_filled = None
    if ptype in ('CC', 'RC'):
        d_series = tbl_descconccylinder[
            (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
            (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_OuterDiameter']
        if not d_series.empty:
            diameter = d_series.values[0] * 0.0393701
        t_series = tbl_descconccylinder[
            (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
            (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_WallThickness']
        if not t_series.empty:
            wall_thickness = t_series.values[0] * 0.0393701
        m_series = tbl_descconccylinder[
            (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
            (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_CompositeModulus']
        if not m_series.empty and not pd.isna(m_series.values[0]):
            modulus = m_series.values[0] * 1.4503773773e-07
        w_series = tbl_descconccylinder[
            (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
            (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_WeightPerUnitLength']
        if not w_series.empty and not pd.isna(w_series.values[0]):
            weight_ft = w_series.values[0] * 0.67
    elif ptype in ('MI', 'BC', 'FC', 'SP', 'AC'):
        if prj_id != 707:
            d_series = tbl_descdrilledshaft[
                (tbl_descdrilledshaft['lng_KeyProject'] == prj_id) &
                (tbl_descdrilledshaft['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_DiameterMain']
            if not d_series.empty:
                diameter = d_series.values[0] * 0.0393701
            m_series = tbl_descdrilledshaft[
                (tbl_descdrilledshaft['lng_KeyProject'] == prj_id) &
                (tbl_descdrilledshaft['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_ConcreteModulus']
            if not m_series.empty and not pd.isna(m_series.values[0]):
                modulus = m_series.values[0] * 1.4503773773e-07
            a_series = tbl_descdrilledshaft[
                (tbl_descdrilledshaft['lng_KeyProject'] == prj_id) &
                (tbl_descdrilledshaft['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_CrossSectionArea']
            if not a_series.empty:
                cross_area = a_series.values[0] * 1.5500031000062e-03
        else:
            d_series = tbl_descaugercast[
                (tbl_descaugercast['lng_KeyProject'] == prj_id) &
                (tbl_descaugercast['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_Diameter']
            if not d_series.empty:
                diameter = d_series.values[0] * 0.0393701
    elif ptype == 'SH':
        d_series = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_FlangeWidth']
        if not d_series.empty:
            diameter = d_series.values[0] * 0.0393701
        w_series = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_WeightPerUnitLength']
        if not w_series.empty and not pd.isna(w_series.values[0]):
            weight_ft = w_series.values[0] * 0.67
        m_series = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_SteelModulus']
        if not m_series.empty and not pd.isna(m_series.values[0]):
            modulus = m_series.values[0] * 1.4503773773e-07
        sh_series = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['txt_HpileCode']
        if not sh_series.empty:
            shape = sh_series.values[0]
        a_series = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_CrossSectionArea']
        if not a_series.empty:
            cross_area = a_series.values[0] * 1.5500031000062e-03
        depth = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_DepthSection']
        if not depth.empty:
            square_circ = (2 * diameter + 2 * depth.values[0] * 0.0393701) / 12
        circ = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_CoatingArea']
        if not circ.empty and not pd.isna(circ.values[0]):
            circumference = circ.values[0] * 0.00328084
        t_series = tbl_deschpile[
            (tbl_deschpile['lng_KeyProject'] == prj_id) &
            (tbl_deschpile['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_WebThickness']
        if not t_series.empty:
            wall_thickness = t_series.values[0] * 0.0393701
    elif ptype == 'M':
        d_series = tbl_descmonotube[
            (tbl_descmonotube['lng_KeyProject'] == prj_id) &
            (tbl_descmonotube['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_TopDiameter']
        if not d_series.empty:
            diameter = d_series.values[0] * 0.0393701
        t_series = tbl_descmonotube[
            (tbl_descmonotube['lng_KeyProject'] == prj_id) &
            (tbl_descmonotube['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_Gauge']
        if not t_series.empty:
            wall_thickness = t_series.values[0] * 0.0393701
    elif ptype in ('OC', 'SC'):
        if prj_id == 460 and pile_id == 1:
            d_series = tbl_descconccylinder[
                (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
                (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_OuterDiameter']
            if not d_series.empty:
                diameter = d_series.values[0] * 0.0393701
            m_series = tbl_descconccylinder[
                (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
                (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_CompositeModulus']
            if not m_series.empty and not pd.isna(m_series.values[0]):
                modulus = m_series.values[0] * 1.4503773773e-07
            w_series = tbl_descconccylinder[
                (tbl_descconccylinder['lng_KeyProject'] == prj_id) &
                (tbl_descconccylinder['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_WeightPerUnitLength']
            if not w_series.empty and not pd.isna(w_series.values[0]):
                weight_ft = w_series.values[0] * 0.67
        else:
            if ptype == 'SC':
                d_series = tbl_descpolyconc[
                    (tbl_descpolyconc['lng_KeyProject'] == prj_id) &
                    (tbl_descpolyconc['lng_KeyDeepFoundation'] == pile_id)
                    ]['dbl_SideLength']
                if not d_series.empty:
                    diameter = d_series.values[0] * 0.0393701
            else:
                d_series = tbl_descpolyconc[
                    (tbl_descpolyconc['lng_KeyProject'] == prj_id) &
                    (tbl_descpolyconc['lng_KeyDeepFoundation'] == pile_id)
                    ]['dbl_EquivalentDiameter']
                if not d_series.empty:
                    diameter = d_series.values[0] * 0.0393701
            circ = tbl_descpolyconc[
                (tbl_descpolyconc['lng_KeyProject'] == prj_id) &
                (tbl_descpolyconc['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_Perimeter']
            if not circ.empty and not pd.isna(circ.values[0]):
                circumference = circ.values[0] * 0.00328084
            a_series = tbl_descpolyconc[
                (tbl_descpolyconc['lng_KeyProject'] == prj_id) &
                (tbl_descpolyconc['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_CrossSectionArea']
            if not a_series.empty:
                cross_area = a_series.values[0] * 1.5500031000062e-03
            m_series = tbl_descpolyconc[
                (tbl_descpolyconc['lng_KeyProject'] == prj_id) &
                (tbl_descpolyconc['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_ConcreteModulus']
            if not m_series.empty and not pd.isna(m_series.values[0]):
                modulus = m_series.values[0] * 1.4503773773e-07
    elif ptype in ('SPO', 'SPC'):
        t_series = tbl_descsteelpipe[
            (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
            (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_WallThickness']
        if not t_series.empty:
            wall_thickness = t_series.values[0] * 0.0393701
        d_series = tbl_descsteelpipe[
            (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
            (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_OuterDiameter']
        if not d_series.empty:
            diameter = d_series.values[0] * 0.0393701
        a_series = tbl_descsteelpipe[
            (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
            (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_CrossSectionArea']
        if not a_series.empty:
            cross_area = a_series.values[0] * 1.5500031000062e-03
        w_series = tbl_descsteelpipe[
            (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
            (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_WeightPerUnitLength']
        if not w_series.empty and not pd.isna(w_series.values[0]):
            weight_ft = w_series.values[0] * 0.67
        if prj_id < 1000 or prj_id == 1050:
            m_series = tbl_descsteelpipe[
                (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
                (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_CompositeModulus']
            if not m_series.empty and not pd.isna(m_series.values[0]):
                modulus = m_series.values[0] * 1.4503773773e-07
        else:
            m_series = tbl_descsteelpipe[
                (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
                (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
                ]['dbl_SteelModulus']
            if not m_series.empty and not pd.isna(m_series.values[0]):
                modulus = m_series.values[0] * 1.4503773773e-07
        conc_filled_series = tbl_descsteelpipe[
            (tbl_descsteelpipe['lng_KeyProject'] == prj_id) &
            (tbl_descsteelpipe['lng_KeyDeepFoundation'] == pile_id)
            ]['txt_ConcreteFilledYN']
        if not conc_filled_series.empty and conc_filled_series.values[0] == 'Y':
            conc_filled = True
    elif ptype == 'ST':
        d_series = tbl_descsteptaper[
            (tbl_descsteptaper['lng_KeyProject'] == prj_id) &
            (tbl_descsteptaper['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_Diameter']
        if not d_series.empty:
            diameter = d_series.values[0] * 0.0393701
        conc_filled_series = tbl_descsteptaper[
            (tbl_descsteptaper['lng_KeyProject'] == prj_id) &
            (tbl_descsteptaper['lng_KeyDeepFoundation'] == pile_id)
            ]['txt_ConcreteFilledYN']
        if not conc_filled_series.empty and conc_filled_series.values[0] == 'Y':
            conc_filled = True
        a_series = tbl_descsteptaper[
            (tbl_descsteptaper['lng_KeyProject'] == prj_id) &
            (tbl_descsteptaper['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_CrossSectionArea']
        if not a_series.empty:
            cross_area = a_series.values[0] * 1.5500031000062e-03
        m_series = tbl_descsteptaper[
            (tbl_descsteptaper['lng_KeyProject'] == prj_id) &
            (tbl_descsteptaper['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_Modulus']
        if not m_series.empty and not pd.isna(m_series.values[0]):
            modulus = m_series.values[0] * 1.4503773773e-07
    elif ptype == 'T':
        d_series = tbl_desctimber[
            (tbl_desctimber['lng_KeyProject'] == prj_id) &
            (tbl_desctimber['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_TopDiameter']
        if not d_series.empty:
            diameter = d_series.values[0] * 0.0393701
        m_series = tbl_desctimber[
            (tbl_desctimber['lng_KeyProject'] == prj_id) &
            (tbl_desctimber['lng_KeyDeepFoundation'] == pile_id)
            ]['dbl_Modulus']
        if not m_series.empty and not pd.isna(m_series.values[0]):
            modulus = m_series.values[0] * 1.4503773773e-07

    return {'diameter': diameter, 'wall_thickness': wall_thickness,
            'modulus': modulus, 'weight_ft': weight_ft,
            'cross_area': cross_area, 'shape': shape,
            'square_circ': square_circ, 'circumference': circumference,
            'conc_filled': conc_filled}


def add_pile_data(i_pile, prj_id, pile_id, prj):
    """ Compiles pile data given an index for the tbl_deepfoundation
    DataFrame
    """

    org_ptype = tbl_deepfoundation['txt_PileType'][i_pile]
    ptype = pile_types[
        tbl_deepfoundation['txt_PileType'][i_pile]]['type']
    pshape = pile_types[
        tbl_deepfoundation['txt_PileType'][i_pile]]['shape']
    pshape = pshape if ptype != 'HPIL' else pile_dims(
        org_ptype, prj_id, pile_id)['shape']
    plength = tbl_deepfoundation[
                  'dbl_TotalLength'][i_pile] * 0.00328084
    str_num = tbl_deepfoundation['txt_StructureNumber'][i_pile]
    str_num = str_num + '; ' if not pd.isna(str_num) else ''
    pier_num = tbl_deepfoundation['txt_PierGroupNumber'][i_pile]
    pier_num = pier_num if not pd.isna(pier_num) else ''
    conc_filled = pile_dims(org_ptype, prj_id, pile_id)['conc_filled']
    conc_filled = '(CONCRETE FILLED) ' if conc_filled else ''
    pile_remarks = conc_filled + str_num + pier_num
    pile_remarks = None if pile_remarks == '' else pile_remarks
    pmodulus = pile_dims(org_ptype, prj_id, pile_id)['modulus']
    weight_ft = pile_dims(org_ptype, prj_id, pile_id)['weight_ft']

    pile = Piles(
        project=prj,
        type=ptype,
        shape=pshape,
        length=round(plength, 1) if not pd.isna(plength) else None,
        emb_length=round(tbl_deepfoundation[
                       'dbl_EmbeddedLength'][i_pile] * 0.00328084, 1)
        if not pd.isna(tbl_deepfoundation['dbl_EmbeddedLength'][i_pile])
        else None,
        remarks=pile_remarks,
        name=tbl_deepfoundation['txt_PileDesignation'][i_pile],
        tapered=True if tbl_deepfoundation[
                            'txt_GeometryCode'][i_pile] == 'V' else None,
        vibro=True if tbl_deepfoundation[
                          'txt_ConstructionMethodCode'][i_pile] in ('VDID', 'VD')
        else None,
        jetted=True if tbl_deepfoundation[
                           'txt_ConstructionMethodCode'][i_pile] == 'JETID'
        else None,
        toe_elevation=tbl_deepfoundation[
                          'dbl_TipElevation'][i_pile] * 0.00328084
        if not pd.isna(tbl_deepfoundation[
                          'dbl_TipElevation'][i_pile]) else None,
        head_elevation=tbl_deepfoundation[
                           'dbl_TopElevation'][i_pile] * 0.00328084
        if not pd.isna(tbl_deepfoundation[
                           'dbl_TopElevation'][i_pile]) else None,
        diameter=round(pile_dims(org_ptype, prj_id, pile_id)['diameter'], 1)
        if not pd.isna(pile_dims(org_ptype, prj_id, pile_id)['diameter'])
        else None,
        wall_thickness=pile_dims(
            org_ptype, prj_id, pile_id)['wall_thickness']
        if not pd.isna(pile_dims(
            org_ptype, prj_id, pile_id)['wall_thickness']) else None,
        modulus=int(pmodulus) if pmodulus else None,
        weight=int(weight_ft * plength) if weight_ft else None,
        cross_area=round(pile_dims(
            org_ptype, prj_id, pile_id)['cross_area'], 1) if not pd.isna(
            pile_dims(org_ptype, prj_id, pile_id)['cross_area']) else None,
        square_circ=pile_dims(
            org_ptype, prj_id, pile_id)['square_circ']
        if not pd.isna(pile_dims(
            org_ptype, prj_id, pile_id)['square_circ']) else None,
        circumference=pile_dims(
            org_ptype, prj_id, pile_id)['circumference']
        if not pd.isna(pile_dims(
            org_ptype, prj_id, pile_id)['circumference']) else None,
    )

    return pile


def add_load_test_data(i_lt, pile):
    """ Compiles load_test data given an index for the tbl_LoadTest DataFrame
    """
    lt_test_code = tbl_loadtest['txt_LoadTestCode'][i_lt]
    lt_dir_code = tbl_loadtest['txt_LoadTypeCode'][i_lt]
    lt_dir_code = lt_dir_code if not pd.isna(lt_dir_code) else ''
    lt_contractor = tbl_loadtest['txt_LoadTestSubcontractor'][i_lt]
    lt_contractor = lt_contractor if not pd.isna(lt_contractor) else None
    astm_lt_type = tbl_loadtest['txt_ASTMProcedureCode'][i_lt]
    load_test = LoadTests(
        pile=pile,
        direction=lt_dir[lt_test_code + lt_dir_code],
        date_tested=pd.to_datetime(
            tbl_loadtest['dte_TestDate'][i_lt] if not
            pd.isna(tbl_loadtest['dte_TestDate'][i_lt]) else None),
        setup_time=tbl_loadtest['dbl_SetupDays'][i_lt]
        if not pd.isna(tbl_loadtest['dbl_SetupDays'][i_lt]) else None,
        tested_by=lt_contractor if lt_contractor != 'Unknown' else None,
        static_type=test_type[astm_lt_type] if not
        pd.isna(astm_lt_type) else None
    )

    return load_test


def add_static_test_data(prj_id, pile_id, test_id, load_test):
    """ Compiles load_test data given an index for the tbl_LoadTestStatic
    DataFrame
    """
    slt_points = tbl_statictest[
        (tbl_statictest.lng_KeyProject == prj_id) &
        (tbl_statictest.lng_KeyDeepFoundation == pile_id) &
        (tbl_statictest.lng_KeyLoadTest == test_id)]
    for p in slt_points.index:
        index = int(slt_points['lng_KeyLoadStep'][p])
        q_generic = slt_points['dbl_TotalAppliedLoadGeneric'][p]
        q_cell = slt_points['dbl_TotalAppliedLoadCell'][p]
        q_jack = slt_points['dbl_TotalAppliedLoadJack'][p]
        q_strain = slt_points['dbl_TotalAppliedLoadStrainGage'][p]
        if not pd.isna(q_generic):
            q = q_generic * 2.24808943e-04
            load_type = 'Generic'
        elif not pd.isna(q_cell):
            q = q_cell * 2.24808943e-04
            load_type = 'Load Cell'
        elif not pd.isna(q_jack):
            q = q_jack * 2.24808943e-04
            load_type = 'Hydraulic Jack'
        elif not pd.isna(q_strain):
            q = q_strain * 2.24808943e-04
            load_type = 'Strain Gage'
        else:
            q = None
            load_type = None
        s_generic = slt_points['dbl_DisplGeneric'][p]
        s_head = slt_points['dbl_DisplPileHeadSurvey'][p]
        s_dial = slt_points['dbl_DisplDialGage'][p]
        s_level = slt_points['dbl_DisplLiquidLevelGage'][p]
        if not pd.isna(s_generic):
            s = s_generic * -0.0393701
            displ_type = 'Generic'
        elif not pd.isna(s_head):
            s = s_head * -0.0393701
            displ_type = 'Pile Head Survey'
        elif not pd.isna(s_dial):
            s = s_dial * -0.0393701
            displ_type = 'Dial Gage'
        elif not pd.isna(s_level):
            s = s_level * -0.0393701
            displ_type = 'Liquid Level Gage'
        else:
            s = None
            displ_type = None
        slt_point = StaticTests(
            load_test=load_test,
            index=index,
            load=q,
            load_type=load_type,
            displacement=s,
            displ_type=displ_type
        )
        db.session.add(slt_point)


def add_interp_data(prj_id, pile_id, test_id, load_test):
    """ Compiles interpreted capacity data given an index for the
    tbl_LoadTestNominalResistance DataFrame
    """
    interp_capacities = tbl_interp[
        (tbl_interp.lng_KeyProject == prj_id) &
        (tbl_interp.lng_KeyDeepFoundation == pile_id) &
        (tbl_interp.lng_KeyLoadTest == test_id)]
    for c in interp_capacities.index:
        interp_code = interp_capacities[
            'txt_KeyFailureCriteriaCode'][c]
        interp_method = interp_type[interp_code] if not \
            pd.isna(interp_code) else 'Unknown/Not Specified'
        interp_load = interp_capacities[
                          'dbl_FailureLoad'][c] * 2.24808943e-04
        interp_disp = interp_capacities[
                          'dbl_Displacement'][c] * 0.0393701
        interp_capacity = InterpCapacities(
            load_test=load_test,
            load=interp_load,
            displacement=interp_disp,
            type=interp_method,
            origin='source DB'
        )
        db.session.add(interp_capacity)


def add_expl_data(i_exp, expl_id, prj):
    """ Compiles boring data from the tbl_Exploration DataFrame
    """
    exp_remarks = tbl_exploration['mem_Remarks'][i_exp] \
        if not pd.isna(tbl_exploration['mem_Remarks'][i_exp]) \
        else None
    exp_ewt = tbl_exploration['dbl_DepthToWaterStatic'][i_exp] * 0.00328084 \
        if not pd.isna(
        tbl_exploration['dbl_DepthToWaterStatic'][i_exp]) else None
    exp_predom = tbl_exploration[
        'txt_USCSCodePredominant'][i_exp] if not pd.isna(
        tbl_exploration['txt_USCSCodePredominant'][i_exp]) else 'NA'
    exp_predom = uscs_predom[exp_predom]
    exp_type = tbl_exploration['txt_KeyExplorationType'][i_exp]
    exp_elev = tbl_exploration['dbl_GroundElevation'][i_exp] * 0.00328084 \
        if not pd.isna(
        tbl_exploration['dbl_GroundElevation'][i_exp]) else None
    exploration = Borings(
        name=expl_id,
        project=prj,
        remarks=exp_remarks,
        ewt=exp_ewt,
        predom_soil=exp_predom,
        type=exp_type,
        elevation=exp_elev)

    return exploration


def add_layer_data(prj_id, expl_id, exploration):
    """ Compiles layer data from the tbl_ExplorationSoilLayerBoring DataFrame
    """
    layers = tbl_explsoilboring[
        (tbl_explsoilboring.lng_KeyProject == prj_id) &
        (tbl_explsoilboring.txt_KeyExplorationName == expl_id)]

    # add new column with layer numbers
    layers['layer'] = [i for i in range(1, len(layers.index) + 1)]

    # get SPT data
    spt_data = tbl_explboring[
        (tbl_explboring.lng_KeyProject == prj_id) &
        (tbl_explboring.txt_KeyExplorationName == expl_id)]

    if not spt_data.empty and not layers.empty:
        spt_depths = spt_data.dbl_KeyDepth
        layer_i = []
        max_d = layers['dbl_KeyDepthToBottom'].values[-1]
        for d in spt_depths:
            if d <= max_d:
                layr = layers[
                    layers.dbl_KeyDepthToBottom >= d]['layer'].values[0]
            else:
                layr = None
            layer_i.append(layr)
        spt_data['layer'] = layer_i
        avg_spt = spt_data[
            ['layer', 'dbl_FieldBlowCount']].groupby('layer').agg('mean')
    else:
        avg_spt = pd.DataFrame()

    # get lab data
    lab_data = tbl_expllab[
        (tbl_expllab.lng_KeyProject == prj_id) &
        (tbl_expllab.txt_KeyExplorationName == expl_id)]

    if not lab_data.empty and not layers.empty:
        lab_depths = lab_data.dbl_KeyDepth
        layer_i = []
        max_d = layers['dbl_KeyDepthToBottom'].values[-1]
        for d in lab_depths:
            if d <= max_d:
                layr = layers[
                    layers.dbl_KeyDepthToBottom >= d]['layer'].values[0]
            else:
                layr = None
            layer_i.append(layr)
        lab_data['layer'] = layer_i
        avg_lab = lab_data[
            ['layer', 'dbl_MoistureContent', 'dbl_TotalUnitWeight',
             'dbl_LiquidLimit', 'dbl_PlasticityIndex', 'dbl_Cohesion']
        ].groupby('layer').agg('mean')
    else:
        avg_lab = pd.DataFrame()

    for i in layers.index:
        index = int(layers.layer[i])
        if index == 1:
            height = tbl_explsoilboring['dbl_KeyDepthToBottom'][i] * 0.00328084
        else:
            height = (tbl_explsoilboring['dbl_KeyDepthToBottom'][i]
                      - tbl_explsoilboring['dbl_KeyDepthToBottom'][i-1]) \
                     * 0.00328084
        soil_type = tbl_explsoilboring['txt_PrimarySoilDescriptionCode'][i] \
            if not pd.isna(
            tbl_explsoilboring['txt_PrimarySoilDescriptionCode'][i]) else None
        soil_type = primary_explsoil[soil_type] if soil_type else None
        uscs_type = tbl_explsoilboring['txt_USCSCode'][i] if not \
            pd.isna(tbl_explsoilboring['txt_USCSCode'][i]) else None
        if not soil_type and uscs_type:
            soil_type = uscs_type
        description = tbl_explsoilboring['txt_LayerDescription'][i] \
            if not pd.isna(tbl_explsoilboring['txt_LayerDescription'][i]) \
            else None
        nval = tbl_explsoilboring['dbl_BlowCountInterpreted'][i] \
            if not pd.isna(tbl_explsoilboring['dbl_BlowCountInterpreted'][i]) \
            else None
        nval_from_avg_spt = avg_spt[avg_spt.index == index]
        if not nval and not nval_from_avg_spt.empty:
            nval = nval_from_avg_spt.values[0][0] if not pd.isna(
                nval_from_avg_spt.values[0][0]) else None
        angle = tbl_explsoilboring['dbl_FrictionAngleInterpreted'][i] \
            if not pd.isna(
            tbl_explsoilboring['dbl_FrictionAngleInterpreted'][i]) else None
        data_from_avg_lab = avg_lab[avg_lab.index == index]
        cohesion = tbl_explsoilboring['dbl_CohesionInterpreted'][i] \
            * 2.0885434273e-05 if not pd.isna(
            tbl_explsoilboring['dbl_CohesionInterpreted'][i]) else None
        if not cohesion and not data_from_avg_lab.empty:
            cohesion = data_from_avg_lab.values[0][4] * 2.0885434273e-05 \
                if not pd.isna(data_from_avg_lab.values[0][4]) else None
            if cohesion:
                cohesion = cohesion if cohesion < 99 else None
        tuw = tbl_explsoilboring['dbl_UnitWeightInterpreted'][i] * 0.062428 \
            if not pd.isna(tbl_explsoilboring['dbl_UnitWeightInterpreted'][i]) \
            else None
        if not tuw and not data_from_avg_lab.empty:
            tuw = data_from_avg_lab.values[0][1] * 0.062428 if not pd.isna(
                data_from_avg_lab.values[0][1]) else None
        if not data_from_avg_lab.empty and not pd.isna(
                data_from_avg_lab.values[0][0]):
            water_content = int(data_from_avg_lab.values[0][0])
        else:
            water_content = None
        if not data_from_avg_lab.empty and not pd.isna(
                data_from_avg_lab.values[0][2]):
            liquid_limit = int(data_from_avg_lab.values[0][2])
        else:
            liquid_limit = None
        if not data_from_avg_lab.empty and not pd.isna(
                data_from_avg_lab.values[0][3]):
            plasticity = int(data_from_avg_lab.values[0][3])
        else:
            plasticity = None
        layer = Layers(
            boring=exploration,
            index=index,
            soil_type=soil_type,
            height=height,
            description=description,
            nval=nval,
            ssuu=cohesion,
            friction_angle=angle,
            tuw=tuw,
            water_content=water_content,
            liquid_limit=liquid_limit,
            plasticity=plasticity
        )
        db.session.add(layer)


# -- Main Import Function --------------------------------------------------- #
def load_fhwa_records():
    """ Iterates through source files and adds the FHWA DFLTD records to the
    database
    """
    print('--- Importing FHWA DFLTD v.2 records ---')
    for i in tqdm(range(len(tbl_project))):
        prj_id = tbl_project['lng_KeyProject'][i]

        expl_in_project = tbl_exploration[
            tbl_exploration.lng_KeyProject == prj_id].index
        for i_exp in expl_in_project:
            expl_id = tbl_exploration['txt_KeyExplorationName'][i_exp]

            piles_in_project = tbl_deepfoundation[
                    tbl_deepfoundation.lng_KeyProject == prj_id].index
            for i_pile in piles_in_project:
                pile_id = tbl_deepfoundation['lng_KeyDeepFoundation'][i_pile]

                tests_for_pile = tbl_loadtest[
                    (tbl_loadtest.lng_KeyProject == prj_id) &
                    (tbl_loadtest.lng_KeyDeepFoundation == pile_id)
                ].index
                for i_lt in tests_for_pile:
                    test_id = tbl_loadtest['lng_KeyLoadTest'][i_lt]

                    # -- Adding Project Data -------------------------------- #
                    if len(piles_in_project) > 1 and len(expl_in_project) < 2:
                        wrn = 'Expanded from a project with multiple piles '\
                              'and/or retests'
                        prj = add_loc_proj(i, wrn)
                    elif len(piles_in_project) < 2 and len(expl_in_project) > 1:
                        wrn = 'Expanded from a project with multiple '\
                              'explorations'
                        prj = add_loc_proj(i, wrn)
                    elif len(piles_in_project) > 1 and len(expl_in_project) > 1:
                        wrn = 'Expanded from a project with multiple '\
                              'explorations and multiple piles/retests'
                        prj = add_loc_proj(i, wrn)
                    else:
                        prj = add_loc_proj(i)
                    db.session.add(prj)

                    # -- Adding Exploration Data ---------------------------- #
                    exploration = add_expl_data(i_exp, expl_id, prj)
                    db.session.add(exploration)

                    # -- Adding Layer Data ---------------------------------- #
                    add_layer_data(prj_id, expl_id, exploration)

                    # -- Adding Pile Data ----------------------------------- #
                    pile = add_pile_data(i_pile, prj_id, pile_id, prj)
                    db.session.add(pile)

                    # -- Adding Load Test Data ------------------------------ #
                    load_test = add_load_test_data(i_lt, pile)
                    db.session.add(load_test)

                    # -- Adding Static Test Data ---------------------------- #
                    add_static_test_data(prj_id, pile_id, test_id, load_test)

                    # -- Adding Interpreted Data ---------------------------- #
                    add_interp_data(prj_id, pile_id, test_id, load_test)

    db.session.commit()
