#!/usr/bin/python3
""" deletes keys with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    roll_keys = list(a_dictionary.keys())

    for val_dict in roll_keys:
        if value == a_dictionary.get(val_dict):
            del a_dictionary[val_dict]

    return (a_dictionary)
