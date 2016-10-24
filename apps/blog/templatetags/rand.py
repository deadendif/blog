#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import glob
import random
import logging
from django import template
from django.conf import settings

register = template.Library()

logger = logging.getLogger('online')


@register.simple_tag(name='randBackground')
def randBackground():
    try:
        pattern = os.path.join(settings.STATIC_ROOT, settings.RANDOM_BACKGROUND_IMAGES)
        logger.info(pattern)
        images = [os.path.join(os.path.dirname(settings.RANDOM_BACKGROUND_IMAGES), os.path.basename(i)) 
                for i in glob.glob(pattern)]
        return images[int(time.strftime('%d')) % len(images)]
        # return random.choice(images)
    except Exception, e:
        logger.error(str(e))
        return ''
