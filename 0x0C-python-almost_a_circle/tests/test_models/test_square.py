#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test the class square"""
    def test_id(self):
        """Test that the id is correctly assigned"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        s2 = Square(2)
        self.assertEqual(s2.id, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_size(self):
        """Test that the size is correctly assigned"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(2)
        self.assertEqual(s2.size, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s3 = Square("5")
        with self.assertRaisesRegex(ValueError, "width must be  > 0"):
            s4 = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be  > 0"):
            s5 = Square(-5)
    
    def test_x(self):
        """Test that x is correctly assigned"""
        s1 = Square(5, 3)
        self.assertEqual(s1.x, 3)
        s2 = Square(2, 8)
        self.assertEqual(s2.x, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s3 = Square(5, "3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s4 = Square(5, -3)
    
    def test_y(self):
        """Test that y is correctly assigned"""
        s1 = Square(5, 0, 3)
        self.assertEqual(s1.y, 3)
        s2 = Square(2, 0, 8)
        self.assertEqual(s2.y, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s3 = Square(5, 0, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s4 = Square(5, 0, -3)
        
    def test_area(self):
        """Test the method area"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.area(), 64)

    def test_display(self):
        """Test the method display"""
        s1 = Square(5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), '#####\n#####\n#####\n#####\n#####\n')
        s2 = Square(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(), '  ##\n  ##\n')
        s3 = Square(3, 1, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s3.display()
            self.assertEqual(fake_out.getvalue(), ' \n \n \n ###\n ###\n ###\n')
    
    def test_str(self):
        """Test the method __str__"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 1)
        self.assertEqual(s2.__str__(), "[Square] (39) 1/0 - 5")
        s3 = Square(2, 3, 2)
        self.assertEqual(s3.__str__(), "[Square] (40) 3/2 - 2")

    def test_update(self):
        """Test the method update"""
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")
        s1.update(x=1, size=2, y=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/3 - 2")
        s1.update(size=1, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/1 - 1")

    def test_to_dictionary(self):
        """Test the method to_dictionary"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 41, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)