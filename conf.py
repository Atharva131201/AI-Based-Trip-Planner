# Configuration file for the Sphinx documentation builder

# -- Project information -----------------------------------------------------

project = 'AI BASED TRIP PLANNER'
author = 'Atharva Nandurkar and Chetana Shinde'
version = '1.0'
release = '1.0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    # Add more extensions as needed
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Source directory --------------------------------------------------------

master_doc = 'index'
source_suffix = '.rst'

# -- Other settings ----------------------------------------------------------

# Additional settings can include specifying paths, configuring extensions,
# defining options for specific extensions, etc.
