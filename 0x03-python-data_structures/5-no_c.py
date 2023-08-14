#!/usr/bin/python3
"""removes all characters c and C from a string."""


def no_c(my_string):

    cpy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(cpy))
