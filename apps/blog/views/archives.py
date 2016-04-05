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
from blog.models import Entry


class EntryIndex(EntryArchiveMixin, BaseArchiveIndexView):
    """
    Mixin index.
    """
    pass


class EntryYear(EntryArchiveMixin, BaseYearArchiveView):
    """
    Mixin year.
    """
    pass


class EntryMonth(EntryArchiveMixin, BaseMonthArchiveView):
    """
    Mixin month.
    """
 