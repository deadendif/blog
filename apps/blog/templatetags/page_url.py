#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import resolve, reverse
    
register = template.Library()


@register.filter
def page_url(path, page):
    """
    Return the url of the page.
    """
    match = resolve(path)
    match.kwargs.update({'page': page})
    page_key = '_paginated'
    match.view_name += (page_key if page_key not in match.view_name else '')
    return reverse(match.view_name, args=match.args, kwargs=match.kwargs)
