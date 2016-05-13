#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.caches import new_redis_connection_pool
from ..settings import REDIS_DB_BLOG


""" Blog reids connection pool """
BLOG_REDIS_CONN_POOL = new_redis_connection_pool(db=REDIS_DB_BLOG)