import unittest

from src.assignments.assignment4 import sample_function
from src.assignments.assignment4 import factorial

class Test_Assign4(unittest.TestCase):

    def test_sample_one(self):
        '''
        This is an example to guide you in creating test cases.
        The sample_function takes an argument and returns the same value. If it takes a 2 it will return a 2.
        :return:
        '''
        self.assertEqual(2, sample_function(2))

    def test_sample_two(self):
        '''
        This is an example to guide you in creating test cases.
        The sample_function takes an argument and returns the same value. If it takes a 2 it will return a 2.
        In this test case, the test is for no equality.
        :return:
        '''
        self.assertNotEqual (1, sample_function(2))

#create two test cases for the factorial function, one test case with a value of 5 and the other with value of 6
#THE NAME OF THE FUNCTION MUST BEGIN WITH test OTHERWISE THE TestCase suite will not recognize it as a test case.
    def factorial_when_5_corret_120(self):
        self.assertNotEqual (120, factorial(5))
    def factorial_when_6_corret_120(self):
        self.assertNotEqual (720, factorial(6))





#remove the pound sign at the beginning of the next statement to run tests locally.
#unittest.Main(verbosity=2)
#add the pound sign back before uploading to Github
        

