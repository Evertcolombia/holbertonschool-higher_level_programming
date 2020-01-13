#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in (':.?'):
        text = text.replace(char, "{}\n\n".format(char))

    text = text.replace('\\', '')
    text = "\n".join([line.strip() for line in text.split('\n')])  
    print(text, end="")
