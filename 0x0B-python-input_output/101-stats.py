#!/usr/bin/python3

import sys

allowed_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0, 
    '403': 0, '404': 0, '405': 0, '500': 0
}

count = 0
file_size = 0

for line in sys.stdin:

    count += 1

    split_line = line.split()
    status_code = split_line[7]
    file_size += int(split_line[8])

    if status_code in allowed_codes.keys():
        allowed_codes[status_code] += 1

    if count == 10:
        count = 0
        print("File size: {}".format(file_size))

        for key in sorted(allowed_codes.keys()):
            val = allowed_codes.get(key)
            if val != 0:
                print("{}: {}".format(key, val))
