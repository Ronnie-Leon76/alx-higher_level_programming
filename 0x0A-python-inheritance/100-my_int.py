#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """Represent a MyInt"""
    def __eq__(self, other):
        """Invert the behavior of == and !="""
        return int(self) != int(other)

    def __ne__(self, other):
        """Invert the behavior of != and =="""
        return int(self) == int(other)
