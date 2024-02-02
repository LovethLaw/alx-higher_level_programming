#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    def test_is_equal(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        
    def test_negative(self):
        self.assertEqual(max_integer([-1, -3, -4]), -1)

    def test_large(self):
        self.assertEqual(max_integer([40, 90, 87, 78]), 90)

    def test_valid_data_types(self):
        self.assertIsInstance(max_integer([90, 98, 0.5, 4.67]), (int, float))

    def test_emptylist(self):
        self.assertIsNone(max_integer([]), None)

    def test_notnone(self):
        self.assertIsNotNone(max_integer([90]), None)

    def test_invalidinstance(self):
        self.assertNotIsInstance(max_integer(['w', 'i,', 'c']), (int, float))

    def test_sameobject(self):
        self.assertIs(max_integer([30, 70, 89]), max_integer([30, 70, 89]))

    def test_differentobject(self):
        self.assertIsNot(max_integer([59, 76]), max_integer([89, 34]))

    def test_invalidargument(self):
        self.assertRaises(TypeError, max_integer((67, 90)))

    def test_assertionerror(self):
        self.assertRaises(TypeError, max_integer('e'))
        

if __name__ == "__main__":
    unittest.main()