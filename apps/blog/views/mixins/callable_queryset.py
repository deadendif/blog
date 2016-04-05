#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured


class CallableQuerysetMixin(object):
    """
    Mixin for handling a callable queryset,
    which will force the update of the queryset.
    Related to issue http://code.djangoproject.com/ticket/8378
    """
    queryset = None

    def get_queryset(self):
        """
        Validate and call the queryset.
        """
        if self.queryset is None:
            raise ImproperlyConfigured("'%s' must define 'queryset'" % self.__class__.__name__)
        return self.queryset()