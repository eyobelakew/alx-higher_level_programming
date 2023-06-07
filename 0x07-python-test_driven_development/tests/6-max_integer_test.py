#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_module_docstring(self):
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_max_at_the_end(self):
        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

    def test_max_at_the_beginning(self):
        result = max_integer([3, 2, 1])
        self.assertEqual(result, 3)

    def test_max_in_the_middle(self):
        result = max_integer([1, 2, 3, 1, 2])
        self.assertEqual(result, 3)

    def test_one_negative_number_in_the_list(self):
        result = max_integer([1, 2, 3, -1, 2])
        self.assertEqual(result, 3)

    def test_only_negative_numbers(self):
        result = max_integer([-11, -22, -33, -1, -2])
        self.assertEqual(result, -1)

    def test_list_of_one_element(self):
        result = max_integer([3])
        self.assertEqual(result, 3)

    def test_list_is_element(self):
        result = max_integer([])
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
