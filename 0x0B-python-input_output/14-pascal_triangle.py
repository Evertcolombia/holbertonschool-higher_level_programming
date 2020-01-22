#!/usr/bin/python3
def pascal_triangle(n):
    new = []
    tr = [[]]

    for i in range(n):
        new = []
        size = i + 1
        if i == 0:
            new.append(1)
            tr[i] = new
            continue
        for j in range(size - 1):
            if j == 0 or j == size:
                new.append(1)
                continue
            #else:
                #new.append(a)
                #tr.append(new)j
            print(i)
