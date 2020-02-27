#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

count = 0

while True:
    sleep(random.random())
    sys.stdout.write("[{:d}] Holberton \n".format(count))
    count += 1
    sys.stdout.flush()
