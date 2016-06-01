#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import redis
import logging
from lib.exceptions import InvalidCounterTypeException, InvalidFuncParamException
from .pool import BLOG_REDIS_CONN_POOL
from ..models import EntryCounter
from ..adapters import entry_adapter
from .. import settings
from ..settings import PTN_BLOG_ENTRY_VIEWER

logger = logging.getLogger('online')


class EntryCounterCache(object):
    """
    Cache entry counter.
    """

    def __init__(self, entry_or_id):
        self.__r = redis.StrictRedis(connection_pool=BLOG_REDIS_CONN_POOL)
        self.__pipe = None
        self.__expire = settings.REDIS_EXPIRE_BLOG_ENTRY_COUNTER
        self.__entry = entry_adapter.adapt(entry_or_id)
        self.__map = {
            'page_view_num': settings.PTN_BLOG_ENTRY_COUNTER_PV,
            'useful_num'   : settings.PTN_BLOG_ENTRY_COUNTER_UF,
            'useless_num'  : settings.PTN_BLOG_ENTRY_COUNTER_UL
        }

    @property
    def entry(self):
        return self.__entry

    @property
    def pipe(self):
        if self.__pipe is None:
            self.__pipe = self.__r.pipeline()
        return self.__pipe

    def get_key(self, ctype):
        key = self.__map.get(ctype, None)
        if key is None:
            raise InvalidCounterTypeException(
                'Invalid type of entry counter, type="%s"' % str(ctype))
        else:
            key = key % self.entry.id
        return key

    def get(self, ctype):
        """
        Get count number according to ctype.
        """
        key = self.get_key(ctype)
        count = self.__r.get(key)
        if count is None:
            count = getattr(EntryCounter.objects.get(entry=self.entry), ctype)
            self.__r.setex(key, self.__expire, count)
        return count

    def set(self, ctype, val):
        """
        Set count number according to ctype. 
        """
        key = self.get_key(ctype)
        self.__r.setex(key, self.__expire, val)

    def incr(self, ctype, delta=1):
        """
        Increase count number.
        """
        key = self.get_key(ctype)
        self.__r.incr(key, delta)

    def delete(self):
        """
        Delete all counters of the entry.
        """
        self.__r.delete(*(tuple([ptn % self.entry.id for ptn in self.__map.values()])))


class EntryActorIpCache(object):
    """
    Cache ip of entry's actor.
    """

    def __init__(self, entry_or_id, pattern):
        self.__r = redis.StrictRedis(connection_pool=BLOG_REDIS_CONN_POOL)
        self.__expire = settings.REDIS_EXPIRE_BLOG_ENTRY_VIEWER
        self.__entry = entry_adapter.adapt(entry_or_id)
        self.__key = pattern % self.__entry.id

    @property
    def entry(self):
        return self.__entry

    @property
    def key(self):
        return self.__key

    def add(self, ip):
        """
        Add ip to zset, score is added time.
        """
        self.__r.zadd(self.key, int(time.time()), ip)

    def exists(self, ip):
        """
        Whether ip cannot contribute a page view.
        """
        last_time = self.__r.zscore(self.key, ip)
        if last_time is None or int(last_time) < int(time.time()) - settings.BLOG_ENTRY_ACTOR_DELTA:
            return False
        return True

    def zremrangebyscore(self, min_score, max_score):
        """
        Remove members whose socre between min_score and max_score.
        """
        self.__r.zremrangebyscore(self.key, min_score, max_score)

    def delete(self):
        """
        Delete actor's ips of the entry.
        """
        self.__r.delete(self.__key)

