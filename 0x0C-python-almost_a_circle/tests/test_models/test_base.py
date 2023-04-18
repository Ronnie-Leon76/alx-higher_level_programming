#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test the class base"""
    def test_id(self):
        """Test that the id is correctly assigned"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test the static method to_json_string"""
        r1 = Base.to_json_string(None)
        self.assertEqual(r1, "[]")
        self.assertEqual(r1, "[]")
        r2 = Base.to_json_string([])
        self.assertEqual(r2, "[]")
        r3 = Base.to_json_string([{'id': 89}])
        self.assertEqual(r3, '[{"id": 89}]')
        r4 = Base.to_json_string([{'id': 7}, {'id': 89}])
        self.assertEqual(r4, '[{"id": 7}, {"id": 89}]')

    def test_from_json_string(self):
        """Test the static method from_json_string"""
        r1 = Base.from_json_string(None)
        self.assertEqual(r1, [])
        r2 = Base.from_json_string("[]")
        self.assertEqual(r2, [])
        r3 = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(r3, [{'id': 89}])
        r4 = Base.from_json_string('[{"id": 7}, {"id": 89}]')
        self.assertEqual(r4, [{'id': 7}, {'id': 89}])

    def test_save_to_file(self):
        """Test the class method save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(),
            '[{"x": 2, "size": 10, "id": 3, "y": 8}, {"x": 0, "size": 2, "id": 4, "y": 0}]'
            )
            self.assertEqual(f.read(),
            '[{"id": 4, "width": 10, "height": 7, "x": 2, "y": 8}, {"x": 0, "size": 2, "id": 4, "y": 0 }]'
            )
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(),
            '[{"x": 2, "size": 10, "id": 3, "y": 8}, {"x": 0, "size": 2, "id": 4, "y": 0}]'
            )

    def test_create(self):
        """Test the class method create"""
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.__class__.__name__, "Rectangle")
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.__class__.__name__, "Square")

    def test_load_from_file(self):
        """Test the class method load_from_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]),
        "[Rectangle] (1) 2/8 - 10/7"
        )
        self.assertEqual(str(list_rectangles_output[1]),
        "[Rectangle] (2) 0/0 - 2/4"
        )
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]),
        "[Square] (3) 2/8 - 10"
        )
        self.assertEqual(str(list_rectangles_output[0]),
        "[Rectangle] (4) 2/8 - 10/7"
        )
        self.assertEqual(str(list_rectangles_output[1]),
        "[Rectangle] (2) 0/0 - 2"
        )
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]),
        "[Square] (3) 2/8 - 10"
        )
        self.assertEqual(str(list_squares_output[1]),
        "[Square] (4) 0/0 - 2"
        )

    def test_save_to_file_csv(self):
        """Test the class method save_to_file_csv"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(),
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 0, "size": 2, "id": 4, "y": 0 }]'
            )
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(),
            '[{"x": 2, "size": 10, "id": 3, "y": 8}, {"x": 0, "size": 2, "id": 4, "y": 0}]'
            )

    def test_load_from_file_csv(self):
        """Test the class method load_from_file_csv"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output[0]),
        "[Rectangle] (1) 2/8 - 10/7"
        )
        self.assertEqual(str(list_rectangles_output[1]),
        "[Rectangle] (2) 0/0 - 2"
        )
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(list_squares_output[0]),
        "[Square] (3) 2/8 - 10"
        )
        self.assertEqual(str(list_squares_output[1]),
        "[Square] (4) 0/0 - 2"
        )
