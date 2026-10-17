#!/usr/bin/env python3
"""Task 5: Import add function from add_0 and print the result."""
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
