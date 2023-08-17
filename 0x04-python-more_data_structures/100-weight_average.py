#!/usr/bin/python3
"""returns the weighted average of all
integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    numb = 0
    de = 0

    for tupl in my_list:
        numb += tupl[0] * tupl[1]
        de += tupl[1]

    return (numb / de)
