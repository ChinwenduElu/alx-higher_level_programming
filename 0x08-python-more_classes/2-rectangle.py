#!/usr/bin/python3
"""
Module 2-rectangle
Contains class Rectangle with private attribute width and height,
and public area and perimeter methods
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Method that initializes the instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the Rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
