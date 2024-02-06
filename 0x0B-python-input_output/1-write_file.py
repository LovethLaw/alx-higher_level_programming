#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """function writes text to a file if it exists or creats if it doesnt"""
    with open(filename, "w") as file:

        read = file.write(text)
        return read