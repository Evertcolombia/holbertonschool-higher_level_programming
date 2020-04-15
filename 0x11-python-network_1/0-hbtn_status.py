#!/usr/bin/python3
from urllib import request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()

        res_headers = [['type', str(type(content))],
            ['content', str(content)],
            ['utf8 content', content.decode('utf-8')]]

        print('Body Response:')
        for el in res_headers:
            print('    - {}: {}'.format(el[0], el[1]))
