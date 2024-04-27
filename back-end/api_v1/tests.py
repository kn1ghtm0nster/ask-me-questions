from django.test import TestCase

# Create your tests here.

# TODO: REMOVE THE CODE BELOW. THIS IS DUMMY CODE


def add_numbers(num1, num2) -> int or None:
    if type(num1) is int and type(num2) is int:
        return num1 + num2
    return None


class TestAddNumbers(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(1, -1), 0)
        self.assertEqual(add_numbers(1.0, 1), None)
        self.assertEqual(add_numbers(1, 1.0), None)
        self.assertEqual(add_numbers(1.0, 1.0), None)
