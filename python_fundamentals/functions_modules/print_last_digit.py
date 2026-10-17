#!/usr/bin/env python3
"""Task 2: Print and return the last digit of a number."""


def print_last_digit(number):
    """Prints and returns the last digit of number (always positive)."""
    if number < 0:
        last_digit = abs(number) % 10
    else:
        last_digit = number % 10

    print("{}".format(last_digit), end="")
    return last_digit
