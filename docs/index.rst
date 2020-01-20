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

   ..
      This research endeavor encompasses the following objectives, as reiterated in
      the March 5, 2019 Memorandum between the author and the PhD Guidance Committee.

      1. Evaluation of available methods for estimating the **interpreted capacity**
         of single driven piles from static load tests and address the research
         question as to which is the best method, especially for LDOEPs.
      2. Evaluation of various available methods for calculating the **nominal
         resistance** of single driven piles against the pile load tests stored in the
         Warehouse; and selection of the best performing design method as the basis
         to propose an improved design method. In particular, you should address the
         research question of whether or not existing interpreted capacity methods
         from static load tests for piles wider than 36 inches are suitable for
         LDOEPs.
      3. Address the long-standing research question of whether or not, and under
         what conditions does skin friction increase linearly with depth, using data
         in the Warehouse.
      4. Employ the warehouse to provide recommendations for revised resistance
         factors for design.
      5. Address the research question of whether or not soil plugging is affected by
         factors other than pile’s length to diameter ratio.


   ..
      Members of the Ph.D. Guidance Committee:

      - **Magued Iskander**, PhD, PE, Professor & Chair, Civil and Urban Engineering, NYU
      - **Mohsen Hossein**, PhD, PE, Industry Professor, Civil and Urban Engineering, NYU
      - **Torsten Suel**, PhD, Professor, Computer Science and Engineering, NYU
      - **Muhannad Suleiman**, PhD, Associate Professor, Civil and Environmental Engineering, Lehigh University
      - **Antonio Marinucci**, PhD, Adjunct Professor, Civil and Urban Engineering, NYU
      - **Debra Laefer**, PhD, Associate Professor, CUE & Professor of Practice, CUSP

   For the past 30+ years, engineers and researchers have been
   independently collecting pile load tests and relevant subsurface
   data while organizing this information into structurally dissimilar
   repositories. Despite their competent efforts, the overall result was
   highly fragmented with very little benefit to the greater geotechnical
   community. Meanwhile, scientists aided by state-of-the-art data
   analytics have been transforming their respective industries,
   producing remarkable predictions and insights. The unstructured and
   decentralized current scheme of this valuable pile load test data
   has provided few benefits, instead it has mostly been a hindrance to
   the geotechnical community at large.

   Use of load test databases for comparison between calculated and
   interpreted capacities can provide insights on
   suitability of use of current design methods under varying pile and
   soil conditions. Past studies have generally demonstrated that all
   methods in current use for calculating the ultimate capacity of
   single piles have large margins of error.

   As part of this doctoral dissertation, a modern system, called
   `NYU Pile Capacity`_
   was developed that allows for the collaborative data storage, cleaning
   and analysis of deep foundations. `NYU Pile Capacity`_
   has a relational database backend and a friendly HTML interface
   for user interactions. In direct contrast to the status of existing
   load test databases, `NYU Pile Capacity`_ requires no
   software installations and is served over the Internet as a web
   application. Users can log in and immediately start running
   custom aggregate analyses on the 3,000+ records that were imported
   from existing datasets or add new records (adding new records
   requires elevated user access privileges). Users can easily share
   their results and collaborate.

   `NYU Pile Capacity`_ was built using Python Flask. Choosing
   a Python-based framework was instrumental in designing a platform
   that can batch-process multiple load test records for practically
   countless combinations of soil conditions and pile types.
   Furthermore, `NYU Pile Capacity`_ can be easily extended to
   run additional analyses with minimal updates to its core
   codebase. `NYU Pile Capacity`_ was designed to serve as the
   golden standard for geotechnical and pile load test data storage and
   analysis.

   Most of the methods in current use for pile design are based on
   empirical formulas that required gross overgeneralization to develop.
   The empirical/semi-empirical design guidelines were derived from as
   few as 41 load test records. This doctoral dissertation compiled a
   dataset of more than 3,000 load test records and evaluated popular
   methods for capacity calculation and capacity interpretation
   against this massive dataset. The results of the author's analyses
   reveal that contrary to common practice by engineers and against
   federal and state guidelines, the recommended *Nordlund* and
   *Tomlinson* methods are not producing optimal designs.
   Instead, the *API* and *Lambda* methods proved far
   superior. Also, a comprehensive evaluation of interpreted capacity
   methods validated the dominance of the original *Davisson*
   method while not finding any significant benefits to the subsequent
   federally proposed modifications to this method.

   Finally, a major finding of this dissertation is that given a large
   enough training sample, pile capacity can be reliably estimated
   by Machine Learning analyses.
   In projects that involve a very large number of
   pile foundations, usually not all piles are individually designed
   and checked. That would be a tall order given the existing design
   software, manually repeating the process hundreds of times would be
   extremely time consuming. However, working off of a reliable
   approximation of subsurface conditions for the entire site based on
   the results of site investigation, every pile on site can be
   designed via batch processing and an iterative optimization process.
   A combination of cost optimization and clustering analysis, because
   while we can optimally size each pile, it would be impossible to construct.
   The clustering analysis will group pile sizes in the most
   cost-efficient way from a material and constructability perspective.


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

      a1-edafos/edafos.rst
      a2-piles-notations/notations.rst
      a3-db-tables/_db_appendix.rst
