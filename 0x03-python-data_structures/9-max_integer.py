#!/usr/bin/python3
"""function that finds the biggest integer of a list"""


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > biggest:
            biggest = my_list[j]

    return (biggest)
