#!/usr/bin/python3
def add_integer(a, b=99):
    """
    A function that adds Two integers

    Args:
        a (int): First operand
        b (int): Secound operand
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
