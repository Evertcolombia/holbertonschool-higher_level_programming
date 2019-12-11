#!/usr/bin/python3
for num in range(122, 96, -1):
    if num % 2 == 0:
        num = chr(num)
    else:
        num = chr(num - 32)
    print("{}".format(num), end='')
