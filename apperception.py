#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Classes for Apperception package """

__author__ = "Eric Allen Youngson"
__copyright__ = "Copyright 2020, Apperception"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE"


# https://github.com/python/cpython/blob/3.8/Lib/collections/__init__.py
from collections import ChainMap


class Perception(object):
    """docstring for Perception"""
    def __init__(self, **kwargs):
        super(Perception, self).__init__()
        self.__dict__.update(kwargs)


class Apperception(ChainMap):
    """docstring for Apperception"""
    def __init__(self, *perceptions):
        super(Apperception, self).__init__()
        for perception in perceptions:
            self.perception = perception
