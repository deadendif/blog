#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging
from django.core.management.base import BaseCommand

from blog.caches import EntryActorIpCache
from blog.models import Entry
from blog.settings import BLOG_ENTRY_ACTOR_DELTA, PTN_BLOG_ENTRY_VIEWER, PTN_BLOG_ENTRY_FEEDBACK

logger = logging.getLogger('file')


class Command(BaseCommand):
    """
    Clean expire actor's ip of entry.
    [circle] BLOG_ENTRY_ACTOR_DELTA
    """

    def handle(self, *args, **kwargs):
        deadline = int(time.time()) - BLOG_ENTRY_ACTOR_DELTA
        logger.info('[CleanEntryActorIpCommand.handle] [deadline=%d] Begin cleaning ...' % deadline)
        for entry in Entry.objects.all():
            try:
                EntryActorIpCache(entry, PTN_BLOG_ENTRY_VIEWER).zremrangebyscore(0, deadline)
                EntryActorIpCache(entry, PTN_BLOG_ENTRY_FEEDBACK).zremrangebyscore(0, deadline)
            except Exception, e:
                logger.error('[CleanEntryActorIpCommand.handle] Clean entry [id=%d] except, err: %s' % (entry.id, str(e)))
            else:
                logger.debug('[CleanEntryActorIpCommand.handle] Clean entry [id=%d] success' % entry.id)
        logger.info('[CleanEntryActorIpCommand.handle] [deadline=%d] Clean success' % deadline)

