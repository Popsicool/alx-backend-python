#!/usr/bin/env python3
'''
Parameterize a unit test
'''
import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    '''
    base class
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, res: int) -> None:
        '''
        test access nested map
        '''
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        '''
        test access nested map exception
        '''
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    Test Get Json class
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, req):
        '''
        Mock HTTP calls
        '''
        req.return_value.json.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        req.assert_called_once_with(test_url)
