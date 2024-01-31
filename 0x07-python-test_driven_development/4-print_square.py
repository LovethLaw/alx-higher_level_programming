#!/usr/bin/python3
""" This module prints square with a particlar size
    Paramters:
        size: the size of the square
"""


def print_square(size):
    """ Prints square of of size given """

    if not isinstance(size, int):

        raise TypeError("size must be an integer")

    if size < 0:

        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:

        raise TypeError("size must be an integer")

    for row in range(size):

        for col in range(size):

            print("#", end="")

        print()