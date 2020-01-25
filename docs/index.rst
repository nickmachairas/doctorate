.. Prediction of the Ultimate Capacity of Driven Piles and Optimization of Design Parameters documentation master file, created by
   sphinx-quickstart on Sun Aug 25 19:39:27 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Assessment of Pile Design Methods Using Advanced Data Analytics
===============================================================

.. only:: html

   .. rubric:: PhD Dissertation by Nikolaos Machairas

   .. important::

      No license, *yet*. You may not use or reference any of the material presented herein. For all inquiries, please `contact me <mailto:machairas@nyu.edu>`_.


   For the past 30+ years, engineers and researchers have been
   independently collecting pile load tests and relevant subsurface
   data while organizing this information into structurally dissimilar
   repositories. Despite their competent efforts, the overall result was
   highly fragmented with very little benefit to the greater geotechnical
   community. Meanwhile, scientists aided by state-of-the-art data
   analytics have been transforming their respective industries,
   producing remarkable predictions and insights. The current
   unstructured and decentralized scheme of valuable pile load test data
   has provided few benefits. Instead it has been a hindrance to the
   geotechnical community at large.

   Use of load test databases for comparison between calculated and
   interpreted capacities has provided insights on the suitability of
   use of design methods under varying pile and soil conditions. Past
   studies have generally demonstrated that all methods in use for
   calculating the ultimate capacity of single piles have large
   margins of error. This dissertation verified past findings and
   expanded the evaluation for Large Diameter Open Ended Piles (LDOEP)
   discovering similarly poor performance.

   As part of this doctoral dissertation, a multi-tiered system, called
   `NYU Pile Capacity`_ was developed that allowed for the
   collaborative data storage, cleaning and analysis of data for deep
   foundations. *NYU Pile Capacity* has a relational database
   backend and a friendly HTML interface for user interactions.
   Existing load test databases have been delivered as locally installed
   software applications. *NYU Pile Capacity*, however, required
   no software installations and was served over the Internet as a web
   application. Users can log in and instantly start running custom
   aggregate analyses on the 5,000+ records that were imported
   from existing datasets or add new records.

   *NYU Pile Capacity* was built using Python Flask and
   can batch-process multiple load test records for practically
   countless combinations of soil conditions and pile types.
   Furthermore, *NYU Pile Capacity* was designed to be extended
   in order to run additional analyses with minimal updates to its core
   codebase.

   Most of the methods in current use for pile design are based on
   empirical formulas that required gross overgeneralization to develop.
   The empirical/semi-empirical design guidelines were derived from as
   few as 41 load test records. This doctoral dissertation compiled a
   dataset of more than 5,000 load test records and evaluated popular
   methods for capacity calculation and capacity interpretation
   against this massive dataset. The results of analyses revealed that
   contrary to common practice and against federal and state guidelines,
   the recommended *Nordlund* and *Tomlinson* methods
   were not producing optimal designs. Instead, the less popular
   *API* and *Lambda* methods proved far superior.
   Also, a comprehensive evaluation of interpreted capacity
   methods validated the dominance of the original *Davisson*
   method while not finding any significant benefits to the subsequent
   federally proposed modifications to this method, once again proving
   that going against Federal guidelines could produce more efficient
   designs.

   Another major finding of this dissertation is that given a large
   enough training sample, pile capacity can be reliably estimated
   by employing Machine Learning techniques. In projects that involve
   a large number of pile foundations, not all piles are individually
   designed and checked. Existing design software do not run aggregate
   analyses, and manually repeating the process hundreds of times
   would be extremely time consuming. However, working off of a reliable
   approximation of subsurface conditions for the entire site based on
   the results of site investigation, every pile on site can be designed
   or checked via batch processing and an iterative optimization process.
   A proof-of-concept of this alternative design process was presented
   where a *Support Vector Machine* algorithm outperformed the
   Federal design method for driven piles. Perhaps more remarkably, the
   predictive model outperformed the FHWA pile design method by relying
   only on seven readily available features as compared to a laborious
   and error-prone design methodology.

   Finally, this dissertation presented the argument for the
   *case-based design* of driven pile foundations. Most of the
   existing design methods attempted to generalize and provide
   recommendations for all soil conditions and all pile types. There
   was, however, little focus on the performance of these methods
   for specific soil conditions and pile types. The industry implemented
   the design methods as blanket solutions expecting that they would
   perform well for all cases. The custom tools developed in this study
   provided the flexibility to run aggregate analyses on groups of load
   test records with similar characteristics. The results of these
   analyses revealed that design methods do not perform equally well
   for all cases. Gaining insights into the cases for which design
   methods perform best can enable enhanced pile design workflows where
   instead of using a single method to calculate capacities, a
   combination of methods can be employed depending on the soil
   conditions and pile type. Hence, *case-based design* can lead
   to safer and cost-effective designs for driven pile foundations.


   .. _NYU Pile Capacity: http://pilecapacity.com

   |

   Please use the table of contents to navigate.



.. raw:: html

   </br></br><strong>Table of contents:</strong>


.. toctree::
   :numbered:
   :maxdepth: 5

   1-intro/_intro.rst
   2-database/_database.rst
   3-interpreted-desc/interpreted_desc.rst
   4-interpreted-eval/interpreted_eval.rst
   5-nominal-desc/_nominal_capacity.rst
   6-nominal-small/fhwa_paper.rst
   7-nominal-ldoep/ldoep_calc_paper.rst
   9-ifcee-analytics/ifcee_paper.rst
   10-conclusion/conclusion.rst
   references.rst




.. raw:: html

   </br></br><strong>Appendices:</strong>


.. only:: html

   .. toctree::
      :maxdepth: 5

      a1-soil-approx/soil-approx.rst
      a2-piles-notations/notations.rst
      a3-db-tables/_db_appendix.rst
