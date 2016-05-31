#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager

from blog.utils import entries_published


class Category(MPTTModel):
    """
    Entry's Category model.
    """
    title = models.CharField('title',
            max_length=255,
            help_text='Title of the category.')
    slug = models.SlugField('slug',
            unique=True, max_length=255,
            help_text="Used to build the category\' URL.")
    description = models.TextField('description',
            blank=True,
            help_text="Describe the category.")
    weight = models.IntegerField('weight',
            default=0,
            help_text="Used to sort category.")
    parent = TreeForeignKey(
            'self', related_name='children', null=True, blank=True, db_index=True,
            help_text='Parent category.')

    objects = TreeManager()

    def entries_published(self):
        """
        Return category's published entries.
        """
        return entries_published(self.entries)

    @property
    def tree_path(self):
        """
        Return category's tree path.
        """
        return '/'.join([anc.slug for anc in self.get_ancestors(False, True)])

    @models.permalink
    def get_absolute_url(self):
        """
        Return the category's URL.
        """
        return ('blog:categories:detail', (self.tree_path, ))

    def __str__(self):
        return '%s: %s' % (self.title, self.tree_path)

    class Meta:
        ordering = ['title']

    class MPTTMeta:
        order_insertion_by = ['title']

