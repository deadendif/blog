#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.core.urlresolvers import resolve

logger = logging.getLogger('file')

class ViewNameMiddleware(object):
    """
    Middleware to add view name to request.
    """

    def process_request(self, request):
        try:
            request.view_name = resolve(request.path).view_name
        except Exception, e:
            logger.warning('[ViewNameMiddleware] Resolve request path [path=%s] failed' % request.path)
        finally:
            return None
