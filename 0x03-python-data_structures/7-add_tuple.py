#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = [0, 0]
    if (tuple_a):
        if len(tuple_a) == 2:
            for i in range(2):
                if tuple_a[i]:
                    new[i] += tuple_a[i]
        if len(tuple_a) == 1:
            new[0] += tuple_b[0]

    if (tuple_b):
        if len(tuple_b) == 2:
            for i in range(len(tuple_b)):
                if tuple_b[i]:
                    new[i] += tuple_b[i]
        if len(tuple_b) == 1:
                    new[0] += tuple_b[0]

    new = tuple(new)
    return new
