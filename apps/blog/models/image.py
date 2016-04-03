#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid

from django.db import models
from django.utils import timezone

from blog.settings import UPLOAD_IMAGE_TO
from entry import Entry


def upload_image_to(filename):
    now = timezone.now()
    filename, extension = os.path.splitext(filename)
    path = os.path.join(UPLOAD_IMAGE_TO, now.strftime('%Y/%m/%d'), 
            '%s.%s' % (str(uuid.uuid4()), extension))
    return path


class Image(models.Model):
    """
    Image in entry
    """
    image_caption = models.TextField('image caption',
            blank=True,
            help_text='Image\' caption.')
    image = models.ImageField('image',
            blank=True, upload_to=upload_image_to,
            help_text='Used in entry.')
    entry = models.ForeignKey(
            Entry, related_name='images',
            help_text='Entry that contains this image.')