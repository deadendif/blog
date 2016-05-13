#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Entry status """
DRAFT     = 1
HIDDEN    = 2
PUBLISHED = 3

""" Entry detail templates """
ENTRY_DETAIL_TEMPLATES = [('xxx', '111'), ]

""" Upload path """
UPLOAD_IMAGE_TO = 'images/'

""" Splitters of entries """
SPLITTERS = ['<!-- more -->', ]

""" Archive pagination """
PAGINATION = 5

""" Archive allow empty or not """
ALLOW_EMPTY = True

""" Markdown extensions """
MARKDOWN_EXTENSIONS = ['markdown.extensions.tables', ]

""" Number of recent archives """
RECENT_ARCHIVES_NUM = 4

""" Hash value """
HASH_TAG_COLOR_START = 3
HASH_TAG_COLOR_END = 9

""" Min length of keyword for searching """
MIN_KEYWORD_LENGTH = 3

""" Entry search fields """
SEARCH_FIELDS = ['title', 'content']

""" Key patterns of cached entry counter """
COUNTER_PAGE_VIEW_PTN = 'CT_ENTRY_PV_%s'
COUNTER_USEFUL_PTN    = 'CT_ENTRY_UF_%s'
COUNTER_USELESS_PTN   = 'CT_ENTRY_UL_%s'

""" Redis config """
REDIS_DB_BLOG = 1
REDIS_EXPIRE_BLOG = 3600 * 24 * 30
