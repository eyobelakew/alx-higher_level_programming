#!/usr/bin/python3
"""
This module contains the matrix_divided method
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Args:
        matrix (list int/float): Must be a list of lists of integers or floats.
        div (int/float): must be a number.

    Raises:
        TypeError: If matrix is not a lits, print 'matrix must be a matrix \
            (list of lists) of integers/floats'.
        TypeError: If a row is not a list, print 'matrix must be a matrix \
            (list of lists) of integers/floats'.
        TypeError: Each row of the matrix must be of the same size, if not \
            print 'Each row of the matrix must have the same size'.
        TypeError: All items in a row must be an integer or floating \
            number, if not, print 'matrix must be a matrix (list of lists) \
            of integers/floats'.
        TypeError: div must be a number (integer or float), \
            otherwise raise a TypeError exception with the message \
            'div must be a number'.
        ZeroDivisionError: div can’t be equal to 0, if not, print \
            'division by zero'.

    Returns:
        list: a new list.
    """
    mtx_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(mtx_error)

    len_row = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtx_error)
        if len_row is None:
            len_row = len(row)
        elif len_row != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(mtx_error)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for item in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), item)))

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
