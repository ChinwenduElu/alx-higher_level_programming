#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contains method is_kind_of_class
returns True if object is an instance of class that it inherited from
"""



def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
