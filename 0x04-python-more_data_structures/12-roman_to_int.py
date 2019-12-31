#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    num_len = len(roman_string)
    romans = [
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
    ]

    if roman_string is None:
        return 0

    if num_len == 1:
        new = [x for x in romans if roman_string[0] in x][0]
        result += new[1]
        return result

    for i in range(num_len - 1):
        for j in range(len(romans)):
            if roman_string[i] == romans[j][0]:
                if roman_string[i] == "I":
                    if roman_string[i + 1] != "I":
                        new = [x for x in romans if roman_string[i+1] in x][0]
                        result += new[1]
                        result -= 1
                    else:
                        result += 2
                else:
                    result += romans[j][1]
    return result
