#!/usr/bin/env python3
"""Task 1: Print a string in uppercase using ASCII conversions."""


def uppercase(str):
    """Prints a string in uppercase followed by a new line,

    without using the .upper() method, using ord() and chr().
    """
    result = ""
    for c in str:
        code = ord(c)
        # Si el carácter es una minúscula (entre 'a' y 'z' en ASCII: 97 a 122)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += c
    print("{}".format(result))
