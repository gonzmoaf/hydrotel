# Configuration file for the Sphinx documentation builder.

import os

# -- Project information

project = 'HYDROTEL'
copyright = '2001, INRS'
author = 'Fortin, J.-P. et al.'

version = '4.3.7'

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_codeautolink",
    "sphinx_copybutton",
    "nbsphinx",
    "sphinx_design",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

#The suffix(es) of source filenames.
# You can specify multiple suffix as a dictionary of suffix: filetype
source_suffix = {".rst": "restructuredtext"}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "hydrotel"
copyright = "2026, INRS"
author = "Institut national de la recherche scientifique"

templates_path = ['_templates']

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "light_logo": "hydrotel_logo_light_rtd.png",
    "dark_logo": "hydrotel_logo_transparent_rtd.png",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
if not os.path.exists("_static"):
    os.makedirs("_static")
html_static_path = ["_static", "logo"]

# html_sidebars = {
#     "**": [
#         "sidebar/scroll-start.html",
#         "sidebar/brand.html",
#         "sidebar/search.html",
#         "sidebar/navigation.html",
#         "sidebar/ethical-ads.html",
#         "sidebar/scroll-end.html",
#     ]
# }

def setup(app):
    app.add_css_file("style.css")
