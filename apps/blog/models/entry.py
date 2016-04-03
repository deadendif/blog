#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown as md

from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags

from tagging.fields import TagField
from tagging.utils import parse_tag_input

from author import Author
from category import Category
from blog.settings import DRAFT, HIDDEN, PUBLISHED
from blog.settings import ENTRY_DETAIL_TEMPLATES, SPLITTERS
from blog.utils import entries_published
from blog.managers import EntryPublishedManager


class Entry(models.Model):
    """
    Entry model class
    """
    STATUS = (
        (DRAFT, 'draft'),
        (HIDDEN, 'hidden'),
        (PUBLISHED, 'published')
    )

    title = models.CharField('title', 
            max_length=255,
            help_text='Title of the entry.')
    slug = models.SlugField('slug', 
            max_length=255,
            help_text='Used to build the entry\' URL.')
    status = models.IntegerField('status', 
            db_index=True, choices=STATUS, default=DRAFT,
            help_text='Status of the entry.')
    create_time = models.DateTimeField('Create time',
            db_index=True, default=timezone.now,
            help_text='Datetime when create the entry.')
    start_publish = models.DateTimeField('start publish',
            db_index=True, blank=True, null=True,
            help_text='Datetime when starting publication')
    end_publish = models.DateTimeField('end publish',
            db_index=True, blank=True, null=True,
            help_text='Datetime when stopping publication')
    last_update = models.DateTimeField('last update time',
            default=timezone.now,
            help_text='Datetime when last update the entry.')
    excerpt = models.TextField('excerpt',
            blank=True,
            help_text='Used to SEO purposes.')
    content = models.TextField('content',
            blank=True,
            help_text='Content of the entry.')
    featured = models.BooleanField('featrue',
            default=False,
            help_text='Telling if the entry is featured')
    author = models.ForeignKey(
            Author, related_name='entries', null=True, on_delete=models.SET_NULL,  # ???
            help_text='Author of the entry.')
    categories = models.ManyToManyField(
            Category, related_name='entries', blank=True,
            help_text='Categories that contain this entry.')
    tags = TagField('tags')
    login_required = models.BooleanField('login required',
            default=False,
            help_text='Telling if user need to be authenticated.')
    password = models.CharField('password',
            max_length=64, blank=True,
            help_text='Protects the entry with a password.')
    detail_template = models.CharField('detail template',
            max_length=255, choices=ENTRY_DETAIL_TEMPLATES,
            default=ENTRY_DETAIL_TEMPLATES[0],
            help_text='The detail tempate of the entry.')

    # Set managers
    objects = models.Manager()
    published = EntryPublishedManager()
    
    @property
    def publish_date(self):
        """
        Return publish date or create data.
        """
        return self.start_publish or self.create_time

    @property
    def is_visible(self):
        """
        Check if the entry is visible.
        """
        now = timezone.now()
        if (self.start_publish and now < self.start_publish) or \
                (self.end_publish and now >= self.end_publish):
            return False
        return self.status == PUBLISHED

    @property
    def previous_next_entry(self):
        """
        Return and cache previous and next published entry.
        """
        attr_name = 'previous_next'
        previous_next = getattr(self, attr_name, None)

        if previous_next is None:
            if not self.is_visible:
                previous_next = (None, None)
                setattr(self, 'previous_next', previous_next)
                return previous_next

            entries = list(self.__class__.published.all())
            index = entries.index(self)

            previous_entry = entries[index + 1] if index + 1 < len(entries) else None
            next_entry = entries[index - 1] if index > 0 else None 
            previous_next = (previous_entry, next_entry)
            setattr(self, attr_name, previous_next)
        return previous_next


    @property
    def previous_entry(self):
        """
        Return the previous published entry if exists.
        """
        return self.previous_next_entry[0]


    @property
    def next_entry(self):
        """
        Return the next published entry if exist.
        """
        return self.previous_next_entry[1]

    @property
    def tags_list(self):
        """
        Return iterable list of tags.
        """
        return parse_tag_input(self.tags)
 
    @models.permalink
    def get_absolute_url(self):
        """
        Return the entry's URL
        """
        ctime = self.create_time
        return ('blog:entry_detail', (), {
            'year': self.create_time.strftime('%Y'),
            'month': self.create_time.strftime('%m'),
            'day': self.create_time.strftime('%d'),
            'slug': self.slug
            })

    @property
    def html_content(self):
        """
        Return html content
        """
        return md.markdown('content', extensions=['markdown.extensions.tables'])

    @property
    def html_preview(self):
        """
        Return html preview object
        """
        return HtmlPreview(self.html_content, SPLITTERS)

    @property
    def word_count(self):
        """
        Return the number of words
        """
        return len(strip_tags(self.html_content).split())

    def save(self, *args, **kwargs):
        """
        [Override] update fields: last_update, excerpt
        """
        self.last_update = timezone.now()
        if not self.excerpt and self.status == PUBLISHED:
            self.excerpt = Truncator(strip_tags(getattr(self, 'content', ''))).words(50)
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s' % (self.title, STATUS[self.status])

    class Meta:
        ordering = ['-create_time']
        get_latest_by = 'creation_date'