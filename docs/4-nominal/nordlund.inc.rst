
Nordlund (cohesionless soils)
=============================

The *Nordlund* method (:ref:`Nordlund, 1963 <Nordlund1963>`), is recommended by FHWA (:ref:`Hannigan et al., 2016a <Hannigan2016a>`) for accurate determination of driven pile capacity in cohesionless soils. This method is semi-empirical and heavily reliant on determination of the soil friction angle, :math:`\phi`. Nordlund (:ref:`Nordlund, 1963 <Nordlund1963>`; :ref:`Nordlund, 1979 <Nordlund1979>`) developed his method of calculating bearing capacity of piles in cohesionless soils from as few as 41 load tests from eight different test sites. Although the method was developed for piles smaller than 18 inches in diameter, it is still the most widely used method in State DOTs for the design of all driven piles, including LDOEPs (:ref:`NCHRP 2015 <NCHRP2015>`).


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
