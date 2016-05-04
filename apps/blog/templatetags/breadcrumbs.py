#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.inclusion_tag('tags/_breadcrumbs_snippet.html', takes_context=True)
def breadcrumbs(context):
    """
    Breadcrumbs for the application.
    """
    path = context['request'].path
    return {'path': path}