#!/usr/bin/python3

import sys

def ten_times(file_size, allowed_codes):

    print("File size: {:d}".format(file_size))

    for key in sorted(allowed_codes.keys()):
        val = allowed_codes.get(key)
        if val != 0:
            print("{}: {:d}".format(key, val))

allowed_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

count = 0
file_size = 0

try:
    for line in sys.stdin:

        if count == 10:
            ten_times(file_size, allowed_codes)
            count = 0

        split_line = line.split()
        if split_line[7] and type(split_line[8]) != int:
            status_code = split_line[7]
            file_size += int(split_line[8])

        if status_code in allowed_codes.keys():
            allowed_codes[status_code] += 1

        count += 1

    ten_times(file_size, allowed_codes)
except KeyboardInterrupt:
    ten_times(file_size, allowed_codes)
    raise
