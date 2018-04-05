import unittest

#Write the import statement for the Die class
from src.homework.homework9.die import Die
class TestHomework9(unittest.TestCase):

    def test_rolls_values_1_to_6(self):
        '''
        Write a test case to ensure that the Die class only rolls values from 1 to 6

        '''
        self.rolling = Die()
        self.assertTrue(range(1,6), self.rolling.roll())

#unittest.main(verbosity=2)

