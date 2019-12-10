#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for char in str:
        ascii_char = ord(char)
        if(ascii_char > 96) and (ascii_char < 123):
            ascii_char -= 32
            str2 += chr(ascii_char)
        elif ascii_char > 64 and ascii_char < 91:
            str2 += chr(ascii_char)
        elif ascii_char == 32:
            str2 += chr(ascii_char)
        elif ascii_char > 47 and ascii_char < 58:
            str2 += chr(ascii_char)
    print("{}".format(str2), end='')
