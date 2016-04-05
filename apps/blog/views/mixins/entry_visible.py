#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import Http404


class EntryVisibleMixin(object):
    """
    Mixin validating the entry's visibility.
    """

    def get_object(self, queryset=None):
        """
        Validate visibility.
        """
        obj = super(self.__class__, self).get_object(queryset)
        if obj.is_visible:
            return obj
        raise Http404('No such entry')