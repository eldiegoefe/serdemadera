#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diego Fainstein'
SITENAME = u'Ser de Madera'
SITESUBTITLE = u'Diario de un aprendiz de ebanista'
SITEURL = 'https://eldiegoefe.github.io/serdemadera'
TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = u'es'
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE_FORMAT = '%Y %B %d %a'
DATE_FORMATS = {
    'en': ('en_US','%Y, %B %d %a'),
    'jp': ('ja_JP','%Y-%m-%d(%a)'),
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    # ('Archives', 'archives.html'),
          ('Foro Madera', 'http://www.foromadera.com'),
          ('Mi Blog: Certezas Dudosas', 'https://eldiegoefe.github.io'),
          )
          

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/eldiegoefe'),
          ('Github', 'https://github.com/eldiegoefe'),
          ('Facebook', 'https://www.facebook.com/eldiegoefe'),
          ('Flickr', 'https://www.flickr.com/photos/eldiegoefe/'),
          ('Instagram', 'https://instagram.com/eldiegoefe'),
          ('Google+', 'https://plus.google.com/+DiegoEfe'),
          ('Diaspora', 'https://www.joindiaspora.com/u/eldiegoefe'),
)

DEFAULT_PAGINATION = 20

# Seteos para modificar cuando pruebo el blog con un servidor en localhost
# Los posts con fecha futura se toman como drafts
# WITH_FUTURE_DATES = False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# THEME = "/home/user/pelican-themes/theme-name"
# Mis agregados

THEME = "../pelican-elegant"

# THEME = "notmyidea"    # es un tema built-in
# THEME = "foundation-default-colours"
# CSS_FILE = "elegant.css"


# TAG_CLOUD_STEPS = 4
# TAG_CLOUD_MAX_ITEMS = 100


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
DISQUS_SITENAME = "serdemadera"

# Instrucciones para la instalacion del plugin para videos de youtube
# en https://github.com/kura/pelican_youtube
PLUGIN_PATHS = ['../pelican-plugins']

LOAD_CONTENT_CACHE = False

# Direct_Templates lo requiere Elegant, esta habilitado mas abajo
# DIRECT_TEMPLATES = ('index', 'categories', 'archives')
TYPOGRIFY = True

TWITTER_USERNAME = 'eldiegoefe'

# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_SAVE_AS = '/home/eldiegoefe/documentos/eldiegoefe.github.io/output/{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_EXCLUDES = ('pages',)
# PAGE_URL = 'pages/{slug}.html'


# Elegant requiere los siguientes seteos

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'pelican_youtube']
# el plugin pelican_youtube lo tenia desde antes de Elegant

MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# esto tambien es de Elegant...
# These are the optional configuration variables that you can define

RECENT_ARTICLES_COUNT = 30
COMMENTS_INTRO = u'Contame algo...'
SITE_LICENSE = u'Podes usar el contenido de este blog si pones un link hacia este sitio'
SITE_DESCRIPTION = u'Blog de Ebanistería'
EMAIL_SUBSCRIPTION_LABEL = u'Suscripción'
EMAIL_FIELD_PLACEHOLDER = u'¿dirección de e-mail?'
SUBSCRIBE_BUTTON_TITLE = u'Suscribirme'
# MAILCHIMP_FORM_ACTION = u'Esto es del mailchimp'

LANDING_PAGE_ABOUT = ({'title': 'Diario de un aprendizaje dificil', 'details': '<p>A veces las pasiones nos encuentran y nos cambian, a pesar de nuestra dureza. Me pasa con el oficio de construir en madera objetos útiles y hermosos.</p>'})

# PROJECTS = [{
#     'name': 'Logpad + Duration',
#     'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
#     'description': 'Vim plugin to emulate Windows Notepad logging feature,'
#     ' and log duration of each entry'},
#     {'name': 'Elegant Theme for Pelican',
#     'url': 'https://oncrashreboot.com/pelican-elegant',
#     'description': 'A clean and distraction free theme, with search and a'
#     ' lot more unique features, using Jinja2 and Bootstrap'}]


# These are the optional article meta data variables that you can use

# subtitle
# summary
# disqus_identifier
# modified
# keywords

# info sobre sitemap. priorities y changefreqs tienen valores que usan
# los buscadores. mas info en:
# https://docs.getpelican.com/en/3.1.1/plugins.html#sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
