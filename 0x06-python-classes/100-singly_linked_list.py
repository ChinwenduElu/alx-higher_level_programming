#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node (with private data and next_node)
Defines class SinglyLinkedList (with private head and public sorted_insert)
"""


class Node:
    """
    class Node definition

    Args:
        data (int): private
        next_node : private; can be None or Node object

    Functions:
        __init__(self, data, next_node=None)
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    """

    def __init__(self, data, next_node=None):
        """
        Initializes node

        Attributes:
            data (int): private
            next_node : private; can be None or Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter 

        Args: 
            value: sets data to value if int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Return: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter 

        Args:
            value: sets node if value is next node or none
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    class SinglyLinkedList definition

    Args:
        head: private

    Functions:
        __init__(self)
        sorted_insert(self, value)
    """

    def __init__(self):

                self.__head = None
