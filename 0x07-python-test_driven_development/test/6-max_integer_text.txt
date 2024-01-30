#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positvie_elements(self):
        self.assertEqual(max_integer([4, 5, 6, 10]), 10)

    def test_negative_elements(self):
        self.assertEqual(max_integer([-1, -3, -4]), -1)

    def test_large_elements(self):
        self.assertEqual(max_integer([40, 90, 87, 78]), 90)

    def test_valid_instance(self):
        self.assertIsInstance(max_integer([90, 98, 0.5, 4.67]), (int, float))

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_not_none(self):
        self.assertIsNotNone(max_integer([90]), None)

    def test_invalid_instance(self):
        self.assertNotIsInstance(max_integer(['w', 'i,', 'c']), (int, float))

    def test_same_object(self):
        self.assertIs(max_integer([30, 70, 89]), max_integer([30, 70, 89]))

    def test_different_object(self):
        self.assertIsNot(max_integer([59, 76]), max_integer([89, 34]))

    def test_invalid_argument(self):
        self.assertRaises(TypeError, max_integer((67, 90)))

    def test_assertion_error(self):
        self.assertRaises(TypeError, max_integer('e'))
