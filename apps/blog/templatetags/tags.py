#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from django import template
from tagging.models import Tag

register = template.Library()


@register.inclusion_tag('tags/_tags_snippet.html')
def get_tags():
    """
    Return all tags's infomation.
    """
    from random import randint
    t_tags = [{
            'title': t.name,
            'url': '',
            'count': randint(0, 50)
        } for t in Tag.objects.all()]
    return {'t_tags': t_tags}


@register.filter
def size(count):
    """
    Return size according to 'count'.
    """
    BASE = 10
    SIZES = ['mini', 'tiny', 'small', 'medium', 'large', 'big', 'huge', 'massive']
    index = count / BASE if (count / BASE <= len(SIZES) - 1) else (len(SIZES) - 1)
    return SIZES[index]


@register.filter
def color(title):
    """
    Return color according to 'title'.
    """
    COLORS = ['red', 'orange', 'yellow', 'olive', 'green', 'teal', 'blue', 'violet', 'purple', 'pink', 'brown', 'grey', 'black']
    md5 = hashlib.md5()
    md5.update(str(title))
    index = int(md5.hexdigest()[3:6], 16) % len(COLORS)
    return COLORS[index]
