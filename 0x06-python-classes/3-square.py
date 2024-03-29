#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize the data"""
        self.__size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Method"""
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns current square area"""
        return self.__size**2
