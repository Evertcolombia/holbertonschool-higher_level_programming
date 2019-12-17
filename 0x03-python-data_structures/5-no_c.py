#!/usr/bin/python3
def no_c(my_string):
    if (my_string):
        new = ""
        for char in my_string:
            if (char == 'C') or (char == 'c'):
                my_string.replace(char, '')
            else:
                new = new + new.join(char)
        return new
