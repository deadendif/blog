#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Entry status """
DRAFT     = 1
HIDDEN    = 2
PUBLISHED = 3

""" Entry detail templates """
ENTRY_DETAIL_TEMPLATES = [('default', 'default'), ]

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

""" Min time delta between two valid page view """
BLOG_ENTRY_ACTOR_DELTA = 30


""" Redis config """
REDIS_DB_BLOG = 1
REDIS_EXPIRE_BLOG_ENTRY_COUNTER = 3600 * 24 * 14
REDIS_EXPIRE_BLOG_ENTRY_VIEWER  = 3600 * 1

""" Key patterns of cached entry counter """
PTN_BLOG_ENTRY_COUNTER_PV = 'BL_ET_CT_PV_%d'
PTN_BLOG_ENTRY_COUNTER_UF = 'BL_ET_CT_UF_%d'
PTN_BLOG_ENTRY_COUNTER_UL = 'BL_ET_CT_UL_%d'
PTN_BLOG_ENTRY_VIEWER     = 'BL_ET_VW_%d'
PTN_BLOG_ENTRY_FEEDBACK   = 'BL_ET_FB_%d'

