import unittest
import sys
import os
print(os.getcwd())
print(os.environ.get('PYTHONPATH'))
from ofa.code import add_two_numbers


class TestAdd(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)

