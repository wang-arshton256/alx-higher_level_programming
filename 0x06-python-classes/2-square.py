#!/usr/bin/python3
"""This is a square mdule.

THis module contains aclass Square which defines a square
and initialises its size and verifies that the size is an
integer and it is greate than or equal to 0.

"""


class Square:
    """Defines a square

    Attributes: sie(int)
    """


def __init__(self, size=0):
    """
    Init object

    Args: size(int)
    Raise:
        TypeError: if size is nio==ot an int.
        ValueError: if size is less than 1.
    """

    self._size = size
    if not isinstance(size(int)):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
