#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging
from django.core.management.base import BaseCommand

from blog.caches import EntryActorCache
from blog.models import Entry
from blog.settings import BLOG_ENTRY_ACTOR_DELTA, PTN_BLOG_ENTRY_VIEWER, PTN_BLOG_ENTRY_FEEDBACK

logger = logging.getLogger('offline')


class Command(BaseCommand):
    """
    Clean expire actor's key of entry.
    [circle] BLOG_ENTRY_ACTOR_DELTA
    [ps] Redis can't set expiration time to element of zset, so I use this command to clean in cycle.
    """

    def handle(self, *args, **kwargs):
        deadline = int(time.time()) - BLOG_ENTRY_ACTOR_DELTA
        logger.info('[CleanEntryActorIpCommand.handle] [deadline=%d] Begin cleaning ...' % deadline)
        for entry in Entry.objects.all():
            try:
                EntryActorCache(entry, PTN_BLOG_ENTRY_VIEWER).zremrangebyscore(0, deadline)
                EntryActorCache(entry, PTN_BLOG_ENTRY_FEEDBACK).zremrangebyscore(0, deadline)
            except Exception, e:
                logger.error('[CleanEntryActorIpCommand.handle] Clean entry [id=%d] except, err: %s' % (entry.id, str(e)))
            else:
                logger.debug('[CleanEntryActorIpCommand.handle] Clean entry [id=%d] success' % entry.id)
        logger.info('[CleanEntryActorIpCommand.handle] [deadline=%d] Clean success' % deadline)

