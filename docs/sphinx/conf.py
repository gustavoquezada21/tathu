#
# This file is part of TATHU - Tracking and Analysis of Thunderstorms.
# Copyright (C) 2022 INPE.
#
# TATHU - Tracking and Analysis of Thunderstorms is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Configuration file for the TATHU - Tracking and Analysis of Thunderstorms documentation.

The documentation system is based on Sphinx. If you want to know
more about the options to be used for configuration, please, see:

- https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import tathu
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'TATHU'
copyright = '2022, INPE.'
author = 'Douglas Uba'
release = tathu.__version__


# -- General configuration ---------------------------------------------------

# Enabled Sphinx extensions.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx_rtd_theme',
    'sphinx_gallery.gen_gallery',
    # 'sphinx_tabs.tabs',s
]

# Configuration for gallery example.
sphinx_gallery_conf = {
    'examples_dirs': '../../examples/gallery', # path to example scripts (for gallery)
    'gallery_dirs': 'auto_examples', # path to where to save gallery generated output
}

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx.
language = 'en_US'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'analytics_id': 'XXXXXXXXXX',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': False,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False
}

html_baseurl = 'https://uba.github.io/tathu'

#html_theme_path = ''

#html_style = ''

html_title = 'TATHU'

html_context = {
    'display_github': False,
    'github_user': 'uba',
    'github_repo': 'tathu',
    'last_updated': False,
    #'commit': False,
}

html_show_sourcelink = False

html_logo = './img/logo-tathu.png'

html_favicon = './img/favicon.ico'

#html_static_path = ['_static']

html_css_files = [ ]

html_last_updated_fmt = '%b %d, %Y'

html_show_sphinx = False

html_search_language = 'en'

numfig = True

numfig_format = {
    'figure': 'Figure %s -',
    'table': 'Table %s -',
    'code-block': 'Code snippet %s -',
    'section': 'Section %s.'
}

copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

#def setup(app):
#    app.add_stylesheet('tathu.css')

#doctest_global_setup = '''
#import os
#
#TATHU_EXAMPLE_URL = os.getenv('TATHU_EXAMPLE_URL', None)
#'''

#todo_include_todos = True
#todo_emit_warnings = True
master_doc = 'index'
