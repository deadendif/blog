#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.exceptions import InvalidFuncParamException
from .models import Entry


class ModelAdapter(object):
    """
    Adapter of model.
    """

    def __init__(self, model_class):
        self.__model_class = model_class

    def adapt(self, instance_or_id):
        """
        Adapt param.
        """
        if isinstance(instance_or_id, int):
            return self.__model_class.objects.get(id=instance_or_id)
        elif isinstance(instance_or_id, self.__model_class):
            return instance_or_id
        else:
            raise InvalidFuncParamException('Invalid function param, instance_or_id="%s"' % str(instance_or_id))

entry_adapter = ModelAdapter(Entry)