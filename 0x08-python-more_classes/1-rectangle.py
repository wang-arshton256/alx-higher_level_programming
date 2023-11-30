#!/usr/bin/python3
"""
A class that defines a Rectangle
"""


"""
this class represents a rectangle
"""


class Rectangle:
    """
    Initialization for the class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialization for the class Rectangle
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """
            retrieves the width attribute
            """
        @width.setter
        def width(self, value):
            """
            sets width attributes
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0"
                        self.__width=value
