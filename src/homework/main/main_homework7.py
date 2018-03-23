#write import statement for homework 7 file
from src.homework.homework7 import p_distance, pd_matrix
'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:

[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen
'''
def main():
    file = open('p_distance.dat', 'r')
    f = []
    for line in file.readlines():
        f.append(line.split())
    file.close()
    print( pd_matrix(f))
main()
