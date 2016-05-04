#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import BaseListView

from mixins.archives import ArchiveConfMixin
from blog.settings import PAGINATION
from blog.models import Category, Entry
from blog.breadcrumbs import Link

def get_category_or_404(path):
    """
    Retrieve a category instance by a path.
    """
    path_crumbs = [p for p in path.split('/') if p]
    return get_object_or_404(Category, slug=path_crumbs[-1])


class BaseCategoryDetail(ArchiveConfMixin):
    """
    Mixin of categories.
    """

    def get_queryset(self):
        """
        Retrieve the category by its path and get its published entries.
        """
        self.category = get_category_or_404(self.kwargs['path'])
        entries = reduce(lambda q,c: q|c.entries_published(), self.category.get_descendants(include_self=True), Entry.objects.none())
        return entries

    def get_context_data(self, **kwargs):
        """
        [Override] Update context data when rendering.
        """
        context = super(BaseCategoryDetail, self).get_context_data(**kwargs)
        # context['category'] = self.category
        context.update(getattr(self, 'private_context_data', {}))
        return context


class CategoryDetail(BaseCategoryDetail, BaseListView, TemplateResponseMixin):
    """
    Category detail view.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs, direct subdirectories.
        """
        breadcrumbs = [Link(cg.title, cg.get_absolute_url()) for cg in self.category.get_ancestors(ascending=False, include_self=True)]
        labels = [Link(cg.title, cg.get_absolute_url()) for cg in self.category.children.all()]
        return {'breadcrumbs': breadcrumbs, 'labels': labels}
