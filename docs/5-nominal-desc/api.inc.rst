
American Petroleum Institute (API) Method
=========================================

The API design method is widely regarded as the best method for the design of LDOEPs due to the Institute’s long history in the design of offshore platforms. It was presented in the "Recommended Practice" Report RP-2A in 1986 and was revised in 1987 and 1993. Side resistance in cohesionless soils can be calculated using :eq:`ldoep_calc_eq15`.


.. math::
   :label: ldoep_calc_eq15

   R_s = \sum f_s A_s = \sum K \, \bar{\sigma'} \, \tan \delta \, A_s


where:

:|K|: coefficient of lateral earth
:|sigma_p|: average vertical effective stress
:|delta|: angle of friction between pile and soil (:ref:`API RP-2A, 1993 <API1993>`)


:numref:`API_K_table` offers recommended values for the coefficient of lateral earth, :math:`K`.


.. table:: Values for coefficient of lateral earth, :math:`K`
   :name: API_K_table

   +------------------------------------------------+-----+
   | Condition                                      | K   |
   +================================================+=====+
   | unplugged, open-ended pipe piles (tens & comp) | 0.8 |
   +------------------------------------------------+-----+
   | full-displacement piles                        | 1.0 |
   +------------------------------------------------+-----+


:numref:`API_d_table` offers guidelines for :math:`\delta`, the friction angle between the soil and the pile wall as well as limiting unit friction, :math:`f_s`.


.. table:: API Guidelines for Side Friction in Siliceous Soil
   :name: API_d_table

   +----------------------------------------+----------------+-----------------------+
   | Soil                                   | :math:`\delta` | Limiting, :math:`f_s` |
   |                                        | , degrees      +-----------------------+
   |                                        |                | kips/ft2 | kPa        |
   +========================================+================+==========+============+
   | Very loose to medium, sand to silt     | 15             | 1.0      | 47.8       |
   +----------------------------------------+----------------+----------+------------+
   | Loose to dense, sand to silt           | 20             | 1.4      | 67.0       |
   +----------------------------------------+----------------+----------+------------+
   | Medium to dense, sand to sand-silt     | 25             | 1.7      | 81.4       |
   +----------------------------------------+----------------+----------+------------+
   | Dense to very dense, sand to sand-silt | 30             | 2.0      | 95.8       |
   +----------------------------------------+----------------+----------+------------+
   | Dense to very dense, gravel to sand    | 35             | 2.4      | 114.9      |
   +----------------------------------------+----------------+----------+------------+



Toe resistance in cohesionless soils is given by :eq:`ldoep_calc_eq16`.


.. math::
   :label: ldoep_calc_eq16

   R_p = q_p A_p = \sigma' N_q \, A_p


where:

.. |sigma_| replace:: :math:`\sigma'`

:|sigma_|: effective stress at pile toe
:|N_q|: bearing capacity factor


Neither unit shaft resistance, :math:`f_s`, nor unit toe resistance, :math:`q_p`, increase linearly without limit. API RP-2A limiting unit shaft and toe resistance values based on soil consistency, from very loose sand/silt to very dense sand/gravel.


:numref:`API_q_table` offers guidelines for :math:`N_q`, bearing capacity factor
as well as limiting, :math:`q_p`.



.. table:: API Guidelines for Toe Resistance in Siliceous Soil
   :name: API_q_table

   +----------------------------------------+-------------+--------------------------+
   | Soil                                   | :math:`N_q` | Limiting, :math:`q_p`    |
   |                                        |             +--------------------------+
   |                                        |             | kips/ft\ :sup:`2` | MPa  |
   +========================================+=============+===================+======+
   | Very loose to medium, sand to silt     | 8           | 40                | 1.9  |
   +----------------------------------------+-------------+-------------------+------+
   | Loose to dense, sand to silt           | 12          | 60                | 2.9  |
   +----------------------------------------+-------------+-------------------+------+
   | Medium to dense, sand to sand-silt     | 20          | 100               | 4.8  |
   +----------------------------------------+-------------+-------------------+------+
   | Dense to very dense, sand to sand-silt | 40          | 200               | 9.6  |
   +----------------------------------------+-------------+-------------------+------+
   | Dense to very dense, gravel to sand    | 50          | 250               | 12.0 |
   +----------------------------------------+-------------+-------------------+------+


The general equation for shaft resistance in cohesive soils according to the revised API method is presented in :eq:`ldoep_calc_eq17`.


.. math::
   :label: ldoep_calc_eq17

   R_s = \sum f_s A_s = \sum \alpha s_u \, A_s

.. math::
   :label: ldoep_calc_eq18

   \alpha =
    \begin{cases}
     0.5\psi^{-0.5} & \textrm{if} \quad \psi \leq 1.0 \\
     0.5\psi^{-0.25} & \textrm{if} \quad \psi > 1.0
    \end{cases} \quad \leq 1.0

where:

.. |psi| replace:: :math:`\psi`

:|alpha|: adhesion coefficient governed by :eq:`ldoep_calc_eq18` where :math:`\psi = s_u/\bar{\sigma'}`
:|sigma_p|: average vertical effective stress


Finally, toe resistance in cohesive soils is given by :eq:`ldoep_calc_eq19`, the same way as for the USACE method.


.. math::
   :label: ldoep_calc_eq19

   R_p = q_p A_p = 9 \, s_u \, A_p

.. important::

   - Toe resistance must always be checked against :math:`R_p = q_p A_{pp}` where :math:`A_{pp}` is the cross sectional area of soil plug in open end pipe or H-piles at pile toe.
   - Undrained shear strength at the toe of the pile, :math:`s_u`, is usually taken as the **average over a distance of two diameters** below the tip of the pile.


.. note::

   For plugged and unplugged analyses, :eq:`ldoep_calc_eq15` through :eq:`ldoep_calc_eq19` must be adjusted according to :eq:`ldoep_calc_eq2` & :eq:`ldoep_calc_eq3`.




In order to interpret :numref:`API_d_table` and :numref:`API_q_table` algorithmically, the correlation in :numref:`API_SPT_corr_table` was employed in batch calculations.



.. table:: SPT-N corrected Correlations
   :name: API_SPT_corr_table

   +--------------+-----------------------+--------------------+
   | Density      | :math:`N_{cor}` (bpf) | :math:`\phi` (deg) |
   +==============+=======================+====================+
   | Very loose   | 0 - 4                 | < 28               |
   +--------------+-----------------------+--------------------+
   | Loose        | 5 - 10                | 28 - 30            |
   +--------------+-----------------------+--------------------+
   | Medium dense | 11 - 30               | 30 - 36            |
   +--------------+-----------------------+--------------------+
   | Dense        | 31 - 50               | 36 - 41            |
   +--------------+-----------------------+--------------------+
   | Very Dense   | over 50               | > 41               |
   +--------------+-----------------------+--------------------+


In which case :numref:`API_d_table`, :numref:`API_q_table` and :numref:`API_SPT_corr_table` can be consolidated as in :numref:`API_d_q_SPT_table`.


.. table:: API Guidelines for Shaft and Toe Resistance in Siliceous Soil with SPT-N values
   :name: API_d_q_SPT_table

   +----------------------------------------+-----------------------+----------------------+-------------------------+-------------+-------------------------+
   | Soil                                   | :math:`N_{cor}` (bpf) | :math:`\delta` (deg) | :math:`f_{s.lim}` (ksf) | :math:`N_q` | :math:`q_{p.lim}` (ksf) |
   +========================================+=======================+======================+=========================+=============+=========================+
   | Very loose to medium, sand to silt     | 0 - 4                 | 15                   | 1.0                     | 8           | 40                      |
   +----------------------------------------+-----------------------+----------------------+-------------------------+-------------+-------------------------+
   | Loose to dense, sand to silt           | 5 - 10                | 20                   | 1.4                     | 12          | 60                      |
   +----------------------------------------+-----------------------+----------------------+-------------------------+-------------+-------------------------+
   | Medium to dense, sand to sand-silt     | 11 - 30               | 25                   | 1.7                     | 20          | 100                     |
   +----------------------------------------+-----------------------+----------------------+-------------------------+-------------+-------------------------+
   | Dense to very dense, sand to sand-silt | 31 - 50               | 30                   | 2.0                     | 40          | 200                     |
   +----------------------------------------+-----------------------+----------------------+-------------------------+-------------+-------------------------+
   | Dense to very dense, gravel to sand    | over 50               | 35                   | 2.4                     | 50          | 250                     |
   +----------------------------------------+-----------------------+----------------------+-------------------------+-------------+-------------------------+


