#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import BaseListView

from ..utils import category_ancestors, category_children
from .mixins.categories import CategoryDetailMixin

class CategoryDetail(CategoryDetailMixin, BaseListView, TemplateResponseMixin):
    """
    Category detail view.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs, direct subdirectories.
        """
        breadcrumbs = category_ancestors(self.category)     
        labels = category_children(self.category)
        return {'breadcrumbs': breadcrumbs, 'labels': labels}
