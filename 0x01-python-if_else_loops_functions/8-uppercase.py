#!/usr/bin/python3
# uppercase.py

"""function that prints a string in uppercase followed by a new line"""


def uppercase(str):
    result = ""
    for b in str:
        if ord(b) >= 97 and ord(b) <= 122:
            b = chr(ord(b) - 32)
        result += b
    result += "\n"
    return result
