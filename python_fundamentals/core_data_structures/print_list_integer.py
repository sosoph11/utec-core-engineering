#!/usr/bin/env python3
def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line using {:d}."""
    for item in my_list:
        print("{:d}".format(item))
