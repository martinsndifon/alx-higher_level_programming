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

    def test_max_float(self):
        self.assertEqual(max_integer([7.2, 19.27, 77.46, 11.5]), 77.46)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_non_number(self):
        with self.assertRaises(TypeError):
            max_integer([2, 1, "max", "integer"])

if __name__ == "__main__":
    unittest.main()
