
Revised Lambda
==============

The Lambda method has gone through several revisions since it was first introduced. Focht and Vijayvergiya (:ref:`1972 <Focht1972>`) proposed that side resistance be calculated using :eq:`ldoep_calc_eq12`.



.. math::
   :label: ldoep_calc_eq12

   R_s = \sum f_s A_s = \sum \lambda \, (\bar{\sigma'} + 2 \bar{s_u}) \, A_s


where:

.. |lambda| replace:: :math:`\lambda`
.. |sigma_p| replace:: :math:`\bar{\sigma'}`
.. |su_bar| replace:: :math:`\bar{s_u}`


:|lambda|: pile penetration coefficient
:|sigma_p|: average vertical effective stress between the ground surface and the pile toe
:|su_bar|: average undrained shear strength


Kraft et al. (:ref:`1981 <Kraft1981>`) revised the pile penetration coefficient, :math:`\lambda`, proposing formulas for normally consolidated soils (:eq:`ldoep_calc_eq13`) and overconsolidated soils (:eq:`ldoep_calc_eq14`). When information on consolidation was missing or was unreliable, cohesive soils were assumed to be over-consolidated if :math:`s_u/\sigma` was equal to or larger than 0.1.


.. math::
   :label: ldoep_calc_eq13

   \lambda = 0.178 - 0.016 \ln \pi_3


.. math::
   :label: ldoep_calc_eq14

   \lambda = 0.232 - 0.032 \ln \pi_3


where:

.. |pi3| replace:: :math:`\pi_3`
.. |pi3_eq| replace:: :math:`\dfrac{\pi b f_{s.max}D^2 }{AEU}`
.. |b| replace:: :math:`b`
.. |fs_max| replace:: :math:`f_{s.max}`
.. |A| replace:: :math:`A`
.. |E| replace:: :math:`E`
.. |U| replace:: :math:`U`

:|pi3|: |pi3_eq|
:|b|: pile diameter
:|fs_max|: peak unit skin friction
:|D|: embedded pile length
:|A|: cross-sectional area
:|E|: modulus of elasticity
:|U|: pile displacement needed to develop side shear (normally 0.1 inch)
