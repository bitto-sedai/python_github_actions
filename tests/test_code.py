from code.code import add_two_numbers
import unittest



class TestAdd(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)



