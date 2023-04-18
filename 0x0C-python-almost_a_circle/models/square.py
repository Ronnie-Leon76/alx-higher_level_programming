#!/usr/bin/python3
"""Module contains a square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Data"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints formatted string"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square instance"""
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of Square instance"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
