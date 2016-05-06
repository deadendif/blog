#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import BaseListView

from blog.breadcrumbs import Link
from mixins.tags import TagDetailMixin


class TagDetail(TagDetailMixin, BaseListView, TemplateResponseMixin):
    """
    Tag detail view.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs.
        """
        return {'breadcrumbs': [Link('Tag : %s' % self.tag.name)], 'labels': []}