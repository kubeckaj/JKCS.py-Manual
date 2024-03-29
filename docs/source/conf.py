# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'JKCS'
copyright = '2021, Jakub Kubečka'
author = 'Jakub Kubečka'

release = '3.0'
version = '3.0.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_togglebutton',
    'sphinx_tabs.tabs',
]

#'sphinxcontrib.bibtex',

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

master_doc = 'index'
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_css_files = [ "custom.css", ]


