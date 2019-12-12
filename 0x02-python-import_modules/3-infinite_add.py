#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    lenArgv = len(sys.argv)
    res = 0
    if lenArgv == 1:
        print(0)
    else:
        for i in range(1, lenArgv):
            res += int(sys.argv[i])
        print(res)
