#!/usr/bin/python3
"""function that finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):

    multis = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            multis.append(True)
        else:
            multis.append(False)

    return (multis)
