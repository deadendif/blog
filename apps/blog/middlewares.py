#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.shortcuts import HttpResponse
from django.core.urlresolvers import resolve
from .utils import extract
from .caches import EntryCounterCache, EntryActorIpCache
from .settings import PTN_BLOG_ENTRY_VIEWER

logger = logging.getLogger('file')

# https://www.andreagrandi.it/2015/08/23/how-to-write-a-custom-django-middleware/

class LoggerMiddleware(object):
    """
    Middleware to record log.
    """

    def process_request(self, request):
        try:
            logger.info('[%s] Enter' % request.view_name)
            logger.info('[%s] Params: %s' % (request.view_name, extract(request)))
        except Exception, e:
            pass
        finally:
            return None

    def process_response(self, request, response):
        try:
            logger.info('[%s] Success' % (request.view_name))
        except Exception, e:
            pass
        finally:
            return response


class EntryCounterMiddleware(object):
    """
    Middleware to update entry's counter.
    """

    def process_response(self, request, response):
        try:
            view_name = request.view_name

            # Add page view number of the entry
            if request.method == 'GET' and view_name == 'blog:entries:detail':
                entry_actor = EntryActorIpCache(request.entry, PTN_BLOG_ENTRY_VIEWER)
                ip = request.META.get('REMOTE_ADDR', '')
                if not entry_actor.exists(ip):
                    entry_counter = EntryCounterCache(request.entry)
                    entry_counter.incr('page_view_num')
                    entry_actor.add(ip)
        except Exception, e:
            logger.error('[%s] add page view number except, err: %s' % (view_name, str(e)))
        finally:
            return response
