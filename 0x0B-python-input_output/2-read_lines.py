#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    l = 0
    with open(filename, encoding='utf-8') as f:
            for line in f:
                l += 1
    if nb_lines <= 0 or nb_lines >= l:
        with open(filename, encoding='utf-8') as f:
                print(f.read(), end="")
    else:
        with open(filename, encoding='utf-8') as f:
            for i in range(nb_lines):
                print(f.readline(), end="")
