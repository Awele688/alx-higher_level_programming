#!/usr/bin/python3
# print_alphabt.py

"""prints the ASCII alphabet, in lowercase, not followed by a new line."""

for alpha in range(97, 123):
    if chr(alpha) != 'q' and chr(alpha) != 'e':
        print("{}".format(chr(alpha)), end="")
