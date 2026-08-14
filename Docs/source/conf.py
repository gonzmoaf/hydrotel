# Configuration file for the Sphinx documentation builder.

import os

# -- Project information

# General information about the project.
project = "HYDROTEL"
copyright = "2026, INRS"
author = "Institut national de la recherche scientifique"

version = '4.3.7'
release = '4.3.7'

# -- General configuration

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax", # Ensure render equations properly in HTML
]

myst_enable_extensions = [
    "dollarmath", # Parses $ and $$ delimiters
    "amsmath", # Parses direct LaTeX environments
]

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

#The suffix(es) of source filenames.
# You can specify multiple suffix as a dictionary of suffix: filetype
source_suffix = {".rst": "restructuredtext"}

# The master toctree document.
master_doc = "index"

# templates_path = ['_templates']

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# -- Options for HTML output

html_theme = os.environ.get("SPHINX_THEME", "sphinx_book_theme")
html_logo = '../logo/hydrotel_logo_transparent_rtd.png'

html_theme_options = {
    "logo":{
        "image_light": "../logo/hydrotel_logo_light_rtd.png",
        "image_dark": "../logo/hydrotel_logo_transparent_rtd.png",
    },
    "repository_url": "https://github.com/gonzmoaf/hydrotel.git",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
    "repository_branch": "asus",
    "path_to_docs": "Docs",
    "homepage_in_toc": False,
}

