#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.dates import BaseArchiveIndexView
from django.views.generic.dates import BaseYearArchiveView
from django.views.generic.dates import BaseMonthArchiveView
from django.views.generic.dates import BaseDayArchiveView
from django.views.generic.dates import BaseTodayArchiveView
from django.views.generic.base import TemplateResponseMixin

from mixins.archives import EntryArchiveMixin
from mixins.json_response import RenderMixin
from blog.models import Entry, Category
from blog.breadcrumbs import Link


class EntryIndex(EntryArchiveMixin, BaseArchiveIndexView):
    """
    Mixin index.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs, direct subdirectories.
        """
        categories = Category.objects.filter(parent=None)
        labels = [Link(cg.title, cg.get_absolute_url()) for cg in categories]
        return {'breadcrumbs': [Link('Index')], 'labels': labels}


class EntryYear(EntryArchiveMixin, BaseYearArchiveView):
    """
    Mixin year.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs, direct subdirectories.
        """
        categories = Category.objects.filter(parent=None)
        labels = [Link(cg.title, cg.get_absolute_url()) for cg in categories]
        return {'breadcrumbs': [Link(self.kwargs['year'])], 'labels': labels}


class EntryMonth(EntryArchiveMixin, BaseMonthArchiveView):
    """
    Mixin month.
    """
