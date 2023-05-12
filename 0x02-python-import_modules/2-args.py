#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif argc == 1:
        print("Number of argument(s): 1.")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {}.".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
