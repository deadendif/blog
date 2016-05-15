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
            logger.error('[ViewNameMiddleware] add view name to request except, err: %s' % str(e))
        finally:
            return None
