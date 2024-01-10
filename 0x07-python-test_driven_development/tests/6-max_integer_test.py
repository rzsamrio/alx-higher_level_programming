#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Testfunction(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer("Str"))
        self.assertRaises
    def test_val(self):
        self.assertAlmostEqual(max_integer([1, 5, 9, 24, 2, 6]), 24)
        self.assertAlmostEqual(max_integer([1, 5, 2, 6, 9]), 9)
        self.assertAlmostEqual(max_integer([-1, -7, -11]), -1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([0]), 0)
