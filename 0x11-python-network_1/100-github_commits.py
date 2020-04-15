#!/usr/bin/python3
import requests
from sys import argv
import json

if __name__ == "__main__":
    repo_name = argv[1]
    username = argv[2]
    st = 'https://api.github.com/repos/{}/{}/commits'
    url = st.format(username, repo_name)

    res = requests.get(url)
    res.raise_for_status()

    print(res.text)
    try:
        obj = res.json()
        for el in obj[0:10]:
            sha = el['sha']
            author = el['commit']['author']['name']
            print("{}: {}".format(sha, author))
    except:
        print("None")

