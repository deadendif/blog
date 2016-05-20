#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from .app import app

logger = logging.getLogger('file')


class BaseTask(app.Task):

    abstract = True

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        super(BaseTask, self).on_retry(exc, task_id, args, kwargs, einfo)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)
        logger.error('[%s] [task_id=%s] [args=%s] [kwargs=%s] Run task except, err: %s' \
            % (self.name, task_id, str(args), str(kwargs), str(exc)))

    def on_success(self, retval, task_id, args, kwargs):
        super(BaseTask, self).on_success(retval, task_id, args, kwargs)
        