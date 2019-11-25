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

latex_appendices = ['a1-db-tables/_db_appendix']

texinfo_appendices = ['a1-db-tables/_db_appendix']

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
        \usepackage{lineno}
        \linenumbers
        
        %% footer
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}

    ''',
    'maketitle': r'''
    
        \pagenumbering{Roman} %% % to avoid page 1 conflict with actual page 1
        
        \begin{titlepage}
        \centering
            
            \textbf{\Large MODERN DATA MANAGEMENT AND}
            \vspace*{0.05 in}

            \textbf{\Large ANALYSIS OF DRIVEN PILES}
            \vspace*{0.1 in}
            
            \noindent\rule{8cm}{0.4pt}
            \vspace*{0.2 in}
            
            \textbf{\Large DISSERTATION}
            \vspace*{0.3 in}
            
            \textbf{\normalsize Submitted in Partial Fulfillment of}
            \vspace*{0.15 in}
            
            \textbf{\normalsize the Requirements for}
            \vspace*{0.15 in}
            
            \textbf{\normalsize the Degree of}
            \vspace*{0.2 in}
            
            \textbf{\Large DOCTOR OF PHILOSOPHY (CIVIL ENGINEERING)}
            \vspace*{0.3 in}
            
            \textbf{\normalsize at the}
            \vspace*{0.3 in}
            
            \textbf{\LARGE NEW YORK UNIVERSITY}
            
            \textbf{\LARGE TANDON SCHOOL OF ENGINEERING}
            \vspace*{0.3 in}
            
            \textbf{\normalsize by}
            \vspace*{0.3 in}
            
            \textbf{\Large Nikolaos Machairas}
            \vspace*{0.3 in}
            
            \textbf{\normalsize January 2020}
        
        \end{titlepage}
        
        
        \pagenumbering{roman}
        
        \newpage
            \chapter*{Committee signature page}
        
        \newpage
            \chapter*{Vita}
        
        \newpage
            \chapter*{Acknowledgements}
        
        \newpage
            \chapter*{Dedication Page}
        
        \newpage
            \chapter*{Abstract}
        
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
