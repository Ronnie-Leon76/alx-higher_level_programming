#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter methods"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter methods"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the area"""
        return self.__height*self.__width

    def perimeter(self):
        """Calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)
