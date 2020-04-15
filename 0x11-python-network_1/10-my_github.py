#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]

    res = requests.get(url, auth=(username, password))
    res.raise_for_status()

    try:
        obj = res.json()
        _id = obj['id']
        print(_id)
    except:
        print("None")

