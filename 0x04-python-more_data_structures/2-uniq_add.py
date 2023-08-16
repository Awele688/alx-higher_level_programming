#!/usr/bin/python3
""" adds all unique integers in a list (only once for each integer)."""


def uniq_add(my_list=[]):
    unique_list = set(my_list)
    numb = 0

    for j in unique_list:
        numb += j

    return (numb)
