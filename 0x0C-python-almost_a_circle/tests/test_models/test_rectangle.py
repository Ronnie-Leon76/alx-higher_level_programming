#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test the Rectangle Class"""
    def test_id(self):
        """Test that the id is correctly assigned"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """Test that the width is correctly assigned"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r3 = Rectangle("10", 2)
        with self.assertRaisesRegex(ValueError, "width must be  > 0"):
            r4 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be  > 0"):
            r5 = Rectangle(-10, 2)

    def test_height(self):
        """Test that the height is correctly assigned"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r3 = Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5 = Rectangle(2, -10)

    def test_x(self):
        """Test that x is correctly assigned"""
        r1 = Rectangle(10, 2, 3)
        self.assertEqual(r1.x, 3)
        r2 = Rectangle(2, 10, 8)
        self.assertEqual(r2.x, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3 = Rectangle(10, 2, "3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r4 = Rectangle(10, 2, -3)

    def test_y(self):
        """Test that y is correctly assigned"""
        r1 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r1.y, 4)
        r2 = Rectangle(2, 10, 8, 3)
        self.assertEqual(r2.y, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3 = Rectangle(10, 2, 3, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r4 = Rectangle(10, 2, 3, -3)
    
    def test_area(self):
        """Test that the area is correctly calculated"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test the method display"""
        r1 = Rectangle(4, 6)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), '####\n####\n####\n####\n####\n####\n')
        r2 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n')
        r3 = Rectangle(3, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r3.display()
            self.assertEqual(fake_out.getvalue(), ' \n \n  ###\n  ###\n')
        
    def test_str(self):
        """Test the __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (15) 1/0 - 5/5")

    def test_update(self):
        """Test the update method"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/5 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        



        
        
