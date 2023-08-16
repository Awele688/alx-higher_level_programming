#!/usr/bin/python3
""" function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    roll_order = list(a_dictionary.keys())
    roll_order.sort()
    for j in roll_order:
        print("{}: {}".format(j, a_dictionary.get(j)))
