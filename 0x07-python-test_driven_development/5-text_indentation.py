#!/usr/bin/python3


"""This module contains a function that does a text indentation.
   Args:
       text (str): this is the string represntation for which
       indentation is to be done.
"""


def text_indentation(text):
    """This function indents the text string based on the delimeters.
       Returns: None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in text:
        if ch == '.' or ch == ':' or ch == '?':
            print("{}".format(ch), end='')
            print("\n")
        else:
            print("{}".format(ch), end='')
