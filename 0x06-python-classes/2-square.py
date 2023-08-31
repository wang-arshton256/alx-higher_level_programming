#!/usr/bin/python3
"""This is a square mdule.

THis module contains aclass Square which defines a square
and initialises its size and verifies that the size is an
integer and it is greate than or equal to 0.

"""


class Square:
    """
    Represent a square

    Attributes:
      size: size
    """
    def __init__(self, size=0):
        """
        Init object

        Args:
          size: size
        Raise:
          TypeError: if size not an int
          ValueError: if size less than 1
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")
        except (ValueError) as size:
