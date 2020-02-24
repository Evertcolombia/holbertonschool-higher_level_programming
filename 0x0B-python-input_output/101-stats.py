#!/usr/bin/python3

import sys
from signal import signal, SIGINT


count, file_size = 0, 0
allowed_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}


def ten_times():

    print("File size: {:d}".format(file_size))

    for key in sorted(allowed_codes.keys()):
        val = allowed_codes.get(key)
        if val != 0:
            print("{}: {:d}".format(key, val))


def handler(signal_received, frame):
    ten_times()
    sys.exit(0)

for line in sys.stdin:

    signal(SIGINT, handler)

    if count == 10:
        ten_times()
        count = 0

    split_line = line.split()
    try:
        if split_line[-2] and split_line[-2] in allowed_codes.keys():
            allowed_codes[split_line[-2]] += 1
    except:
        pass

    try:
        size = int(split_line[-1])
        file_size += size
    except:
        pass

    count += 1

ten_times()
