#write the import for the function get_count_A_C_G_and_T_in_string from assignment 6 file
from assignment6 import get_count_A_C_G_and_T_in_string
'''
Using function get_count_A_C_G_and_T_in_string create a main function and...
Call the function get_count_A_C_G_and_T_in_string from assignment 6 file
With the string AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC as an argument
Sample Output:

DNA String:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
A 20, C 12, G 17, T 21


Call the main function in Python Shell or in this file.
'''

def main():
    dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

    a,c,g,t = get_count_A_C_G_and_T_in_string(dna_string)
    
    
    print("DNA String:"+ '\n'+ dna_string+'\n'+'A',a,', C',c,',','G',g,',','T',t)
    


main()
