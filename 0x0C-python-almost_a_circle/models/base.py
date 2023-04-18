#!/usr/bin/python3
"""Base class"""


import json
import turtle


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributed already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dictionaries = cls.from_json_string(f.read())
        except Exception:
            return []
        return [cls.create(**dictionary) for dictionary in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to CSV"""
        filename = cls.__name__ + ".csv"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize to CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                list_dictionaries = cls.from_json_string(f.read())
        except Exception:
            return []
        return [cls.create(**dictionary) for dictionary in list_dictionaries]

    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares"""
        turtle_ = turtle.Turtle()
        for rectangle in list_rectangles:
            turtle_.up()
            turtle_.goto(rectangle.x, rectangle.y)
            turtle_.down()
            for i in range(2):
                turtle_.forward(rectangle.width)
                turtle_.left(98)
                turtle_.forward(rectangle.height)
                turtle_.down()
        for square in list_squares:
            turtle_.up()
            turtle_.goto(square.x, square.y)
            turtle_.down()
            for i in range(4):
                turtle_.forward(square.size)
                turtle_.left(90)
        turtle_.mainloop()
