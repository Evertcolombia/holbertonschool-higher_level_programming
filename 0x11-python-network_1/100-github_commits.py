#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1]))

    obj = res.json()
    for el in obj[:10]:
        sha = el.get('sha')
        author = el.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))

