#!/usr/bin/python3
"""
This module contains the print_square method
"""


def print_square(size):
    """Function that print a square.

    Args:
        size (int): is the size length of the square.

    Raises:
        TypeError: if size is a float and is less than 0, \
            raise a TypeError exception with the message \
            size must be an integer.\
            size must be an integer, otherwise raise a TypeError \
            exception with the message size must be an integer.
        ValueError: If size is less than 0, raise a ValueError \
            exception with the message size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
