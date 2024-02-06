#!/usr/bin/python3
"""adds attribute"""


def add_attribute(obj, attribute, value):
    """adds attribute to an object"""

    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")