#!/usr/bin/python3

class Square():
    def __init__(self, size=0):
        try:
            if not Instantiation(size(int)):
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
