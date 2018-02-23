import unittest
#write the import for function get_count_A_C_G_and_T_in_string
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string

class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        self.assertEqual((6,4,5,6), get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG'))
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''


    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        self.assertEqual((20,12,17,21), get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''
#unittest.main(verbosity=2)
