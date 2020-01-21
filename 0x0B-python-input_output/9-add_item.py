#!/usr/bin/python3
import sys
save_to__json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

add_list = []
length = len(sys.argv)
file_name = "add_item.json"

if length >= 2:

    try:
        file_python = load_from_json_file(file_name)
        for i in range(length):
            add_list[i] = sys.argv[i]
        file_json = save_to_json_file(add_list, file_python)
        load_from_json_file(file_json)
    except:
        pass
