#!/usr/bin/python3
"""prints all integers of a list"""


def print_list_integer(my_list=[]):

    for j in range(len(my_list)):
        print("{:d}".format(my_list[j]))
