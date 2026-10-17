#!/usr/bin/env python3
"""Task 0: Check if a character is lowercase using ASCII values."""


def islower(c):
    """Returns True if c is a lowercase letter, False otherwise.

    Does not use built-in string methods.
    """
    return 97 <= ord(c) <= 122
