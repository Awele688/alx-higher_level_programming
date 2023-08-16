#!/usr/bin/python3
""" returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    novel_dir = a_dictionary.copy()
    roll_keys = list(novel_dir.keys())

    for j in roll_keys:
        novel_dir[j] *= 2

    return (novel_dir)
