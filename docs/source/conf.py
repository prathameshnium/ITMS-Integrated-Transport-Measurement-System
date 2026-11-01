# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Integrated Transport Measurement System (ITMS)'
copyright = '2026, UGC DAE Consortium for Scientific Research, Mumbai Centre'
author = 'Dr. Sudip Mukherjee, Prathamesh Deshmukh, Swastika Mukherjee and Srishti Kashyap'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'myst_parser',           # For Markdown support
    'sphinx_sitemap',        # Generates sitemap.xml for search engines
    'sphinxext.opengraph',   # Open Graph / social-preview meta tags
]

# Allow HTML <img> tags and ::: fences in Markdown pages
myst_enable_extensions = [
    "html_image",
    "colon_fence",
]

# Auto-generate GitHub-style anchors for headings (h1-h4) so in-page links
# resolve on Read the Docs, not just on GitHub
myst_heading_anchors = 4

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Sets <html lang="en"> — search engines use this for language targeting
language = 'en'

# -- SEO: canonical URL, sitemap, social previews -----------------------------
# The same conf builds two hosts: GitHub Pages and Read the Docs. Each build
# declares itself as canonical so neither site is deranked as duplicate
# content, and each gets a correct sitemap.xml.
_GITHUB_PAGES_URL = (
    'https://prathameshnium.github.io/'
    'ITMS-Integrated-Transport-Measurement-System/'
)
_RTD_URL = (
    'https://itms-integrated-transport-measurement-system.'
    'readthedocs.io/en/latest/'
)

if os.environ.get('READTHEDOCS'):
    html_baseurl = os.environ.get('READTHEDOCS_CANONICAL_URL', _RTD_URL)
else:
    html_baseurl = _GITHUB_PAGES_URL

# sphinx-sitemap: html_baseurl already carries the language/version prefix on
# RTD, so don't add another {lang}/{version} segment to sitemap entries
sitemap_url_scheme = '{link}'
# Search and the empty general index are thin pages that should not be indexed
sitemap_excludes = ['search.html', 'genindex.html']

# sphinxext-opengraph: og:title/description are derived per page
ogp_site_url = html_baseurl
ogp_site_name = 'ITMS — Integrated Transport Measurement System'
ogp_image = html_baseurl + '_static/UGC_DAE_CSR_logo.png'
ogp_type = 'website'
ogp_description_length = 200
ogp_enable_meta_description = True
# Social-card images need matplotlib; the logo above is used instead
ogp_social_cards = {'enable': False}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_title = 'Integrated Transport Measurement System'
html_short_title = 'ITMS Documentation'

# Sidebar branding (paths relative to this conf.py)
html_logo = '_static/UGC_DAE_CSR_logo.png'
html_favicon = '_static/favicon.ico'

# Show the full section tree in the sidebar from the landing page onwards,
# instead of collapsing navigation to top-level entries only
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'titles_only': False,
    'logo_only': False,
}

html_static_path = ['_static']

# robots.txt keeps the site's crawler policy consistent across GitHub Pages
# and Read the Docs
html_extra_path = ['robots.txt']
