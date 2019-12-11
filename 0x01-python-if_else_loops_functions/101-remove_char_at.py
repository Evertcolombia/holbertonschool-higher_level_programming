#!/usr/bin/python3
def remove_char_at(str, n):
    strlen = len(str) - 1
    strCopy = ""
    for i in range(0, strlen + 1):
        if i != n:
            strCopy += str[i]
    return strCopy
