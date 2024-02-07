#!/usr/bin/python3

"""This module contains a function that saves commmand line
   arguments to a JSON object file.
"""

import json
import sys

# save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
# load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def save_to_json_file(my_obj, filename):
    """This function writes and saves a JSON object to a file.
       Args:
           my_obj (any): JSON object to be serialized.
           filename (any): This represents the file to be written to.
    """
    with open(filename, "w") as the_file:
        return the_file.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """This creates an object from a JSON file and returns the object
       Args:
           filename (any): this represents the JSON file to be read
       Returns:
           The JSON object read from the file.
    """

    with open(filename, "r") as the_file:
        json_object = json.load(the_file)

        return json_object


def add_arguments(json_file, *args):
    """This function saves the command line arguments in a JSON file
       Args:
           json_file (any): this represents the JSON file.
           *args (any): this represnts the command line arguments to serialied
    """

    command_line_list = list(args)

    try:
        obj_list = load_from_json_file(json_file)
    except FileNotFoundError:
        obj_list = []  # list is set to be empty if file wasn't created.

    file_obj_list = obj_list + command_line_list

    save_to_json_file(file_obj_list, json_file)


command_args = sys.argv[1:]
json_filename = "add_item.json"

add_arguments(json_filename, *command_args)
