#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
    print("Body response:")

    headers = [["type", type(content)], ["content", content],
                ["utf8 content", content.decode()]]
    for el in headers:
        print("\t- {}: {}".format(el[0], el[1]))
    #print("\t- type: {}".format(type(content)))
    #print("\t- content: {}".format(content))
    #print("\t- utf8 content: {}".format(content.decode()))
