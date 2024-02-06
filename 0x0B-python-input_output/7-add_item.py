#!/usr/bin/python3
"""load, add, save"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""script adds all arguments to a python list,
and then saves to a file"""

try:
    add_1 = load_from_json_file("add_item.json")
    save_to_json_file(add_1 + argv[1:], "add_item.json")
except Exception:
    save_to_json_file(argv[1:], "add_item.json")