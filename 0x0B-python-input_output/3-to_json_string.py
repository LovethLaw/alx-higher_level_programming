#!/usr/bin/python3
"""module contains function to serialize python data structure"""
import json


def to_json_string(my_obj):
    """converts ojb string to json
    Args:
        my_obj: The object string to be converted
    Return: JSON representation of the object string
    """
    json_obj = json.dumps(my_obj)
    return json_obj