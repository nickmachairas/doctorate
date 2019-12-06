
############
Introduction
############


**********
Background
**********

This research endeavor was inspired by a large part from the vast experience that the author's advisor, Dr. Magued Iskander and his advisor, Prof. Roy Olson, have on the broader field of deep foundations. However the work that had been done in the past (that is, 15 - 20 years ago) was based on technologies and methodologies that did provide many valuable insights but left some questions unanswered, particularly about the design and performance of Large Diameter Open Ended Piles (LDOEPs).

Capacity calculations for driven piles can be particularly tedious and error prone when performed manually while commercial design software applications do not offer the flexibility to run multiple analyses on a large number of piles. Data analysis is, of course, an indispensable part of most research projects, although in this case it became quickly obvious that no existing tool would be able to help in producing meaningful and reliable results. The best solution would be to develop new tools and design new databases and software.

The data required for this study included site investigation reports, soil lab test results and pile load test results. Publicly available records were scarce and often unreliable. They came mostly from State Departments of Transportation or published research. The Geoprofession at-large is infamous for its poor state of handling data which made the necessary process of data collection and analysis the most difficult part of this study.




.. History of Driven Piles

.. TODO: For your introduction, trace and find historical facts and pictures about driven piles.

.. There is evidence of people driving and and building on piles since 12,000 years ago. 4,000 years ago the Scots built islands that were founded on driven piles.

.. There is evidence in writing by Herodotus (400 BC) describing piles and pile driving.

.. Ancient Egyptians, Romans, Chinese, Mesopotamians all show use of driven piles. Furthermore, the methods of pile driving did not change up until 400 years ago. Logs driven into the ground by manual labor for thousands of years.

.. The machines that were used were not that simple.



*******************
Research Objectives
*******************

The author was charged with the completion of two main objectives with several sub-tasks attached to each one.

1. The assimilation of several publicly available load test databases into a modern relational database power by an easy-to-use interface
2. The development of batch-processing software that would utilize the new database and run analyses in bulk to deliver recommendations based on high-level statistics

The product of the first objective was `Pile Capacity <http://pilecapacity.com>`_, an online application with an HTML & Javascript frontend and a Python & Postgres backend that allows for collaborative analyses for driven piles and easily sharable results. *Pile Capacity* is envisioned to serve as an example of proper and efficient data management for the Geoprofession.

A product of the the second objective was *edafos* (`<https://github.com/nickmachairas/edafos>`_), a Python module programmed to run capacity calculations which allowed for batch-processing and analysis of hundreds of pile load test records.

Based on these two tools, this study was able to evaluate the efficacy of nominal resistance and interpreted capacity methods, under varying conditions, and provide recommendations on which method performs best. This is a departure from the *one-method-fits-all* approach of current practice in the Geoprofession.



*************************
Dissertation Organization
*************************

This dissertation was written in the `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`_ file format and was compiled using `Sphinx <http://www.sphinx-doc.org/>`_ (a Python documentation module written by Georg Brandl) producing both a PDF document that was printed and bound as well as an HTML page which can be viewed at `<http://phd.nickmachairas.com/>`_. These two mediums have identical contents.

An integral part of the dissertation is a web application named *Pile Capacity*, accessible at `<http://pilecapacity.com>`_. *Pile Capacity* was created by the author as part of this study. It is envisioned to grow and have its functionality extended beyond the scope if this study. The main parts of the application as well as an overview of the features of *Pile Capacity* are presented in :ref:`Chapter 2 <nyu_pile_capacity>`.

.. TODO: make sure that the text below is up-to-date with the chapter numbers

*(chapter numbering will be updated in the last version)*

Chapter 4 offers a comprehensive overview of the most popular methods for calculating the nominal resistance of driven piles. Chapter 5 presents a comparison and evaluation of nominal resistance methods for standard diameter piles while chapter 6 presents a comparison and evaluation of nominal resistance methods for large diameter piles. Chapter 7 offers a comprehensive overview of multiple methods for interpreting the capacity of driven piles from the results of static load tests. Chapter 8 presents a comparison and evaluation of interpreted capacity methods and provides recommendations based on the results of the study. In Chapter 9, a Machine Learning method for calculating nominal resistance is developed and tested with the results presented.

The :ref:`Appendix <appendix1>` includes valuable details on the source databases that were combined as part of this study as well as ETL and attribute mapping. A reader familiar with the original data sources is advised to refer to this section if identifying an original attribute in *Pile Capacity* is difficult.

There is no need for any software installations to interact with the software produced as part of this study. The software was developed in the form of a web application and the interested reader is advised to follow the hyperlinks provided above.
