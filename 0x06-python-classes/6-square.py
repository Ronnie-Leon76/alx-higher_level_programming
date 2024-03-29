#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Setter method"""
        if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()


