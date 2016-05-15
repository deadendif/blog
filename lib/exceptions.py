#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InvalidRequestParamException(Exception):
    """
    Request parameter invalid.
    """
    def __init__(self, e='Request param is invalid'):
        super(InvalidRequestParamException, self).__init__(e)


class InvalidCounterTypeException(Exception):
    """
    Counter key invalid.
    """
    def __init__(self, e='Counter type is invalid'):
        super(InvalidCounterTypeException, self).__init__(e)


class InvalidFuncParamException(Exception):
    """
    Function parameter invalid.
    """
    def __init__(self, e='Function param is invalid'):
        super(InvalidFuncParamException, self).__init__(e)


class OperationTooFrequentException(Exception):
    """
    Operation is too frequent.
    """
    def __init__(self, e="Operation is too frequent"):
        super(OperationTooFrequentException, self).__init__(e)
