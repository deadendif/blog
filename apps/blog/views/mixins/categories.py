#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from archives import ArchiveConfMixin
from blog.models import Category, Entry

def get_category_or_404(path):
    """
    Retrieve a category instance by a path.
    """
    path_crumbs = [p for p in path.split('/') if p]
    return get_object_or_404(Category, slug=path_crumbs[-1])


class CategoryDetailMixin(ArchiveConfMixin):
    """
    Mixin of categoriy detail.
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
        context = super(CategoryDetailMixin, self).get_context_data(**kwargs)
        # context['category'] = self.category
        context.update(getattr(self, 'private_context_data', {}))
        return context
