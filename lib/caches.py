#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.linuxidc.com/Linux/2014-11/109962.htm

import redis
from deadend.settings import REDIS_HOST_DEFAULT, REDIS_PORT_DEFAULT, \
    REDIS_PORT_DEFAULT, REDIS_EXPIRE_DEFAULT


def new_redis_connection_pool(host=REDIS_HOST_DEFAULT,
                              port=REDIS_PORT_DEFAULT,
                              db=REDIS_EXPIRE_DEFAULT,
                              password=''):
    """
    Create a new redis connection pool.
    """
    return redis.ConnectionPool(host=host, port=port, db=db, password=password)
