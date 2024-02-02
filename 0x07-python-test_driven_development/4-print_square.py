#!/usr/bin/python3
"""This Module contains the function that prints # for the number of size
    Args:
       size(int): number of times # prints
    """
def print_square(size):
    """This function takes in size and prints # for the number of size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)