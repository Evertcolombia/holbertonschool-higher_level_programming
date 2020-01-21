#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            for line in f:
                print(line)
#           for line in f:
           # a = f.readline(nb_lines)
            #print(a)
