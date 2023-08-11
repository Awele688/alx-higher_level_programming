#!/usr/bin/python3
""" prints the result of the addition of all arguments"""

if __name__ == "__main__":

    import sys

    gross = 0
    for j in range(len(sys.argv) - 1):
        gross += int(sys.argv[j + 1])
    print("{}".format(gross))
