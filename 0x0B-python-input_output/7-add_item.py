#!/usr/bin/python3
"""
    A script that adds all arguments to a Python list, and then save them to a file:
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
data = sys.argv

new_data = data[1:]
filename = "add_item.json"

data2 = save_to_json_file(new_data,filename)
load_from_json_file(filename)
