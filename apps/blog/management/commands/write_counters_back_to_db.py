#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from redis import WatchError
from django.core.management.base import BaseCommand

from blog.caches import EntryCounterCache
from blog.models import EntryCounter
from blog.settings import PTN_BLOG_ENTRY_COUNTER_PV
from blog.settings import PTN_BLOG_ENTRY_COUNTER_UF
from blog.settings import PTN_BLOG_ENTRY_COUNTER_UL


logger = logging.getLogger('file')


class Command(BaseCommand):
    """
    Write counter in redis back to database.
    [circle] arbitrary
    """
    def handle(self, *args, **kwargs):
        logger.info('[WriteCountersBackToDbCommand.handle] Begin synchronizing ...')
        for (entry_id, ) in EntryCounter.objects.values_list('entry_id'):
            tried_times = 0
            try:
                fields = ['page_view_num', 'useful_num', 'useless_num']
                counter = EntryCounterCache(entry_id)
                while tried_times < 3:
                    try:
                        kwargs = {field: counter.get(field) for field in fields}
                        EntryCounter.objects.filter(entry_id=entry_id).update(**kwargs)
                    except Exception, e:
                        logger.warning('[WriteCountersBackToDbCommand.handle] [entry_id=%d] synchronization except, err: %s. Retry now ...' % (entry_id, str(e)))
                    else:
                        logger.debug('[WriteCountersBackToDbCommand.handle] [entry_id=%d] synchronization done' % entry_id)
                        break
                else:
                    logger.error('[WriteCountersBackToDbCommand.handle] [entry_id=%d] synchronization failure')
            except Exception, e:
                logger.error('[WriteCountersBackToDbCommand.handle] [entry_id=%d] synchronization except, err: %s' % (entry_id, str(e)))
        logger.info('[WriteCountersBackToDbCommand.handle] synchronization done')
