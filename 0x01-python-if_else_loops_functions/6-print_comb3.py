#!/usr/bin/python3
for num in range(0, 9):
    for num1 in range(num + 1, 10):
        if num == 8:
            print("{:d}{:d}".format(num, num1))
        else:
            print("{:d}{:d}". format(num, num1), end=', ')
