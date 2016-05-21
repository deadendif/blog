#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging
from django.core.mail import send_mail
from django.conf import settings

from .app import app
from .base import BaseTask
from lib.exceptions import IsSpamException 
from about.models import Email 

logger = logging.getLogger('tasks')


class SendEmailTask(BaseTask):

    name = 'tasks.send_email'
    max_retries = settings.EMAIL_MAX_RETRIES
    default_retry_delay = settings.EMAIL_DEFAULT_RETRY_DELAY
    soft_time_limit = settings.EMAIL_SOFT_TIME_LIMIT

    def _build_content(self, email):
        """
        Build email content.
        """
        def __build_item(key, val):
            return '【%s】:%s' % (str(key), ('\n' if len(str(val)) > 100 else ' ') + str(val))

        fields = ['name', 'address', 'send_time', 'content', 'id', 'ip', 'ua']
        return '\n\n'.join([__build_item(field, getattr(email, field)) for field in fields])

    def _check_spam(self, email):
        """
        Check whether email is spam.
        """
        if email.is_spam is None:
            email.is_spam = False
            Email.objects.filter(id=email.id).update(success=True, is_spam=False)
        return email.is_spam

    def run(self, email_id):
        """
        Run task.
        """
        try:
            logger.info('[%s] [email_id=%d] [retry=%d] Enter' % (self.name, email_id, self.request.retries))
            email = Email.objects.get(id=email_id)
            if self._check_spam(email):
                raise IsSpamException
            send_mail(email.topic, self._build_content(email), settings.EMAIL_HOST_USER, [admin[1] for admin in settings.ADMINS])
            Email.objects.filter(id=email_id).update(success=True)
        except (Email.DoesNotExist, IsSpamException) as e:
            logger.warning('[%s] [email_id=%d] [retry=%d] Run task except, err: %s' % (self.name, email_id, self.request.retries, str(e)))
        except Exception, e:
            logger.warning('[%s] [email_id=%d] [retry=%d] Run task except, err: %s' % (self.name, email_id, self.request.retries, str(e)))
            self.retry(exc=e)
        else:
            logger.info('[%s] [email_id=%d] [retry=%d] Success' % (self.name, email_id, self.request.retries))
