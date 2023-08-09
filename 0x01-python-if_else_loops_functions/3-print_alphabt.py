#!/usr/bin/python3
# print_alphabt.py

"""prints the ASCII alphabet, in lowercase, not followed by a new line."""

for alpha in range(97, 123):
    if chr(alpha) is not 'q' and chr(alpha) is not 'e':
        print("{}".format(chr(alpha)), end="")
