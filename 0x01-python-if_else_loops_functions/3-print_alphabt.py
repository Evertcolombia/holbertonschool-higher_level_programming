#!/usr/bin/python3
i = 97
for i in range(i, 123):
    if (chr(i) != "e") and (chr(i) != "q"):
        print("{}".format(chr(i)), end='')
