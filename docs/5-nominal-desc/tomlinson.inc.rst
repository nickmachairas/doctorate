
Tomlinson Method for Cohesive Soils
===================================

The FHWA Report on the Design and Construction of Driven Pile Foundations (:ref:`Hannigan et al., 2016a <Hannigan2016a>`; :ref:`Hannigan et al., 2016b <Hannigan2016b>`) recommends that for pile diameters less than 18 inches, nominal resistance be calculated using the :math:`\alpha`-method (:ref:`Tomlinson, 1980 <Tomlinson1980>`) for cohesive soils. Similar to the Nordlund method, it is the most widely used method in State DOTs for the design of all driven piles in cohesive soils, including LDOEPs (:ref:`NCHRP 2015 <NCHRP2015>`).

The :math:`\alpha`-method, is an empirical total stress calculation method that uses the undrained shear strength of soil to find ultimate pile capacity. The unit skin resistance is shown by Tomlinson to be equal to the adhesion of soil to the pile, which is given by an "alpha" (:math:`\alpha`) factor determined by soil and pile properties using original tables and the undrained shear strength, :math:`s_u`, with :math:`f_s = \alpha s_u`. Values of :math:`\alpha` are inversely proportional to the undrained shear strength of the soil and are always less than 1, due to the adhesion between the pile and soil always being less than the cohesion within the soil.

In cohesive layers, side and toe resistances calculated by the :math:`\alpha`-method are based on :eq:`ldoep_calc_eq6` & :eq:`ldoep_calc_eq7`. When dealing with mixed soil profiles, Tomlinson provides adjustment factors to account for drag-down of weaker soils into stiffer layers, a phenomenon that occurs during pile driving and reduces the side resistance. These factors were accounted for in our calculations.



.. math::
   :label: ldoep_calc_eq6

   R_s = \sum f_s A_s = \sum C_\alpha A_s = \sum \alpha \, s_u \, A_s


.. math::
   :label: ldoep_calc_eq7

   R_p = q_p A_p = N_c s_u A_p



where:

.. |C_a| replace:: :math:`C_\alpha`
.. |alpha| replace:: :math:`\alpha`
.. |s_u| replace:: :math:`s_u`
.. |N_c| replace:: :math:`N_c`

:|C_a|: adhesion
:|alpha|: adhesion factor
:|s_U|: undrained shear strength
:|A_s|: shaft surface area
:|N_c|: bearing capacity factor


.. note::

   For plugged and unplugged analyses, :eq:`ldoep_calc_eq4` through :eq:`ldoep_calc_eq7` must be adjusted according to :eq:`ldoep_calc_eq2` & :eq:`ldoep_calc_eq3`.


