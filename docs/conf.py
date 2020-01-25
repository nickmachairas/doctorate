# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Modern Data Management and Analysis of Driven Piles'
copyright = '2019, Nikolaos Machairas'
author = 'Nikolaos Machairas'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.inc.rst']

numfig = True
# numfig_format = {'figure': 'My fig %s', 'table': 'My tab %s', 'code-block': 'My code %s'}
math_eqref_format = 'Eq. {number}'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_theme_options = {
    'logo': 'nyu_short_color.png',
    'description': '<em>"Modern Data Management and Analysis of Driven Piles'
                   '"</em>, PhD Dissertation'
                   ' by Nikolaos Machairas</br>',
    'show_relbar_bottom': True,
    'page_width': '1000px',
    'sidebar_width': '240px',
    'logo_text_align': 'justify',
    'font_size': 9,
    # 'fixed_sidebar': True,
}

# html_sidebars = {
#     '**' : [
#         # 'about.html',
#     ]
# }

html_favicon = '_static/nyu_icon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
    app.add_stylesheet('css/custom.css')


# -- LaTeX customizations

latex_appendices = [
    'a1-soil-approx/soil-approx',
    'a2-piles-notations/notations',
    'a3-db-tables/_db_appendix']

texinfo_appendices = [
    'a1-soil-approx/soil-approx',
    'a2-piles-notations/notations',
    'a3-db-tables/_db_appendix']

latex_elements = {
    'pointsize': '12pt',
    'geometry': '\\usepackage[top = 1in, bottom = 1in, left = 1.5in, right = 1in]{geometry}',
    'extraclassoptions': 'oneside',
    'preamble': r'''
        
        %\renewcommand{\baselinestretch}{1.5}
        %\linespread{1.5}
        
        %\usepackage{listings}
        %\renewcommand\lstlistlistingname{List of Listings}
        %\lstdefinestyle{inText}{
        %   basicstyle=\tiny\ttfamily
        %}
        %\lstset{frame=single}
        
        %\RequirePackage{tocbibind} %% % c omment this to remove page number for following
        %\addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        %\addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
        %\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
        % \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}
        
        
        %% spacing between line
        \usepackage{setspace}
        \onehalfspacing
        %\doublespacing
        %\singlespacing
        
        % line spacing and font size for tables
        \usepackage{etoolbox}
        \BeforeBeginEnvironment{longtable}{\begin{singlespace}\footnotesize}
        \AfterEndEnvironment{longtable}{\end{singlespace}}
        \BeforeBeginEnvironment{tabulary}{\begin{singlespace}\footnotesize}
        \AfterEndEnvironment{tabulary}{\end{singlespace}}
        \BeforeBeginEnvironment{tabular}{\begin{singlespace}\footnotesize}
        \AfterEndEnvironment{tabular}{\end{singlespace}}
        
        %% reduce spacing for itemize
        \usepackage{enumitem}
        \setlist{nosep}
        
        %% page line numbers
        %\usepackage{lineno}
        %\linenumbers
        
        %% footer
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}
        
        %% watermark
        % \usepackage{draftwatermark}
        % \SetWatermarkText{Draft v.0.5}
        % \SetWatermarkScale{1}
        % \SetWatermarkColor[gray]{0.96}
        % \SetWatermarkAngle{52}
        
        %% to move the signatures to the right
        \usepackage{changepage}

    ''',
    'maketitle': r'''
    
        \pagenumbering{Roman} %% % to avoid page 1 conflict with actual page 1
        
        \begin{titlepage}
        \centering
            
            %% \vspace*{3.75 in}
            
            %% For Guidance Committee Review\\
            %% Current: v.0.7.0 - 12/18/2019\\
            %% Next revision: by 12/19/2019
            
            %% \newpage
            
            \textbf{\LARGE ASSESSMENT OF PILE DESIGN METHODS}
            \vspace*{0.05 in}

            \textbf{\LARGE USING ADVANCED DATA ANALYTICS}
            \vspace*{0.2 in}
            
            \noindent\rule{8cm}{0.4pt}
            \vspace*{0.3 in}
            
            \textbf{\Large DISSERTATION}
            \vspace*{0.3 in}
            
            \textbf{\large Submitted in Partial Fulfillment of}
            \vspace*{0.15 in}
            
            \textbf{\large the Requirements for}
            \vspace*{0.15 in}
            
            \textbf{\large the Degree of}
            \vspace*{0.3 in}
            
            \textbf{\Large DOCTOR OF PHILOSOPHY (CIVIL ENGINEERING)}
            \vspace*{0.3 in}
            
            \textbf{\large at the}
            \vspace*{0.3 in}
            
            \textbf{\LARGE NEW YORK UNIVERSITY}
            
            \textbf{\LARGE TANDON SCHOOL OF ENGINEERING}
            \vspace*{0.3 in}
            
            \textbf{\large by}
            \vspace*{0.4 in}
            
            \textbf{\LARGE Nikolaos Machairas}
            \vspace*{0.3 in}
            
            \textbf{\Large January 2020}
        
        
        
        
        
        
        \newpage
        %\chapter*{ }
        %\vspace*{-2.0 in}
        \begin{center}
            
            \textbf{\Large ASSESSMENT OF PILE DESIGN METHODS}
            \vspace*{0.05 in}

            \textbf{\Large USING ADVANCED DATA ANALYTICS}
            \vspace*{0.05 in}
            
            \noindent\rule{8cm}{0.4pt}
            \vspace*{0.1 in}
            
            \textbf{\Large DISSERTATION}
            \vspace*{0.2 in}
            
            \textbf{\normalsize Submitted in Partial Fulfillment of}
            \vspace*{0.05 in}
            
            \textbf{\normalsize the Requirements for}
            \vspace*{0.05 in}
            
            \textbf{\normalsize the Degree of}
            \vspace*{0.15 in}
            
            \textbf{\Large DOCTOR OF PHILOSOPHY (CIVIL ENGINEERING)}
            \vspace*{0.15 in}
            
            \textbf{\normalsize at the}
            \vspace*{0.2 in}
            
            \textbf{\LARGE NEW YORK UNIVERSITY}
            
            \textbf{\LARGE TANDON SCHOOL OF ENGINEERING}
            \vspace*{0.2 in}
            
            \textbf{\normalsize by}
            \vspace*{0.15 in}
            
            \textbf{\Large Nikolaos Machairas}
            \vspace*{0.075 in}
            
            \textbf{\normalsize January 2020}
            
            \vspace*{0.2 in}
        
        \end{center}
        \begin{adjustwidth}{3.5 in}{}
            \begin{singlespacing}
            {\small
            Approved:
            
            \vspace*{0.2 in}
            
            \noindent\rule{2.5 in}{0.4pt} \\
            Department Chair
            
            \vspace*{0.075 in}
            
            \noindent\rule{2.5 in}{0.4pt} \\
            Date
            }
            \end{singlespacing}
        \end{adjustwidth}
        
        \begin{adjustwidth}{0.1 in}{}
            University ID:\hspace{10pt}N18574205 \\
            Net ID:\hspace{43pt}nm1213
        \end{adjustwidth}        

        
        
        \end{titlepage}
        
        
        
        \pagenumbering{roman}
        
        \newpage
            \chapter*{ }
            \vspace*{-2 in}
            Approved by the Guidance Committee:
            
            \vspace*{0.1 in}
            
            \underline{Major:} \hspace{0.5 in} Civil (Geotechnical) Engineering
            
            \vspace*{0.05 in}
            
            \begin{adjustwidth}{2.75 in}{}
            \begin{singlespacing}
            {\small
            \noindent\rule{3.25 in}{0.4pt} \\
            \textbf{Magued Iskander, PhD, PE, F.ASCE} \\
            Professor \& Chair, Civil \& Urban Engineering, NYU
            
            \vspace*{0.1 in}
            
            \noindent\rule{2 in}{0.4pt} \\
            Date
            
            \vspace*{0.25 in}
            
            \noindent\rule{3.25 in}{0.4pt} \\
            \textbf{Mohsen Hossein, PhD} \\
            Industry Professor, Civil \& Urban Engineering, NYU
            
            \vspace*{0.1 in}
            
            \noindent\rule{2 in}{0.4pt} \\
            Date
            
            \vspace*{0.25 in}
            
            \noindent\rule{3.25 in}{0.4pt} \\
            \textbf{Torsten Suel, PhD} \\
            Professor, Computer Science \& Engineering, NYU
            
            \vspace*{0.1 in}
            
            \noindent\rule{2 in}{0.4pt} \\
            Date
            
            \vspace*{0.25 in}
            
            \noindent\rule{3.25 in}{0.4pt} \\
            \textbf{Debra Laefer, PhD} \\
            Professor, Civil \& Urban Engineering, NYU
            
            \vspace*{0.1 in}
            
            \noindent\rule{2 in}{0.4pt} \\
            Date
            
            \vspace*{0.25 in}
            
            \noindent\rule{3.25 in}{0.4pt} \\
            \textbf{Muhannad Suleiman, PhD} \\
            Associate Professor, Civil \& Environmental Engineering, Lehigh University
            
            \vspace*{0.1 in}
            
            \noindent\rule{2 in}{0.4pt} \\
            Date
            
            %\vspace*{0.25 in}
            
            %\noindent\rule{3.25 in}{0.4pt} \\
            %\textbf{Antonio Marinucci, PhD, PE, MBA} \\
            %Research Professor, Civil \& Urban Engineering, NYU
            
            %\vspace*{0.1 in}
            
            %\noindent\rule{2 in}{0.4pt} \\
            %Date
            
            }
            \end{singlespacing}
            \end{adjustwidth}
            
        
        \newpage
            \chapter*{Vita}
            \vspace*{0.3 in}
            {\normalsize
            Nikolaos "Nick" Machairas was born in Athens, Greece on August 30, 
            1984 to Panagiotis and Maria Machairas. He graduated from the Pierce 
            College High School Athens in 2002. Nick studied Geology at the 
            National and Kapodestrian University of Athens while working as a 
            superintendent on residential construction projects under the
            supervision of his father, Panagiotis. In 2008, after completing his
            mandatory military service in the Hellenic Army, Nick immigrated to
            the United States. Between 2008 and 2011, Nick earned a Bachelors
            degree in Civil Engineering from NYU School of Engineering 
            with honors and a Masters degree in Civil Engineering from Columbia 
            University. From 2011 to 2013 he returned back to Greece to work 
            in the family construction business. Since 2013, Nick has been 
            living in Brooklyn, New York, working at NYU while earning his 
            doctoral degree in Civil (Geotechnical) Engineering under the 
            mentorship of Dr. Magued Iskander. Since 2017 and as of this writing,  
            he has been a part-time lecturer at Columbia University teaching  
            Relational \& NoSQL Databases and Applied Analytics.
            
            On August 4, 2019 Nick married Inga Jukneviciute.
            }
        
        \newpage
            \chapter*{Acknowledgements}
            \vspace*{0.3 in}
            {\normalsize
            First and foremost, I would like to thank my advisor and mentor, 
            Professor Magued Iskander. Our friendship is older than this study 
            dating back to 2008 when I first moved to the United States. Inga 
            and I are truly grateful for his support. I would also like to 
            thank Professors Maloof, Ulerio and Hossein. Their ethos as well as 
            their support for and dedication to all students is a big part of 
            what makes the Engineering school so special. Moreover, I would like
            to acknowledge my fellow research teammates at NYU. Thank you for 
            putting up with my (often foolish) ideas and for pushing me to do 
            better. Finally, I would like to express my gratitude to the 
            distinguished members of my guidance committee. Thank you for your 
            time and for lending your expertise.
            }
        
        \newpage
            \chapter*{ }
            \vspace*{1.5 in}
            \begin{center}
            \textit
            {\large
            To Inga, Dad, Mom, Mary, Anna and George. \\            
            Nothing would be possible without your love and support.
            }
            \end{center}
        
        \newpage
            \chapter*{ }
            \vspace*{-1.5 in}
            \begin{center}
            
            \textbf{\large ABSTRACT}
            
            \noindent\rule{2 in}{0.5pt}
            \vspace*{0.1 in}
            
            \textbf{\large ASSESSMENT OF PILE DESIGN METHODS}
            \vspace*{0.05 in}

            \textbf{\large USING ADVANCED DATA ANALYTICS}
            \vspace*{0.05 in}

            \textbf{\large by}
            \vspace*{0.05 in}

            \textbf{\large Nikolaos Machairas}
            \vspace*{0.05 in}

            \textbf{\large Advisor: Prof. Magued Iskander, PhD, PE, F.ASCE}
            \vspace*{0.2 in}

            \textbf{Submitted in Partial Fulfillment of the Requirements for}

            \textbf{the Degree of Doctor of Philosophy (Civil Engineering)}
            \vspace*{0.15 in}

            \textbf{January 2020}
            \vspace*{0.4 in}
            
            \end{center}
            
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
            \textit{NYU Pile Capacity} was developed that allowed for the 
            collaborative data storage, cleaning and analysis of data for deep
            foundations. \textit{NYU Pile Capacity} has a relational database  
            backend and a friendly HTML interface for user interactions.
            Existing load test databases have been delivered as locally installed
            software applications. \textit{NYU Pile Capacity}, however, required 
            no software installations and was served over the Internet as a web
            application. Users can log in and instantly start running custom
            aggregate analyses on the 5,000+ records that were imported 
            from existing datasets or add new records.
            
            \textit{NYU Pile Capacity} was built using Python Flask and 
            can batch-process multiple load test records for practically 
            countless combinations of soil conditions and pile types. 
            Furthermore, \textit{NYU Pile Capacity} was designed to be extended 
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
            the recommended \textit{Nordlund} and \textit{Tomlinson} methods 
            were not producing optimal designs. Instead, the less popular 
            \textit{API} and \textit{Lambda} methods proved far  superior. 
            Also, a comprehensive evaluation of interpreted capacity 
            methods validated the dominance of the original \textit{Davisson} 
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
            where a \textit{Support Vector Machine} algorithm outperformed the 
            Federal design method for driven piles. Perhaps more remarkably, the 
            predictive model outperformed the FHWA pile design method by relying 
            only on seven readily available features as compared to a laborious 
            and error-prone design methodology.
            
            Finally, this dissertation presented the argument for the 
            \textit{case-based design} of driven pile foundations. Most of the 
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
            conditions and pile type. Hence, \textit{case-based design} can lead 
            to safer and cost-effective designs for driven pile foundations.

        
        \tableofcontents
        \cleardoublepage
        \addcontentsline{toc}{chapter}{\listfigurename}
        \listoffigures
        \cleardoublepage
        \addcontentsline{toc}{chapter}{\listtablename}
        \listoftables
        \clearpage
        \pagenumbering{arabic}
    ''',
    'tableofcontents': ' ',
}


from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter


class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\linespread{1}\scriptsize"


PygmentsBridge.latex_formatter = CustomLatexFormatter
