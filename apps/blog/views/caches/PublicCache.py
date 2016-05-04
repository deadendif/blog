#!/usr/bin/env python
# -*- coding: utf-8 -*-


from blog.models import Entry, Category


class WidgetsCache(object):
    """
    Cache public context data when rendering.
    """

    def __init__(self):
        pass


    @property
    def get(self, key):
        pass

    def get_all(self):
        """
        """
        return {'categories': {'title': '编程语言',
                             'url': '127.0.0.1',
                             'count': 2}}
