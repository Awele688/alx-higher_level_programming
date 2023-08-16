#!/usr/bin/python3
"""replaces all occurrences of an element by another in a new list."""


def search_replace(my_list, search, replace):
    novel_list = list(map(lambda x: replace if x == search else x, my_list))
    return (novel_list)
