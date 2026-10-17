#!/usr/bin/env python3
"""Task 3: Compute a raised to the power of b."""


def pow(a, b):
    """Computes a to the power of b using a loop without ** operator."""
    if b == 0:
        return 1

    result = 1
    exp = b
    is_negative = False

    if b < 0:
        is_negative = True
        exp = -b

    for _ in range(exp):
        result *= a

    if is_negative:
        return 1 / result
    return result
