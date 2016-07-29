#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import resolve

register = template.Library()


@register.filter
def location(path, view_names):
    """
    Weather the path agrees with name.
    """
    match  = resolve(path)
    view_name_list = [vn.strip() for vn in view_names.split('|')]
    for view_name in view_name_list:
        if match.view_name[:len(view_name)] == view_name:
            return True
    return False