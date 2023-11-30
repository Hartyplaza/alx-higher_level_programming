#!/usr/bin/python3
"""
    Module function that prints a square
"""


def print_square(size):
    """ Function that prints a square using '#' based on `size`.

    Args:
        size (int): size of one side of the square.
    """

    if type(size) is not int:
        raise TypeError("size must be integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(('#' * size + '\n') * size, end='')
