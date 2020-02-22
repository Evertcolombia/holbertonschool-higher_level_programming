#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):

    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='UTF-8') as f:
        for line in lines:
            if search_string in line:
                line = line + new_string
            f.write(line)
