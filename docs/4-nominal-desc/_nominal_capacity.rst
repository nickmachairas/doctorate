
##########################################
Presentation of Nominal Resistance Methods
##########################################


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



.. include:: nordlund.inc.rst
.. include:: tomlinson.inc.rst
.. include:: usace.inc.rst
.. include:: lambda.inc.rst
.. include:: api.inc.rst
.. include:: olson.inc.rst

