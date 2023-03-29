#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Method"""
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        elif int(value) < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value
