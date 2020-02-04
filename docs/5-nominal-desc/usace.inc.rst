
United States Army Corps of Engineers (USACE) Method
====================================================

For side resistance in cohesionless soils, USACE specifies that skin friction increases linearly down to a critical depth, :math:`D_c`, and remains constant below that depth. The critical depth, :math:`D_c`, is a function of pile diameter, :math:`b`, such that :math:`D_c = 10b` for loose sands, :math:`D_c = 15b` for medium-dense sands and :math:`D_c = 20b` for dense sands. Side resistance can then be calculated according to Eq. 8.


.. math::
   :label: ldoep_calc_eq8

   R_s = \sum f_s A_s = \sum K \, \sigma'_v \, \tan \delta \, A_s


where:

.. |K| replace:: :math:`K`
.. |s_v| replace:: :math:`\sigma'_v`
.. |gamma_p| replace:: :math:`\gamma'`
.. |D| replace:: :math:`D`

:|K|: lateral earth pressure coefficient
:|s_v|: vertical effective overburden pressure (:math:`\sigma'_v = \gamma' D` when :math:`D<D_c` or :math:`\sigma'_v = \gamma' D_c` when :math:`D \geq D_c`)
:|delta|: angle of friction between pile and soil (from :ref:`USACE, 1991 <USACE1991>`)
:|gamma_p|: effective unit weight of soil
:|D|: depth along the pile


For toe resistance in cohesionless soils, the same critical depth relationship as for skin friction can be used. Toe resistance can then be calculated according to :eq:`ldoep_calc_eq9`.


.. math::
   :label: ldoep_calc_eq9

   R_p = q_p A_p = \sigma'_v \, N_q \, A_p


where:

:|s_v|: vertical effective overburden pressure (:math:`\sigma'_v = \gamma' D` when :math:`D<D_c` or :math:`\sigma'_v = \gamma' D_c` when :math:`D \geq D_c`)
:|N_q|: bearing capacity factor (from :ref:`Terzaghi and Peck, 1967 <Terzaghi1967>`)


For side resistance in cohesive soils, the USACE method is largely similar to the :math:`\alpha`-method in that resistance is due to the adhesion of the cohesive material to the side of the pile and is calculated according to :eq:`ldoep_calc_eq10`.


.. math::
   :label: ldoep_calc_eq10

   R_s = \sum f_s A_s = \sum c_a \, A_s = \sum \alpha \, s_u \, A_s


where:

:|C_a|: adhesion between pile and cohesive soil
:|alpha|: adhesion factor (from :ref:`USACE, 1991 <USACE1991>`)


Toe resistance in cohesive soils is calculated by USACE according to :eq:`ldoep_calc_eq11`.


.. math::
   :label: ldoep_calc_eq11

   R_p = q_p A_p = 9 \, s_u \, A_p

where:

:|s_u|: undrained shear strength at pile toe, normally the average over a depth of two pile diameters below the toe


.. note::

   For plugged and unplugged analyses, :eq:`ldoep_calc_eq8` through :eq:`ldoep_calc_eq11` must be adjusted according to :eq:`ldoep_calc_eq2` & :eq:`ldoep_calc_eq3`.


