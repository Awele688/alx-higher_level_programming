#!/usr/bin/python3
# fizzbuzz.py

"""function that prints the numbers from 1 to 100 separated by a space.
For multiples of three print Fizz instead of a number
and for multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz."""


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(num), end=" ")
