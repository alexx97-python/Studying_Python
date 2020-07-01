import unittest
from unittest.mock import patch
import employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        """
         run the code inside this function before every single test
         In this case every time we create objects that use for tests
        """
        self.emp_1 = employee.Employee('Oleksii', 'Sheiko', 50000)
        self.emp_2 = employee.Employee('Vovan', 'Kovalenko', 70000)

    def tearDown(self) -> None:
        """
        run the code inside this function after every single test
        """
        print('TearDown\n')

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Oleksii.Sheiko@email.com')
        self.assertEqual(self.emp_2.email, 'Vovan.Kovalenko@email.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Oleksii Sheiko')
        self.assertEqual(self.emp_2.fullname, 'Vovan Kovalenko')

        self.emp_1.first = 'Alex'
        self.emp_2.first = 'Vova'

        self.assertEqual(self.emp_1.fullname, 'Alex Sheiko')
        self.assertEqual(self.emp_2.fullname, 'Vova Kovalenko')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 73500)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Sheiko/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('April')
            mocked_get.assert_called_with('http://company.com/Kovalenko/April')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()