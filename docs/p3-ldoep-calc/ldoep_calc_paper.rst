#############################################################################
Evaluation of Pile Design Methods for Large Diameter Open-Ended Piles (LDOEP)
#############################################################################

.. rubric:: Nikolaos Machairas, Andrew Rizk and Magued G. Iskander

.. rubric:: Abstract

Large-Diameter Open-Ended Piles (LDOEP) are increasingly being used for support of infrastructure projects. Yet many of the methods in current use for calculating pile capacity are based on databases of interpreted load test data for small diameter piles. The scope of this study was limited to impact or vibratory driven un-tapered steel and concrete pipe-piles, larger than 30 inches in diameter, loaded in compression, using a static load test.

The efficacy of four commonly used pile design methods was explored using data made possible by the 2016 release of FHWA Deep Foundation Load Test Database, which was was ported to a cloud-based relational database that permitted batch processing of the available information. An analytical procedure was developed in Python in conjunction with ENSOFT’s *APILE Offshore 2019* to compute the axial capacity of piles using methods proposed by: (1) FHWA (2) The US Army Corps of Engineers, (3) American Petroleum Institute (API) as well as (4) the Lambda method. Interpreted capacity from static load test data was also obtained using the modified Davisson Criterion.

Scatter between measured (interpreted) and predicted capacities is significant, where the computed capacity was off by a factor of two in many tests. Use of a load test for determining the capacity of LDOEP is therefore strongly encouraged. Several plugging conditions were considered. All 4 methods achieved better predictions for the unplugged condition, suggesting that LDOEPs do not develop significant end bearing, possibly because the deformation required to develop end bearing are not achieved for these piles.



************
Introduction
************

Large Diameter Open-Ended Pipe Piles (LDOEPs) have enjoyed limited use for transportation infrastructure. LDOEPs are ideal for support of heavy axial loads, high lateral forces, and large bending moments. LDOEPs are widely used in the offshore industry where these concerns are paramount. In recent years LDOEPs have also enjoyed considerable use for support of wind energy turbine converters. Use of LDOEPs for support of bridge structures has been increasing, especially where liquefiable layers are encountered, or seismic concerns dominate. However, the rate of adoption has been limited by the lack of design guidance geared towards bridge structures.

LDOEPs are generally more economic than other foundation alternatives, such as drilled shafts, and large pile groups. Driving is typically more efficient than drilling. The ability to specify and inspect the piling dimensions and materials eliminates certain construction risks associated with drilled foundations. Additionally, LDOEPs offer the opportunity to replace large pile groups, thus eliminating the cost of a pile cap and reducing the need for factoring in complex axial and lateral group effects. For foundations under waterways LDOEPs can eliminate the need for costly cofferdams, which are required for drilled shafts and large pile groups. Finally, when complex rock surfaces are encountered, steel pipe piles also offer the possibility of adjusting the pile length, on site, by splicing additional sections as well as eliminating (or torching off) sections.

Single pile design is typically conducted using ultimate capacity determination from either calculated or interpreted methods (or both in combination). Determination of the ultimate capacity of driven piles using calculated methods is conducted by following a series of steps in a design process, starting with data and properties gathered from a geotechnical investigation such as those recommended by the Federal Highway Administration (FHWA) driven pile design manual (:ref:`Hannigan et al., 2016a <Hannigan2016a>`; :ref:`Hannigan et al., 2016b <Hannigan2016b>`), along with pile selection. Interpreted pile capacity calculations are derived from load-settlement curve data generated during an axial load test of a driven pile.

A recent survey of state highway departments of transportation (:ref:`NCHRP, 2015 <NCHRP2015>`) revealed  that when LDOEPs are selected for a project, they are typically designed using methods proposed by FHWA that are based on methods originally proposed by Nordlund (:ref:`1963 <Nordlund1963>`), and Tomlinson (:ref:`1980 <Tomlinson1980>`). Alternate design approaches include methods proposed by the American Petroleum Institute (API) (:ref:`API RP-2A, 1993 <API1993>`), the United States Army Corps of Engineers (:ref:`USACE, 1991 <USACE1991>`), and the Lambda Method (:ref:`Focht and Vijayvergiya, 1972 <Focht1972>`; :ref:`Kraft et al., 1981 <Kraft1981>`).

However, none of these methods was developed using LDOEPs. For example, for piles in sand, Nordlund (:ref:`1963 <Nordlund1963>`) developed his method of calculating bearing capacity of piles in cohesionless soils from as few as 41 load tests from eight different test sites having diameters ranging between 10 and 20 inches. Similarly for clays, Tomlinson (:ref:`1980 <Tomlinson1980>`) employed 56 small diameter piles to develop his popular :math:`\alpha`-design method that was based in part on data published by Peck (:ref:`1958 <Peck1958>`). These methods were adopted by the FHWA Pile Design Manual (:ref:`Hannigan et al., 2016a <Hannigan2016a>`; :ref:`Hannigan et al., 2016b <Hannigan2016b>`), and the methods of choice for many state departments of transportation (DOT).

Recently, FHWA released the Deep Foundation Load Test Database (DFLTD) v.2 (:ref:`Petek et al., 2016 <Petek2016>`). DFLTD v.2 contains a number of load tests on piles having diameters in the 8 to 118 in. range. Comparison between calculated and interpreted capacities for large data sets provides insight of suitability of use of current design methods under varying pile and soil conditions. Thus, these tests can potentially be used to assess the adequacy of current design methods for predicting the axial capacity of LDOEPs.

For this study, several programs were developed in Python, and in conjunction with ENSOFT’s *APILE Offshore 2019* (:ref:`Wang et al., 2019a <Wang2019a>`; :ref:`Wang et al., 2019b <Wang2019b>`), the ultimate pile capacities of 62 LDOEPs were calculated using four driven pile design methods. As such, data available from the DFLTD v.2 could be analyzed on a large scale to compare multiple interpreted pile capacities with their corresponding calculated capacities. The results were summarized, analyzed, plotted and used to compare the performance of calculated vs. interpreted capacity (:math:`Q_c/Q_m`) in sands, clays, and mixed soils. Additionally, the effect of pile length, pile diameter and pile type on the :math:`Q_c/Q_m` ratio was explored.

The scope was limited to impact or vibratory driven un-tapered steel and concrete pipe-piles, larger than 30 inches in diameter, loaded in compression, using a static load test. Although LDOEP are sometimes defined to include piles larger than 36 in. in diameter, in this study, LDOEP was defined to include piles larger than 30 inches in diameter for a number of reasons. First, to increase the size of available load tests for analysis by 15%. Second, because piles in the 30 to 36 inches are among the most commonly used piles sizes for support of infrastructure. Third, the design methods have been developed using piling that was largely smaller than 30 in. in diameter. Finally, the performance of standard diameter piling is provided in the paper, and it fits well with larger diameter piles.



*******************
Pile Design Methods
*******************

The ultimate bearing capacity, :math:`R_n` (aka nominal resistance), of driven piles is typically given by nominally adding the shaft and toe resistances (:eq:`ldoep_calc_eq1`).


.. math::
   :label: ldoep_calc_eq1

   R_n = R_s + R_p = \sum f_s A_s + q_p A_p


where:

.. |R_s| replace:: :math:`R_s`
.. |R_p| replace:: :math:`R_p`
.. |A_s| replace:: :math:`A_s`
.. |A_p| replace:: :math:`A_p`
.. |f_s| replace:: :math:`f_s`
.. |q_p| replace:: :math:`q_p`

:|R_s|: Shaft resistance
:|f_s|: Unit shaft resistance, adhesion
:|A_s|: Shaft surface area
:|R_p|: Toe resistance
:|q_p|: Unit toe resistance
:|A_p|: Toe cross sectional area


For open-ended piles, soil plugging must be taken into account. In the case where a pile is plugged, capacity is calculated with :eq:`ldoep_calc_eq1` using the external side resistance and the toe resistance from the full width of the toe. However, when an open-ended pile cores the soil stratum while driving, the pile is modelled as unplugged or partially plugged and :eq:`ldoep_calc_eq1` is adjusted to account for internal and external side resistance as well as toe resistance from the pile’s annulus cross-sectional area. FHWA advises, following Paikowsky and Whitman (:ref:`1990 <Paikowsky1990>`) recommendations, that static resistance of an open-ended pipe pile be calculated from the lesser of :eq:`ldoep_calc_eq2` for plugged conditions and :eq:`ldoep_calc_eq3` for unplugged conditions (:ref:`Hannigan et al., 2016a <Hannigan2016a>`).


.. math::
   :label: ldoep_calc_eq2

   R_n = \sum f_{so} A_{so} + q_{p} A_{pp}


.. math::
   :label: ldoep_calc_eq3

   R_n = \sum f_{so} A_{so} + \sum f_{si} A_{si} + q_{p} A_{p} - W_p


where:


.. |f_so| replace:: :math:`f_{so}`
.. |f_si| replace:: :math:`f_{si}`
.. |A_so| replace:: :math:`A_{so}`
.. |A_si| replace:: :math:`A_{si}`
.. |A_pp| replace:: :math:`A_{pp}`
.. |W_p| replace:: :math:`W_p`

:|f_so|: exterior unit shaft resistance
:|A_so|: exterior surface area
:|f_si|: interior unit shaft resistance
:|A_si|: interior surface area
:|A_pp|: cross sectional area of pile and soil plug at pile toe
:|W_p|: weight of soil plug


For a comprehensive comparison, this study adopted four popular pile design methods that were identified in NCHRP 478 (:ref:`2015 <NCHRP2015>`): (a) the Federal Highway Administration (FHWA) method, (b) the United States Army Corps of Engineers (USACE) method, (c) the Revised Lambda method and (d) the Revised American Petroleum Institute (API) method. Details of each design method, and the specific parameters employed are available in Reese et al. (:ref:`2006 <Reese2006>`). Several other methods are sometimes used for LDOEPs including Fugro, NGI, ICP, UWA, however all are CPT based. Although the CPT provides a superior tool for geotechnical investigations, the authors did not include CPT methods in this study, (1) in an effort to reduce the variables affecting the analysis. Also, (2) available CPT data was sufficiently complete to allow capacity calculations for only a dozen records.



Federal Highway Administration (FHWA) Method
============================================

The FHWA Report on the Design and Construction of Driven Pile Foundations (:ref:`Hannigan et al., 2016a <Hannigan2016a>`; :ref:`Hannigan et al., 2016b <Hannigan2016b>`) recommends that for pile diameters less than 18 inches, nominal resistance be calculated using the Nordlund method (:ref:`Nordlund, 1963 <Nordlund1963>`) for cohesionless soils and the :math:`\alpha`-method (:ref:`Tomlinson, 1980 <Tomlinson1980>`) for cohesive soils. Although neither method has been developed for piles larger than 18 inches in diameter, they are the most widely used methods in State DOTs for the design of all driven piles, including LDOEPs (:ref:`NCHRP 2015 <NCHRP2015>`).

For uniform (non-tapered) piles, side resistance by the Nordlund method is calculated using :eq:`ldoep_calc_eq4` and toe resistance is calculated using :eq:`ldoep_calc_eq5`. The method uses corrected SPT N-values (or, preferably, lab-produced strength parameters) to determine the soil friction angle for each soil layer and uses a series of published tables and charts to assume correlations for the coefficient of lateral earth pressure and the soil-pile friction angle. These values are used along with the effective overburden pressure, to determine the side resistance for each defined layer. Pile tip bearing capacity factors are also correlated from the soil friction angle using charts. Upper limits are placed upon skin friction and pile tip resistance, :math:`R_p`, in order to limit the magnitude of the computed unit skin and tip resistance and calculate a safer ultimate pile capacity.



.. math::
   :label: ldoep_calc_eq4

   R_s = \sum K_d \, C_F \, \sigma'_d \, \sin(\delta) \, C_d \, \Delta d


.. math::
   :label: ldoep_calc_eq5

   R_p = \alpha_t \, N'_q \, A_p \, \sigma'_p


where:


.. |K_d| replace:: :math:`K_d`
.. |C_F| replace:: :math:`C_F`
.. |s_d| replace:: :math:`\sigma'_d`
.. |delta| replace:: :math:`\delta`
.. |C_d| replace:: :math:`C_d`
.. |D_d| replace:: :math:`\Delta_d`
.. |a_t| replace:: :math:`\alpha_t`
.. |N_q| replace:: :math:`N'_q`
.. |s_p| replace:: :math:`\sigma'_p`

:|K_d|: coefficient of lateral earth pressure at depth :math:`d`
:|C_F|: correction factor for |K_d| when :math:`\delta \neq \phi`
:|s_d|: vertical effective stress at the center of depth increment :math:`d`
:|delta|: friction angle between pile and soil
:|C_d|: pile perimeter at depth :math:`d`
:|D_d|: length of pile segment
:|a_t|: dimensionless factor (dependent on pile depth width relationship)
:|N_q|: bearing capacity factor
:|s_p|: vertical effective stress at pile toe

