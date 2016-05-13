#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.shortcuts import HttpResponse
from django.core.urlresolvers import resolve
from .utils import extract
from .caches import EntryCounterCache

logger = logging.getLogger('file')

# https://www.andreagrandi.it/2015/08/23/how-to-write-a-custom-django-middleware/

class LoggerMiddleware(object):
    """
    Middleware to record log.
    """

    def process_request(self, request):
        view_name = resolve(request.path).view_name
        logger.info('[%s] Enter' % view_name)
        logger.info('[%s] Params: %s' % (view_name, extract(request)))
        return None

    def process_response(self, request, response):
        logger.info('[%s] Success' % (resolve(request.path).view_name))
        return response


class EntryCounterMiddleware(object):
    """
    Middleware to update entry's counter.
    """

    def process_response(self, request, response):
        try:
            view_name = resolve(request.path).view_name

            # Add page view number of the entry
            if 'blog:entries:detail' == view_name:
                entry_counter = EntryCounterCache(request.entry)
                old = entry_counter.get('page_view_num')
                entry_counter.set('page_view_num', int(old) + 1)
        except Exception, e:
            logger.error('[%s] add page view number except, err: %s' % (view_name, str(e)))
        finally:
            return response
