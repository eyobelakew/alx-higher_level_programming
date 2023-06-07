#!/usr/bin/python3
"""
This module contains the add_integer method
"""


def add_integer(a, b=98):
    """
    Return the addition of two numbers

    Args:
        a (int, float): First number.
        b (int, float): Second number.

    Raises:
        TypeError: If a is not integer or float, print 'a must be an integer'.
        TypeError: If b is not integer or float, print 'b must be an integer'.

    Returns:
        int: Sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
