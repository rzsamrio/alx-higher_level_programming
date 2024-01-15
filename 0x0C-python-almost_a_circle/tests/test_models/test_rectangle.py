#!/usr/bin/python3
""" Insert doc """

from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
	def test_init_width(self):
		""" Test the width getter and setter """
		self.assertEqual(Rectangle(10, 1).width, 10)
		self.assertEqual(Rectangle(6, 1).width, 6)
		self.assertEqual(Rectangle(91, 1).width, 91)
		
		with self.assertRaises(TypeError, msg="width must be an integer"):
			Rectangle([], 1)
		with self.assertRaises(TypeError, msg="width must be an integer"):
			Rectangle("90", 1)
		with self.assertRaises(TypeError, msg="width must be an integer"):
			Rectangle(86.34, 1)
		with self.assertRaises(ValueError, msg="width must be > 0"):
			Rectangle(-90, -30)
		with self.assertRaises(ValueError, msg="width must be > 0"):
			Rectangle(0, 1)

	def test_init_height(self):
		""" Test the height property """
		self.assertEqual(Rectangle(1, 30).height, 30)
		self.assertEqual(Rectangle(6, 3).height, 3)

		with self.assertRaises(TypeError, msg="height must be an integer"):
			Rectangle(1, [])
		with self.assertRaises(TypeError, msg="height must be an integer"):
			Rectangle(1, "Number")
		with self.assertRaises(TypeError, msg="height must be an integer"):
			Rectangle(1, 67.89)
		with self.assertRaises(ValueError, msg="height must be > 0"):
			Rectangle(1, 0)
		with self.assertRaises(ValueError, msg="height must be > 0"):
			Rectangle(1, -5)

	def test_area(self):
		""" Test the area method """
		self.assertEqual(Rectangle(5,9).area(), 45)
		self.assertEqual(Rectangle(11, 3).area(), 33)
	
	def test_str(self):
		""" Test the __str__ method """
		self.assertIs(type(str(Rectangle(3, 2))), str)
		self.assertEqual(str(Rectangle(3, 9, 0, 0, 8)), "[Rectangle] (8) 0/0 - 3/9")
		self.assertEqual(str(Rectangle(6, 12, 4, 3, 19)), "[Rectangle] (19) 4/3 - 6/12")
		self.assertEqual(str(Rectangle(11, 9, id=15)), "[Rectangle] (15) 0/0 - 11/9")

