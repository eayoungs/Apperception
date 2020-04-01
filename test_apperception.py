#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Classes for Apperception package """

__author__ = "Eric Allen Youngson"
__copyright__ = "Copyright 2020, Apperception"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE"


import pytest
import apperception
# import inspect


test_args = {'param1': 'arg1', 'param2': 2}


@pytest.fixture
def perception_obj():
    return apperception.Perception(**test_args)


@pytest.fixture
def fixture_args():
    return test_args


class TestPerception():
    """docstring for TestPerception"""

    def test_perception(self, perception_obj):
        """docstring for test_perception"""
        assert perception_obj

    def test_perception_instance_parameters(self, perception_obj, fixture_args,
                                            capsys):
        """docstring for test_perception_instance_parameters"""
        # sig = inspect.signature(perception_obj.__init__)
        for key, value in fixture_args.items():
            assert key in vars(perception_obj).keys()
            with capsys.disabled():
                print(key)

    def test_introspect_instance_attribute_types(self, perception_obj,
                                                 fixture_args):
        """docstring for test_get_attribute_types"""
        for key, value in fixture_args.items():
            assert type(value) in [type(var) for var in
                                   vars(perception_obj).values()]
