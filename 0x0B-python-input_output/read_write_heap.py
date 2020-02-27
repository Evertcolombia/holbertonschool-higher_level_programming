#!/usr/bin/python3

import ctypes
import os
import re
import sys

PTRACE_ATTACH = 16
PTRACE_DETACH = 17


def default_ptrace(attach, pid):

    libc = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6')
    libc.ptrace.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p]
    err = libc.ptrace(attach, int(pid), None, None)

    #if err != 0:
     #   raise SystemError('ptrace', err)


if len(sys.argv) == 4:

    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    default_ptrace(PTRACE_ATTACH, pid)

    with open('/proc/' + pid + '/maps', 'r') as maps:
        print(maps.read())
        maps_list = maps.read()
        #Here you need a regex to get the memory adress for the heap
       

    default_ptrace(PTRACE_DETACH, pid)
else:
    print('Error')

