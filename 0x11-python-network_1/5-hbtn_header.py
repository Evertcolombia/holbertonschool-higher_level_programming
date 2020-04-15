#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code == 200:
        x_request_id = res.headers['X-Request-Id']
        print(x_request_id)
