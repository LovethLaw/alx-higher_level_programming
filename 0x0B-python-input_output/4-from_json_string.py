#!/usr/bin/python3
"""module contains function to for deserialization"""
import json


def from_json_string(my_str):
    """deserializes a json object back to a python data structure
        Args:
            my_str: the json string to be deserialized
        Returns: an object (python data structure)
    """
    obj = json.loads(my_str)
    return obj