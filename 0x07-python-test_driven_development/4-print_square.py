#!/usr/bin/python3
"""
Module 4-print_square
This module is composed by a function that prints a square with the character #
Size must me int
"""


def print_square(size):
    """
    Prints square with #'s
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
