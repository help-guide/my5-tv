# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any module directories here if needed.
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Watch Live Channels on My5 TV'
copyright = '2025, My5 TV'
author = 'My5 TV Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Extensions (if needed, like autodoc, napoleon, etc.)
extensions = []

# Templates path
templates_path = ['_templates']

# Patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Website and browser tab title
html_title = "Watch Live Channels on My5 TV – Activate at my5.tv/activate"

# Optional short title for navigation
html_short_title = "My5 TV Live Guide"

# Favicon (ensure it's placed in _static or root)
html_favicon = 'favicon.ico'

# HTML theme (can be customized or changed to another theme)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML inside .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Uncomment if you have CSS/JS/image files
# html_static_path = ['_static']
