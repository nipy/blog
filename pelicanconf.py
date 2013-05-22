#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import join as pjoin

AUTHOR = u'The Nipy developers'
SITENAME = u'The Nipy blog'
SITEURL = 'http://blog.nipy.org'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# atom feeds
FEED_ATOM = 'feeds/all.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# RSS feeds
FEED_RSS = 'feeds/all.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Old nipy blog', 'http://nipyworld.blogspot.com'),
          ('Nipy', 'http://nipy.org/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = (())

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Change theme
THEME = pjoin('pelican-themes', 'tuxlite_tbs')

# Add downloads directory to static paths
STATIC_PATHS = ['images', 'download']

# Syte stuff
ABOUT = u'Ash from the cigarette of working on NIPY'
SITE_DESCRIPTION = (u'About working on NIPY')
SITE_KEYWORDS = u'NIPY, Python, Imaging, Neuroimaging, FMRI'
GOOGLE_PLUSONE = True
CONTACT = u'nipy-devel@neuroimaging.scipy.com'

# Pages that should be served as links (all pages in contents/pages)
DISPLAY_PAGES_ON_MENU = True
