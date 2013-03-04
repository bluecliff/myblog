#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'lijsf'
SITENAME = u'Blue Dream'
SITEURL = 'http://bluedream.me'
#THEME = "notmyidea"
THEME = "pelican-octopress-theme-master"
TIMEZONE = 'Asia/Shanghai'
SITESUBTITLE = u"世事洞察皆学问,人情练达即文章"
DEFAULT_LANG = u'cn'
SITEURLABS = 'http:/bluedream.me'

UYN = True
GITHUB_URL= "https://github.com/lijsf"
GOOGLE_PLUS_URL = "li0shuangjiang@gmail.com"
TWITTER_URL = "https://twitter.com/bluedream"

CSS_PYGEMENT = "default.css"

DISPLAY_PAGES_ON_MENU =True
MD_EXTENSIONS = (['codehilite','extra'])
NEWEST_FIRST_ARCHIVES = True
# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
		  ('Bluedream', 'http://bluedream.me'),)

# Social widget
SOCIAL = (('Google+', 'https://plus.google.com/u/0/115690930397939734244/posts'),
		  ( 'weibo', 'http://weibo.com/u/1259626554')
          )

DEFAULT_PAGINATION = 5

USE_FOLDER_AS_CATEGORY = True

TEMPLATE_PAGES = {'about.html': 'about.html'}
