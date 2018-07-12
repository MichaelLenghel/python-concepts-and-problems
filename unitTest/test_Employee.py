import unittest
from unittest.mock import patch
from Employee import Employee

class TestEmployy(unittest.TestCase):

	# Ran once before all other code
	# Useful if want to do something once, but too costy 
	# to do before every test
	# Tests should always be isolated
	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	# Ran once at the end after all other code
	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	# Will run code before every single test
	def setUp(self):
		print('setUp')
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)

	# Will run code after every single test. Example: closing or deleting databases etc.
	def tearDown(self):
		print('tearDown\n')
		pass

	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

		# Checks if name changed as reflected in email
		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 'Sue Smith')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.fullname, 'John Schafer')
		self.assertEqual(self.emp_2.fullname, 'Jane Smith')

	def test_apply_raise(self):
		print('test_apply_raise')
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)

	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.asset_called_with('http://company.com/Schafer/May')
			self.assertEqual(schedule, 'Success')

			mocked_get.return_value.ok = False
			mocked_get.return_value.text = 'Bad Response!'

			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.asset_called_with('http://company.com/Smith/June')
			self.assertEqual(schedule, 'Bad Response!')
# This allows us to compile it normally
if __name__ == '__main__':
	unittest.main()