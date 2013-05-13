#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import join as pjoin

AUTHOR = u'Matthew Brett'
SITENAME = u'World of Nipy'
SITEURL = 'http://matthew-brett.github.io/nipyworld-blog'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Old nipy blog', 'http://nipyworld.blogspot.com'),
          ('My pages', 'http://matthew.dynevor.org'),
          ('Nipy', 'http://nipy.org/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = (())

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Change them
THEME = pjoin('pelican-themes', 'syte')

# Add downloads directory to static paths
STATIC_PATHS = ['images', 'download']

# Plugins
PLUGIN_PATH = pjoin('pelican-plugins')
PLUGINS = ['assets']

# Syte stuff
ABOUT = u'Ash from the cigarette of working on NIPY'
SITE_DESCRIPTION = (u'About working on NIPY')
SITE_KEYWORDS = u'NIPY, Python, Imaging, Neuroimaging, FMRI'
GOOGLE_PLUSONE = True
CONTACT = u'matthew.brett@gmail.com'

# Pages that should be served as links (all pages in contents/pages)
DISPLAY_PAGES_ON_MENU = True
