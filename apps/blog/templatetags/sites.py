#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

from blog.models import Site

register = template.Library()


@register.inclusion_tag('tags/_sites_snippet.html')
def get_sites():
    """
    Return useful sites.
    """
    t_sites = [{
            'title': s.title,
            'url': s.url
        } for s in Site.objects.filter(is_visible=True)]
    return {'t_sites': t_sites}
