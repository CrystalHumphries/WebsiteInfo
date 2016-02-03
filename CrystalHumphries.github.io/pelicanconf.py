#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Crystal Humphries'
SITENAME = 'Data Scientist in Seattle'
SITEURL = 'https://crystalhumphries.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = '/Users/zephryin/pelican-themes/pelican-bootstrap3/' 
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/ce_humphries'),
('Github', 'http://github.com/CrystalHumphries'),
('LinkedIn', 'https://www.linkedin.com/in/crystalhumphries'))

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_TAGS_ON_SIDEBAR=True
TAGS_URL='tags.html'
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
BOOTSTRAP_NAVBAR_INVERSE=False

##addition to change css file###
################################
DISQUS_SITENAME="datascientistinseattle"
DISQUSURL='http://datascientistinseattle.disqus.com'

PYGMENTS_STYLE='colorful'


# tell pelican where your custom.css file is in your content folder
STATIC_PATHS = ['extras/custom.css']

# tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
'extras/custom.css': {'path': 'static/custom.css'}
}

# tell the pelican-bootstrap-3 theme where to find the custom.css file in your output folder
CUSTOM_CSS = 'static/custom.css'
