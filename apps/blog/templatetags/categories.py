#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from ..models import Category, Entry

register = template.Library()


@register.inclusion_tag('tags/_categories_snippet.html')
def get_root_categories():
    t_categories = [{
            'title': cg.title, 
            'url': cg.get_absolute_url(),
            'count': reduce(lambda q,c: q + c.entries_published().count(), cg.get_descendants(include_self=True), 0)
        } for cg in Category.objects.filter(parent=None).order_by('weight')]
    return {'t_categories': t_categories}
