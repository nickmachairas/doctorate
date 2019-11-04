
*******************
Iowa PILOT Database
*******************


Original Schema
===============

The database was designed and distributed in Microsoft Access. Information in the Iowa Pilot database is organized in three tables, *Pile Load Test Records* (112 attributes), *Average Soil Profile* (eight attributes), *Borehole/SPT Information* (seven attributes), and *Static Load Test Results* (four attributes). Noticeably absent is data on soil unit weight which hinders effective stress and capacity calculations. Moreover, ground water table is recorded as an elevation without additional data on the elevation of the ground level in order to infer ground water table depth. Luckily, there is information on pile toe elevation for most records and combined with pile embedded depth, it is possible to infer water table depth for some records.


**``ref_ccapacities`` values:**
   - Iowa DOT Modified ENR
   - Iowa Theoretical End Bearing
   - Iowa Theoretical Capacity
   - Iowa Blue Book Method
   - Meyerhof
   - API 1984
   - Beta Burland 1973
   - Nordlund
   - WEAP


**``ref_icapacities`` values:**
   - Maximum Load
   - Standard Davisson


.. csv-table:: Iowa PILOT Database Attributes
   :file: tables/iowa_attributes.csv
   :header-rows: 1
   :widths: 20, 30, 20, 30
   :name: IowaAttrTable

