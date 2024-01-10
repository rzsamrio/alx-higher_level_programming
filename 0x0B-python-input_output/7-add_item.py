#!/usr/bin/python3
""" Adds all command line arguments to a Python List
    And saves the list as a json file"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    with open("add_items.json", 'r') as f:
        pass
except FileNotFoundError:
    with open("add_items.json", 'w') as f:
        f.write("[]")

argc = len(sys.argv)
json_data = load_from_json_file("add_items.json")
for i in range(1, argc):
    json_data.append(sys.argv[i])
save_to_json_file(json_data, "add_items.json")
