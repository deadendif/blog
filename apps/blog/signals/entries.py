#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from ..models import Entry, EntryCounter
from ..caches import EntryCounterCache, EntryActorIpCache
from ..settings import PTN_BLOG_ENTRY_VIEWER, PTN_BLOG_ENTRY_FEEDBACK

logger = logging.getLogger('online')

@receiver(post_save, sender=Entry)
def create_entry_counter(sender, instance, created, **kwargs):
    """
    Create the counter after a new entry is created.
    """
    if created:
        EntryCounter.objects.create(entry=instance)


@receiver(pre_delete, sender=Entry)
def delete_entry_counter(sender, instance, **kwargs):
    """
    Delete the caches and counters before a new entry is deleted.
    PS: Cannot find the counter to delete if the entry is delete first.
    """
    try:
        EntryCounterCache(instance).delete()
        EntryActorIpCache(instance, PTN_BLOG_ENTRY_VIEWER).delete()
        EntryActorIpCache(instance, PTN_BLOG_ENTRY_FEEDBACK).delete()
        EntryCounter.objects.get(entry=instance).delete()
    except Exception, e:
        logger.error('%s' % str(e))

