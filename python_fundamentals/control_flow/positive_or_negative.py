#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
try:
    if number > 0:
        print(f"{number:d} is positive")
    elif number == 0:
        print(f"{number:d} is zero")
    else:
        print(f"{number:d} is negative")
except Exception:
    pass
