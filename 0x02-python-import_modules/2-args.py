#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    lenArgv = len(sys.argv)
    num = 1
    if lenArgv > 1:
        if lenArgv == 2:
            print('1 argument:')
            print("1: {}".format(sys.argv[1]))
        else:
            print("{} arguments:".format(lenArgv - 1))
            while num < lenArgv:
                print("{:d}: {}".format(num, sys.argv[num]))
                num += 1
    else:
        print('0 arguments.')
