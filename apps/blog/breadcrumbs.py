#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from django.utils.timezone import format
from django.core.urlresolvers import reverse

class Link(object):
    """
    Link of the breadcrumbs.
    """
    def __init__(self, name, url=None):
        self.name = name
        self.url = url

    def __str__(self):
        return '%s: %s' % (self.name, self.url)

def year_crumb(date):
    """
    Year crumb.
    """
    year = date.strftime('%Y')
    return Link(year, reverse('blog:entry_archives:year', args=[year]))

def month_crumb(date):
    """
    Month crumb.
    """
    year = date.strftime('%Y')
    month = date.strftime('%m')
    # month_text = format(date, 'F').capitalize()
    return Link(month, reverse('blog:entry_archives:month', args=[year, month]))

def year_breadcrumbs(year):
    """
    Breadcrumbs of a year.
    """
    pass


def entry_breadcrumbs(entry):
    """
    Breadcrumbs of an entry.
    """
    return [year_crumb(entry.create_time),
            month_crumb(entry.create_time),
            day_crumb(entry.create_time),
            Link(entry.title)]

def category_breadcrumbs(category):
    pass

def archive_breadcrumbs():
    pass

