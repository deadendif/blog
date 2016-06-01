#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.core.urlresolvers import resolve

logger = logging.getLogger('online')


class ViewNameMiddleware(object):
    """
    Middleware to add view name to request.
    """

    def process_request(self, request):
        try:
            request.view_name = resolve(request.path).view_name
        except Exception, e:
            ip = request.META.get('REMOTE_ADDR', '')
            ua = request.META.get('HTTP_USER_AGENT', '')
            logger.warning('[ViewNameMiddleware] [ip=%s] [ua=%s] Resolve request path [path=%s] failed' % (ip, ua, request.path))
        finally:
            return None
