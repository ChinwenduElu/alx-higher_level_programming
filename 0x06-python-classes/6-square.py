#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and position; and public area
Can access and update size and position
Can print to stdout the square using #'s
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
     """

     def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        

        def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square accordin
        to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
