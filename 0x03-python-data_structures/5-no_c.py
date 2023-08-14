#!/usr/bin/python3
"""removes all characters c and C from a string."""


def no_c(my_string):

    cpy = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(cpy))
