#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """metho not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area"""
        return self.__width*self.__height

    def __str__(self):
        """
        Return the informal and nicely printed string representation
        of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
