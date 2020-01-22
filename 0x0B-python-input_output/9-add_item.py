#!/usr/bin/python3
import sys
import os.path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

lenght = len(sys.argv)
file_name = "add_item.json"

if not os.path.exists(file_name):
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write("[]")

python_file = load_from_json_file(file_name)
