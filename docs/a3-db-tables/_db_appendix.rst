
.. _appendix1:

##############################################
Source Database Attributes and Transformations
##############################################

This chapter offers crucial information on the ETL process of porting all data from the various sources (Olson, Iowa, FHWA, etc.) to the NYU Load Test Warehouse. All available details on all original attributes are summarized in tables along with the new names of the target attributes that each original piece of information was ported to.

Furthermore, and as a tribute to Dr. Roy Olson, parts from his personal notes are presented verbatim (as they could not be paraphrased) in an effort to preserve the insights and design decisions that went in to developing the first advanced pile load test database which led the way for the rest us.



*****************************
Olson APC Database Attributes
*****************************

.. _olson_notes:

A list of issues identified by Dr. Olson in developing the APC database:

#. *A pile capacity was reported in tons but was entered in the data base in kips but without changing the number.*
#. *A pile capacity was reported in “tonnes” with depth in meters and the capacity was interpreted as 2000-pound tons rather than the metric ton of 2205 pounds.*
#. *For steel pipe piles, sources often did not indicate whether the pile was open-ended or closed-ended.*
#. *For closed-ended pipe piles, authors often did not indicate whether the pile was full of concrete, or water, or was empty.*
#. *For closed-ended steel pipe piles, authors rarely indicated whether the base plate had the same diameter as the pile or was oversized.*
#. *For open-ended steel pipe piles, authors did not indicate whether or not a driving shoe was used.*
#. *For open-ended piles, the authors did not indicate the height of soil plug.*
#. *When data from soil borings were presented, it was often difficult to determine which boring was closest to a given pile.*
#. *In several cases, soil borings were made and the results reported. However, the pile penetrations made no sense in that the pile tip stopped in soft clay just above a good supporting layer. It was subsequently figured out that they had removed up to thirty feet of soil from the site after soil exploration but prior to pile driving.*
#. *We were non-uniform in defining what "plunging capacity" meant. Sometimes it was the peak load and other times it was the load at large settlement. They differed by up to 40% in some cases. I have decided to standardize on the peak load. We may want to add a new entry for the "ultimate" load.*
#. *In a number of cases, the authors called the foundation a "pile" but careful reading of the case history led to the conclusion that it was either a "pier" or it could have been a pier. We discarded such data.*
#. *The depth to the water table was often not provided. For sands, this was a fatal problem although sometimes we decided to estimate the location of the water table and just demote our rating of data quality. We are now trying to specify effective stresses in clays but we rarely have water tables for clays.*
#. *Sand densities were rarely specified so we have assumed values. Different people sometimes assumed substantially different values of total unit weight. We need to figure out some standard unit weight, perhaps as functions of N values and any information provided on gradation, but we have not done so yet and it will require a lot of time.*
#. *Japanese N values seem to be considerably different from ours because they have used a hammer of higher efficiency. Norm Dennis worked out a correlation but it is of highly questionable accuracy and this problem needs to be reconsidered.*
#. *We had a number of Japanese pile load tests on large diameter (usually 30") steel pipe piles in sand. Unfortunately, the text is in Japanese. We were able to guess soil profiles based on hatchings used in boring logs and we could read the Arabic numerals to get depths and N values. Subsequently, Tung was able to translate some of the data and he concluded we had made major errors. His corrected data are in other files and will be substituted for data in the database when time permits.*


|


From Dr. Olson's notes on the APC database:


   *Most of the values of total unit weight* (:math:`\gamma_t`) *are assumed. If water contents* (:math:`w`) *are shown then they were used to calculate* :math:`\gamma_t`. *I used cases in which water contents were measured to calculate total unit weights for all soils and then did a correlation of those values of* :math:`\gamma_t` *with whatever other properties were available, meaning cohesion* (:math:`s_u`) *for cohesive soils, and SPT-N values for all soils, and used these other properties to estimate* :math:`\gamma_t` *for cases in which water contents were not defined. The correlations were often bad but at least they gave a consistent basis for estimating* :math:`\gamma_t`.

   *The elevation of the water table was usually unknown for profiles of all clay. If I thought a reasonable value could be assumed, I did so and there are typically no notes indicating EWT was assumed (I added notes later when I thought of it). If EWT is to be left undefined, then EWT=+1, which is code that EWT is unknown.*

   *In all soils, I assumed the pore water pressure above the water table was zero. This value is nonsense but it is typically irrelevant in cohesionless soils (they may not even be saturated). In clays, the pore water pressure is relevant but can't be calculated so I discourage use of effective stress methods for clays.*

   *The wall thickness of steel pipe piles was often an assumed value. The wall thickness is used in calculating pile weight, W, and the pile compressibility, AEOL, but the correction for W is small so the error is even smaller, and AEOL is only used with Davisson's method, and I usually didn't use it as a failure criterion.*

   *The tip condition for steel pipe piles was often unknown. Sometimes, I could infer it from discussion in the text or from discussions with engineers who were more familiar with local practice. For closed-ended pipes, I rarely knew the diameter or thickness of the cover plate. Sometimes I could magnify a drawing to estimate whether the cover plate had a larger diameter than the pile or not but that was often not possible. I used a displacement ratio exceeding 1.00 to indicate the presence of an oversized cover plate.*

   *Originally we made data quality factors range from 0 to 5, then we discarded the 0's, and finally used only DQF=3-5. However, the DQF cannot be used except in the crudest manner. In the common case, we use N to estimate QS. If we have only N values at a clay site the case might warrant a DQF of 5, whereas if we try to use an effective stress method and we know neither EWT nor TUW (common) then the test might be a 1. As work evolved, we started using only data with DQF of 3-5 so I've altered DQFs to be at least 3 if the test was good enough to be used.*

   *Originally, working under very adverse conditions (horrible computer problems, need to generate quick results for API for a very crude analytical method, inexperience, etc.) Dave Winter generated a lot of data. Norm Dennis then came in and altered most of the data sets Dave had set up. Subsequently, other MS students Tim Aschenbrenner, Khalil Al Shafie, Kuan Chu, Magued Iskander, etc.) generated some new data.  Most of the data so generated had obvious errors due to inexperience. I went through many of the tests and modified all of them. The variable ``REOChk`` was added and made true if I had examined the data. Subsequently, I changed many tests I had done. The result is that all of the data are in question. The main problem is that source documents did not contain critical information, or we did not understand what was critical and get it recorded. In some cases, a single case was reported in several papers with different results, or we talked with someone who knew the case, e.g., Bob Semple regarding West Sole and Kontich, and we were informed that the published data contained errors, but revised data were not available.*

   *The source data forms, and format of the computer database have changed massively over the years. Originally, the entire digital database had to fit on one 360KB 5-1/4" floppy disk, the source forms were written in pencil on typed forms. As the forms evolved, we often, but not always, noted material as notes, and then later rewrote the form to include the needed information, but we never had time to go back to the source documents to extract the new data. The paper documentation now is digital and exceeds 1 GB, and this digital database exceeds 11,000 lines and occupies more than 600 KB. Because of limits on storage (PC's were limited to 640 KB in RAM), the original data were much compressed, e.g., we might have reported only a single layer of clay being penetrated by the pile whereas there were, in fact, a number of layers.*

   *The cone data are very deficient, mainly because of lack of use in the U.S. at the time of these cases.*

   *Interpretation of the output from the analytical program is difficult unless the user can memorize data for all of the tests, which seems possible only for small subsets of data. To remind users of problems, the data base can have one field of up to 30 columns, starting with an ``*`` and that field is output in the Excel output, typically warning the user of problems. In addition, lines starting with ``!`` are comment lines in the database and are not processed in the analysis. The ``*`` and ``!`` lines come after the LTN BLANK line (needed in order to use the same code with Caltrans data) and before alphanumeric data.*

   *This database has not been updated significantly since 1982 and there have been a lot of results published or provided from company files since then.*

   *The APC database has been partially converted to a format used on a different project but there are a few remnants of material that were relevant to an earlier format so do not anticipate that every item in this database has a use currently.*

   *I followed the LTN BLANK line with an ``*`` to indicate that I had checked this data base against the printed summary form.*

   *We added the field for set-up time much later. I went back to find values for tests but I'm not currently clear (March 2004) as to the code used to indicate that the value is unknown. I suspect that both 0 and -1 were used to indicate lack of information. I will gradually try to convert to -1 for unknown but I lack time to recheck all such cases so I'll put a note in the data set when I made such a change.*

   *The original N values are quite uncertain because of the lack of data on hammer efficiency and the vague statements in some papers that N was the "standard penetration resistance" but there was no indication that it was the ASTM standard. For example, I suspect that "standard" may have been a local standard, e.g., from a highway department or a consulting firm.*

   *The corrected N values here exceed the uncorrected values but I don't remember how the correction was made. I suspect I assumed a hammer efficiency less than 60%.*

   *I changed some CONC piles to RayC piles and changed some values of EVSO after looking at source data forms. Most of the piles had D=54 inches.*

   *Defined failure occurs when Davisson's criterion is satisfied, i.e., when S=+ 0.15" + 0.01Db. Generally, we used 29,000 ksi for the E of steel, 3000 ksi for unreinforced concrete, 4500 ksi for reinforced concrete, and 1700 ksi for timber. For tension tests we should ignore the tip term but it appears that in most cases we did not ignore that term.  The ultimate load is the largest load that the pile sustained in the test. For piles in sand, the ultimate load was usually just the final load because plunging failure does not occur. There are some known inconsistencies in the ways we interpreted some data. For example, for a constant rate of penetration (CRP) test in clay, I reported the peak load as both the ultimate and defined failure loads whereas some of the students appear to have used Davisson's criterion directly (it would come after "failure") and defined ultimate as the final plunging load (less than the peak). Similarly, if a pile was loaded to failure, unloaded, and reloaded to a larger load than it could sustain the first time, I used the first loading only whereas some of my students may have used the second loading. For piles with a great length above the ground surface, e.g., offshore, we assumed that reported loads were butt loads and we increased the loads by the weight of the pile above the ground surface.*




.. csv-table:: Appendix: *Olson APC Database* Variables
   :file: tables/olson_variables.csv
   :header-rows: 1
   :widths: 20, 50, 30
   :name: OlsonVarsTable



*****************************************
Iowa PILOT Database Tables and Attributes
*****************************************



.. csv-table:: Appendix: Iowa PILOT Database *Pile Load Test Records* Table Attributes
   :file: tables/iowa_attributes1.csv
   :header-rows: 1
   :widths: 20, 30, 20, 30
   :name: IowaAttrTable1

|

.. csv-table:: Appendix: Iowa PILOT Database *Average Soil Profile* Table Attributes
   :file: tables/iowa_attributes2.csv
   :header-rows: 1
   :widths: 20, 30, 20, 30
   :name: IowaAttrTable2

|

.. csv-table:: Appendix: Iowa PILOT Database *Borehole/SPT Information* Table Attributes
   :file: tables/iowa_attributes3.csv
   :header-rows: 1
   :widths: 20, 30, 20, 30
   :name: IowaAttrTable3

|

.. csv-table:: Appendix: Iowa PILOT Database *Static Load Test Results* Table Attributes
   :file: tables/iowa_attributes4.csv
   :header-rows: 1
   :widths: 20, 30, 20, 30
   :name: IowaAttrTable4



************************************
FHWA DFLTD v.2 Tables and Attributes
************************************

.. include:: fhwa_dfltd_appx.inc.rst


.. _lapltd_attributes:

****************************
LAPLTD Tables and Attributes
****************************

.. csv-table:: Appendix: LTRC LAPLTD *dtProjects* Table Attributes
   :file: tables/lapltd/dtProjects.csv
   :header-rows: 1
   :widths: 20, 40, 10, 30
   :name: lapltd_dtProjects

|

.. csv-table:: Appendix: LTRC LAPLTD *dtStaticData* Table Attributes
   :file: tables/lapltd/dtStaticData.csv
   :header-rows: 1
   :widths: 20, 40, 10, 30
   :name: lapltd_dtStaticData

|

.. csv-table:: Appendix: LTRC LAPLTD *dtTestEvents* Table Attributes
   :file: tables/lapltd/dtTestEvents.csv
   :header-rows: 1
   :widths: 20, 40, 10, 30
   :name: lapltd_dtTestEvents

|

.. csv-table:: Appendix: LTRC LAPLTD *dtTestPiles* Table Attributes
   :file: tables/lapltd/dtTestPiles.csv
   :header-rows: 1
   :widths: 20, 40, 10, 30
   :name: lapltd_dtTestPiles

|

.. csv-table:: Appendix: LTRC LAPLTD *lstPileType* Table Attributes
   :file: tables/lapltd/lstPileType.csv
   :header-rows: 1
   :widths: 20, 40, 10, 30
   :name: lapltd_lstPileType
