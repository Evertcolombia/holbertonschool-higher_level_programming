#!/usr/bin/python3
import json

def from_json_string(my_str):
    a = json.dumps(my_str)
    b = json.loads(a)
    return b
