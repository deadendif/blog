#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('tags/_categories_snippet.html')
def get_root_categories():
    t_categories = [{
            'title': cg.title, 
            'url': cg.get_absolute_url(),
            'count': 10
        } for cg in Category.objects.filter(parent=None)]
    if t_categories:
        t_categories[-1]['url'] = None
    print t_categories
    return {'t_categories': t_categories}
