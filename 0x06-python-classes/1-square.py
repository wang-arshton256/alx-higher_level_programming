#!/usr/bin/python3
"""Square module
This module contails a class suare which defines a square
"""


class Square():
    """Defines a suare"""
    def __init__(self, size):
        """Sets all the neccesary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
