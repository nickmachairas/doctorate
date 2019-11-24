
******************
Olson APC Database
******************

.. note::

   "APC" stands for "Axial Pile Capacity". There is some confusion that Dr. Olson's database is the "API Database". That is not the case.


History
=======

Dr. Roy E. Olson (UT Austin), began development on a pile load test database in 1980, as part of a research project with the American Petroleum Institute (API). API was interested in determining how well their recommended practice design method of the time (API RP-2A, 1980) would compare with actual pile load tests. Significant contributions were made by Norm Dennis who did his Ph.D. dissertation on this project (:ref:`Dennis, 1982 <Dennis1982>`) with the final report submitted to API that year.

Work on the then "API Database" continued between 1984 and 1993 with support from small grants from API, Exxon and Aramco but primarily due to Dr. Olson's personal involvement and contributions. There were several questions, namely, on how well different methods of strength measurement compared with each other, predictions of pile settlement under axial load, capacities of steel pipe piles in sand and clay, use of the T-Z method to try to predict pile movements under cyclic axial loading. Answering these questions led to M.S. theses written by the students working on them (:ref:`Aschenbrenner, 1984 <Aschenbrenner1984>`; :ref:`Alyahyai, 1987 <Alyahyai1987>`; :ref:`Al-Shafei, 1987 <Al-Shafei1987>`; :ref:`Van Go, 1990 <Go1990>`; :ref:`Chiu, 1993 <Chiu1993>`).

In 1998, Dr. Olson started working on a major research project from the California Department of Transportation (CalTrans). The goal was to develop a new, separate database for CalTrans. It is not clear if the APC database eventually included data from CalTrans.

The original project with API was meant to focus on open-ended steel pipe piles frequently used for offshore structures. However, Dr. Olson expanded the scope to include all pile types and capacity ranges. Information on piles, subsurface conditions and load tests was collected from the literature, DOTs and the Army Corps of Engineers. However, collection was never straightforward. Several governmental agencies, consulting firms and oil companies did not cooperate.

Norm Dennis and Dr. Olson looked at data for about 7,000 load tests but could use data for only about 1,000 of them. The lost data were almost always because: (1) the test was not carried even close to failure, or (2) no soil data were available. Of the 1,000 "usable" cases, there was still a lot of information that needed to be corrected. Indicative of the complexity of the problem of producing reliable data for analysis is the fact that Dr. Olson and his students went through each case four or five times and would always find errors or areas to improve. A list of issues identified by Dr. Olson is presented in :ref:`Appendix A.1 <olson_notes>`. It is surprising, on several levels, that the challenges Dr. Olson faced when developing the pile load test database almost 40 years ago, are still prevalent today.


Raw Data
========


.. literalinclude:: other/APCNew_sample.dat
   :lines: 1-40
   :linenos:
   :caption: *Olson APC Database* raw sample data (``APC.dat``)
   :name: OlsonRawSample


.. literalinclude:: other/APCNew_sample.dat
   :lines: 45-76
   :emphasize-lines: 2, 6, 9, 12, 18, 21, 31
   :linenos:
   :caption: Decoding raw data in the *Olson APC Database*
   :name: OlsonDecode


:numref:`OlsonVarsTable` (in the appendix) offers details on the variables used in the raw data file of the *Olson APC Database*. Variables are described in the order presented in :numref:`OlsonDecode`.




Load Test Data Points
---------------------

Olson's *APC Database* consisted of a large data file (:numref:`OlsonRawSample`) containing project raw data. A few load test interpretations were stored, i.e. Davisson capacity (``QMDT``), peak load (``QMP``), capacity at 0.5-inch butt settlement (``QCT``), etc. Load test data points were not stored in the data file. Instead, original figures from the source projects were used (see :numref:`olson_ltn013_qs` for LTN 13). Dr. Olson provided figures for _____ records of the total _____. It was crucial to include the load test data points in our *NYU Pile Load Test Data Warehouse*, therefore, all figures were digitized using the tool :ref:`WebPlotDigitizer <WebPlotDigitizer>`.


.. TODO: find total number of records in raw file and total number of QS figures and update text above

.. figure:: figures/olson_ltn013_qs.jpg
   :scale: 30%
   :name: olson_ltn013_qs

   Load/Settlement plot for *Olson APC Database* LTN 13


Digitizing the load test curves allowed us to algorithmically process the load test data points and produce new plots and additional capacity interpretations as shown in :numref:`olson_ltn013_qs_new`.


.. figure:: figures/olson_ltn013_qs_new.png
   :scale: 58%
   :name: olson_ltn013_qs_new

   Load/Settlement plot with capacity interpretations for *Olson APC Database* LTN 13




Database Design
===============

:numref:`OlsonVarsTable` summarizes the variables available in the *Olson Database* raw data files. The reduction of these variables to a relational schema is presented in :numref:`olson_db_schema`. It is important to note that in this iteration, normalization rules are not strictly enforced. For instance, attributes ``ssuu``, ``ssfv``, ``ssms``, ``ssqt`` are all storing information on shear strength obtained from different tests and it could be argued that they are violating the "non-repeating attribute" rule of the 1st Normal Form (1NF). However, in the context of geotechnical engineering, it is unlikely that a value for shear stregth obtained from a new lab test will needs to be stored. It is also unlikely that multiple values of shear strength from the same lab test will need to be stored for a single layer. As such, it is far more practical to keep these four attributes in the ``layers`` relation than move them in separate relations in order to be strictly compliant with the normalization process.




``ref_icapacities`` **values:**
   - Load @ 0.5 inches
   - Standard Davisson
   - Brown
   - Maximum Load
   - Maximum Displacement



.. figure:: figures/olson_db_schema.png
   :name: olson_db_schema

   Entity-Relationship Diagram of the database reduced from the *Olson Database* raw files
