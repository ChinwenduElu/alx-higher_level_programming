#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains method inherits_from
returns True if obj is instance of class that it inherits from or is subcls of
"""


def inherits_from(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
