#!/usr/bin/python3
"""
    Module implementing a function that returns the peak
    from a list of numbers

"""


def find_peak(list_of_integers):
    """Returns the peak from a list of integers"""
    if not list_of_integers or list_of_integers == []:
        return None
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
