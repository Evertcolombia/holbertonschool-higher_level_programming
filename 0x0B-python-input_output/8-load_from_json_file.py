#!/usr/bin/python3
import json


def load_from_json_file(filename):

    with open(filename, encoding='utf-8') as f:
        a = f.readline()
        data = json.loads(a)
        return data
