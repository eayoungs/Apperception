#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Classes for Apperception package """

__author__ = "Eric Allen Youngson"
__copyright__ = "Copyright 2020, Apperception"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE"


class Perception(object):
    """docstring for Perception"""
    def __init__(self, **kwargs):
        super(Perception, self).__init__()
        self.__dict__.update(kwargs)

    def introspect_instance_attribute_types(self):
        """docstring for introspect"""
        attributes = vars(self)
        attribute_types = {}
        for attribute in attributes:
            attribute_types = {
                {attribute.key(): type(attribute.value())}
                for attribute_type in attribute
            }

        return attribute_types
