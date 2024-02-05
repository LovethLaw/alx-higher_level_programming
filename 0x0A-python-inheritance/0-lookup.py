#!/usr/bin/python3
""" defines an object attribute lookup fucntion. """
def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))