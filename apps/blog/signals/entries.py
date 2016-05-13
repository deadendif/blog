#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from ..models import Entry, EntryCounter


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
    Delete the counter before a new entry is deleted.
    PS: Cannot find the counter to delete if the entry is delete first.
    """
    EntryCounter.objects.get(entry=instance).delete()
