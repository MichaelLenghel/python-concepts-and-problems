"""
Code adapted from Corey Schafer
Naming convention for tests is: "stest_Filename"
o run this test: python -m unittest test_calc.py
TestCode assertions: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
"""
import unittest # Pytest is an alternative module
import calc

"""
Inheriting from unittest.TestCase gives us access to a lot
of unit test capabiltiies
"""
class TestCalc(unittest.TestCase):

	# Naming convention "test_" is required
	def test_add(self):
		self.assertEqual(calc.add(10, 5), 15)
		self.assertEqual(calc.add(-1, 1), 0)
		self.assertEqual(calc.add(-1, -1), -2)

	def test_subtract(self):
		self.assertEqual(calc.subtract(10, 5), 5)
		self.assertEqual(calc.subtract(-1, 1), -2)
		self.assertEqual(calc.subtract(-1, -1), 0)

	def test_mult(self):
		self.assertEqual(calc.multiply(10, 5), 50)
		self.assertEqual(calc.multiply(-1, 1), -1)
		self.assertEqual(calc.multiply(-1, -1), 1)

	def test_divide(self):
		self.assertEqual(calc.divide(10, 5), 2)
		self.assertEqual(calc.divide(-1, 1), -1)
		self.assertEqual(calc.divide(-1, -1), 1)
		self.assertEqual(calc.divide(5, 2), 2.5)

		# Checks if exception is incurred. Context manager
		with self.assertRaises(ValueError):
			calc.divide(10, 0)

# This allows us to compile it normally
if __name__ == '__main__':
	unittest.main()