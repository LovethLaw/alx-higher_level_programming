#!/usr/bin/python3

""" This module contains class that inherits from a list"""


class MyList(list):
    """ A class that inherits from the list class"""

    def print_sorted(self):
        """Prints he list in sorted order"""

        print(sorted(self))
