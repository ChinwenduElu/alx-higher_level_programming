#!/usr/bin/python3
"""
Module 5-text_indentation
Function that prints text with 2 new lines after each ".", "?", and ":"
Text must be a string
"""


def text_indentation(text):
    """
    prints 2 new lines after ".?:" characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
