#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        print('Body response:')
        print('    - type: {}'.format(str(type(content))))
        print('    - content: {}'.format(str(content)))
        print('    - utf8 content: {}'.format(content.decode('utf-8')))
