#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import resolve

register = template.Library()


@register.filter
def location(path, view_name):
    """
    Weather the path agrees with name.
    """
    match  = resolve(path)
    if match.view_name[:len(view_name)] == view_name:
        return True
    return False