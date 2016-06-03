#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import logging

from django.shortcuts import HttpResponse
from django.core.urlresolvers import resolve

from .utils import extract
from .caches import EntryCounterCache, EntryActorCache
from .settings import PTN_BLOG_ENTRY_VIEWER, COOKIE_BLOG_ENTRY_ACTOR_KEY, BLOG_ENTRY_ACTOR_DELTA

logger = logging.getLogger('online')
# https://www.andreagrandi.it/2015/08/23/how-to-write-a-custom-django-middleware/


class LoggerMiddleware(object):
    """
    Middleware to record log.
    """

    def process_request(self, request):
        try:
            logger.info('[%s] Enter' % request.view_name)
            ip = request.META.get('REMOTE_ADDR', '')
            ua = request.META.get('HTTP_USER_AGENT', '')
            logger.info('[%s] [ip=%s] [ua=%s] Params: %s' % (request.view_name, ip, ua, extract(request)))
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
                entry_actor = EntryActorCache(request.entry, PTN_BLOG_ENTRY_VIEWER)
                actor_key = request.COOKIES.get(COOKIE_BLOG_ENTRY_ACTOR_KEY, None)
                if actor_key is None:
                    actor_key = uuid.uuid1()
                    response.set_cookie(COOKIE_BLOG_ENTRY_ACTOR_KEY, actor_key, 
                        max_age=BLOG_ENTRY_ACTOR_DELTA)

                if not entry_actor.exists(actor_key):
                    entry_counter = EntryCounterCache(request.entry)
                    entry_counter.incr('page_view_num')
                    entry_actor.add(actor_key)
        except Exception, e:
            logger.error('[%s] Add page view number except, err: %s' % (view_name, str(e)))
        finally:
            return response
