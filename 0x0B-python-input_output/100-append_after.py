#!/usr/bin/python3
"""Appends after"""


def append_after(filename="", search_string="", new_string=""):
    """appends after a search string"""
    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as my_file:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string

        my_file.write(s)