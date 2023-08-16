#!/usr/bin/python3
""" function that returns the number of keys in a dictionary."""


def number_keys(a_dictionary):
    numb = 0
    roll_keys = list(a_dictionary.keys())

    for j in roll_keys:
        numb += 1

    return (numb)
