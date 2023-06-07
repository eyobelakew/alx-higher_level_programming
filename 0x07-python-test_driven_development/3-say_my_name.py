#!/usr/bin/python3
"""
This module contains the say_my_name method
"""


def say_my_name(first_name, last_name=""):
    """Function that print 'My name is <fist name> <last name>'

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first name is not str, raise TypeError \
            'first_name must be a string'
        TypeError: If last name is not str, raise TypeError \
            'last_name must be a string'
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
