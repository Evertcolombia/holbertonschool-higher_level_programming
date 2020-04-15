#!/usr/bin/python3
import requests
from sys import argv
import json

if __name__ == "__main__":
    #st = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    #url = st.format(username, repo_name)
    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1]))

    try:
        obj = res.json()
        for el in obj[0:10]:
            sha = el.get('sha')
            author = el('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except:
        print("None")

