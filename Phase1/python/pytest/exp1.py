"""
    Testing: means checking if the code works as expected.
     
"""
import unittest
def add(x,y):
    return x + y

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), 5)
    
unittest.main()
