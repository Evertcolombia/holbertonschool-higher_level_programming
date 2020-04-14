#!/usr/bin/python3
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = request.Request(url)
    try
        with request.openurl(req) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
