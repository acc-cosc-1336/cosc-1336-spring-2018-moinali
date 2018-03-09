import unittest

#write import statements for exam functions
from src.midterm.exam import get_miles_per_hour, get_bonus_pay_amount,reverse_string,get_list_min_max, get_list_min_max_file

class Test_Midterm(unittest.TestCase):

    def test_get_miles_per_hour_32_60(self):
        self.assertEqual(19.883872, get_miles_per_hour(32,60))
        '''
        5 points
        Test with arguments kilometers 32 and minutes 60 return value should be 19.883872
        '''



    def test_get_bonus_pay_amount_w_good_value(self):
        self.assertEqual(70,get_bonus_pay_amount(1000))
        '''
        5 points
        Test with value 1000 return value should be 70
        '''



    def test_get_bonus_pay_amount_w_bad_value(self):
        self.assertEqual('Invalid arguments',get_bonus_pay_amount(-5))
        '''
        5 points
        Test with -5 return value should be 'Invalid arguments'
        '''



    def test_reverse_string(self):
        self.assertEqual('ataD gnirtS yM',reverse_string('My String Data'))
        '''
        5 points
        Test with value My String Data return value should be ataD gnirtS yM
        '''



    def test_get_list_min_max(self):
        self.assertEqual((10, 40),get_list_min_max(['joe', 10, 15, 20, 30, 40]))
        '''
        5 points
        Test with ['joe', 10, 15, 20, 30, 40]    Returns:    [10, 40]
        '''



    def test_get_list_min_max_file(self):
        self.assertEqual((2,89),get_list_min_max_file())
        '''
        5 points
        Test with quiz.data file the return value should be [2,89]
        '''
        
#unittest.main(verbosity=2)
