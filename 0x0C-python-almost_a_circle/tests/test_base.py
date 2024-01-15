#!/usr/bin/python3
""" Insert doc """


import unittest
from sys import maxsize
from models.base import Base

class TestBase(unittest.TestCase):
	def testid(self):
		self.assertEqual(Base(94).id, 94)
		self.assertEqual(Base(maxsize).id, maxsize)
		self.assertEqual(Base().id, 1)
		self.assertEqual(Base().id, 2)
		self.assertEqual(Base(175).id, 175)
		self.assertEqual(Base(9).id, 9)
		self.assertEqual(Base().id, 3)


if __name__ == '__main__':
	unittest.main()
	
