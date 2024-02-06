#!/usr/bin/python3
"""create json from file"""
import json


def load_from_json_file(filename):
    """creates a json object from a file
        Args:
            filename - the file where obj is stored
    """
    with open(filename, "r") as file:
        file_data = json.load(file)
        return file_data