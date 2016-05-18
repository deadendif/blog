#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Email(models.Model):
    """
    Email model.
    """
    topic = models.CharField('email topic',
        max_length=128, null=False, blank=False,
        help_text='Topic of the email.')
    name = models.CharField('name',
        max_length=32, null=False, blank=False,
        help_text='Name of the sender.')
    address = models.EmailField('address',
        help_text='Email address of the sender.')
    content = models.TextField('content',
        help_text='Email content.')
    ip = models.CharField('IP',
        max_length=64, null=True, blank=True,
        help_text='IP of the sender.')
    ua = models.CharField('user agent',
        max_length=1024, null=True, blank=True,
        help_text="User agent of the sender.")
    send_time = models.DateTimeField('email time',
        default=timezone.now,
        help_text='Datetime when sending email.')
    success = models.BooleanField('success',
        default=False, null=False,
        help_text='Whether send email successfully.')

