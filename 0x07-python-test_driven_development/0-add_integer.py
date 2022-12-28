#!/usr/bin/python3
"""
Module 0-add_integer
Function that adds 2 integers
Accepts two values (int or float) but casts float to int before summation
"""


def add_integer(a, b=98):
    """
    Returns sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
