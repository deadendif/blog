#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from lib.exceptions import InvalidCounterTypeException, InvalidFuncParamException
from .pool import BLOG_REDIS_CONN_POOL
from ..models import EntryCounter
from ..adapters import entry_adapter
from .. import settings
from ..settings import COUNTER_PAGE_VIEW_PTN, COUNTER_USEFUL_PTN, COUNTER_USELESS_PTN


class EntryCounterCache(object):
    """
    Entry counter cache class.
    """

    def __init__(self, entry_or_id):
        self.__r = redis.StrictRedis(connection_pool=BLOG_REDIS_CONN_POOL)
        self.__expire = settings.REDIS_EXPIRE_BLOG
        self.__entry = entry_adapter.adapt(entry_or_id)
        self.__map = {
            'page_view_num': COUNTER_PAGE_VIEW_PTN,
            'useful_num': COUNTER_USEFUL_PTN,
            'useless_num': COUNTER_USELESS_PTN
        }

    @property
    def entry(self):
        return self.__entry

    def get(self, ctype):
        """
        Return count number according to ctype.
        """
        key = self.__map.get(ctype, None)
        if key is None:
            raise InvalidCounterTypeException('Invalid type of entry counter, type="%s"' % str(ctype))
        else:
            key = key % str(self.entry.id)

        count = self.__r.get(key)
        if count is None:
            count = getattr(EntryCounter.objects.get(entry=self.entry), ctype)
            self.__r.setex(key, self.__expire, count)
        return count

    def set(self, ctype, val):
        key = self.__map.get(ctype, None)
        if key is None:
            raise InvalidCounterTypeException('Invalid type of entry counter, type="%s"' % str(ctype))
        else:
            key = key % str(self.entry.id)
        self.__r.setex(key, self.__expire, val)
