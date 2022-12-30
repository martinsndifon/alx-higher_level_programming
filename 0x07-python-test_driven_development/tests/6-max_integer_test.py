#!/usr/bin/python3



"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """A test class for the module '6-max_integer'
    """
    def test_max_integer(self):
        """Checks for correct results in the test
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([12, 24, 35, 4]), 35)
        self.assertEqual(max_integer([-1, 0, -3, -4]), 0)
