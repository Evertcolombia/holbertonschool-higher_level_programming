#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = 0
    char_first = ''

    if not sentence:
        tuple_a = (0, None)
    else:
        len_str = len(sentence)
        char_first = sentence[0]
        tuple_a = (len_str, char_first)
        return tuple_a
