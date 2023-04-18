#!/usr/bin/python3


from .base import Base


"""Rectangle Class"""


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Data"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be  > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """calculate area"""
        return self.__width*self.__height

    def display(self):
        """prints in stdout the Rectangle"""
        for i in range((self.__height+self.__y)):
            if i > (self.__y-1):
                for j in range((self.__width+self.__x)):
                    if j > (self.__x-1):
                        print("#", end='')
                    else:
                        print(" ", end='')
            else:
                print(" ", end='')
            print()

    def __str__(self):
        """Prints nicely formatted data"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update Rectangle class"""
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
