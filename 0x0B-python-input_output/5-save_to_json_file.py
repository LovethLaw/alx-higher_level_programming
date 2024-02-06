#!/usr/bin/python3
"""saves an object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Function saves an object to file using the json interpreter
        Args:
            my_obj - the object to be saved
            filename - the file in which the object will be saved to
    """
    with open(filename, "w") as file:

        json.dump(my_obj, file)