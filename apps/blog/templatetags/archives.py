#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse

from ..settings import RECENT_ARCHIVES_NUM
from ..utils import recent_year_month

register = template.Library()


@register.inclusion_tag('tags/_archives_snippet.html')
def get_recent_archives():
    """
    Return recent archives.
    """
    def _build(year, month):
        return {
            'title': '%d年%02d月' % (year, month),
            'url': reverse('blog:archives:month', args=['%d' % year,  '%02d' % month])
        }

    t_archives = [_build(ym[0], ym[1]) for ym in map(lambda x: recent_year_month(x), range(RECENT_ARCHIVES_NUM))]
    return {'t_archives': t_archives}
