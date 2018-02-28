'''
1.DO NOT USE LISTS.
Define a function get_point_mutations with parameters dna_string1 and dna_string2.
The function returns the hamming distance value (see below).


Problem:
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the 
number of corresponding symbols that differ in s and t. 
See url http://rosalind.info/problems/hamm/ for more information.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset (function parameter arguments)
dna_string1: GAGCCTACTAACGGGAT
dna_string2: CATCGTAATGACGGCCT

Sample Output (function return value)
7
'''

def get_point_mutations(dna_string1, dna_string2):
    dna_string1 = dna_string1.upper()
    dna_string2 = dna_string2.upper()
    count = 0
    for i in range(0,len(dna_string1)):
        if dna_string1[i] != dna_string2[i]:
            count += 1
    return count

'''
2.DO NOT USE LISTS.
Define function get_dna_complement with dna_string parameter.
The function returns one string-the DNA complement see below.

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then 
taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
See http://rosalind.info/problems/revc/ for more information.

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset (function parameter argument)
dna_string: AAAACCCGGT

Sample Output(function return value)
ACCGGGTTTT
'''
def get_dna_complement(dna_string):
    dna_string = dna_string.upper()
    dna_string = dna_string[::-1]
    dna_string1 = ""
    for i in range(0, len(dna_string)):
        if dna_string[i] == "T":
            dna_string1 += "A"

        if dna_string[i] == "A":
            dna_string1 += "T"

        if dna_string[i] == "G":
            dna_string1 += "C"

        if dna_string[i] == "C":
            dna_string1 += "G"

    return dna_string1
    
    
    

'''
3.DO NOT USE LISTS.
Define transcribe_dna_into_rna with a dna_string parameter.
The function returns the transcribed rna see below.

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing 
all occurrences of 'T' in t with 'U' in u.
See http://rosalind.info/problems/rna/ for more information

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT

Sample Output
GAUGGAACUUGACUACGUAAAUU
'''
def transcribe_dna_into_rna(dna_string):
    dna_string = dna_string.upper()
    for i in dna_string:
        dna_string = dna_string.replace('T','U')
    return dna_string

    

'''
4.DO NOT USE LISTS.
Define a function named get_gc_content with a string parameter named dna_string.
The function returns the gc content see below.

Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset (function parameter argument)
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output(function return value)
60.919540
'''
def get_gc_content(dna_string):

    dna_string = dna_string.upper()
    count = 0
    for ch in dna_string:
        if ch == 'C' or ch == 'G':
            count+=1
    value = (count/len(dna_string))*100
    return format(value, '.6f')
    

'''
5.DUE TO COMPLEXITY THIS PROBLEM IS OPTIONAL
DO NOT USE LISTS.
Define function find_motif_in_dna with parameters dna_string and dna_sub.
The function returns 3 integers 

Problem:
The location of a substring s[j:k] is its beginning position j; note that t will have multiple 
locations in s if it occurs more than once as a substring of s (see the Sample below).
See http://rosalind.info/problems/subs/ for more information.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: 4 integers with the locations of t as a substring of s.
Example:

Sample Dataset (function parameter arguments)
dna_string: GATATATGCATATACTT
dna_sub:    ATAT

Sample Output(function return values)
2 4 10
'''
def find_motif_in_dna(dna_string, dna_sub):
    pass
    
    

'''
6.DUE TO COMPLEXITY THIS PROBLEM IS OPTIONAL
DO NOT USE LISTS.
Define a function get_most_likely_ancestor_conensus with 7 dna_string parameters  -THIS IS OPTIONAL
Returns the consensus of dna strings.

Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

DNA Strings(7 function parameters)
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile (Function Return Values)
A   5 1 0 0 5 5 0 0
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6

Consensus(Function Return Value)	
A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
ATCCAGCT
GGGCAACT
ATGGATCT
AAGCAACC
TTGGAACT
ATGCCATT
ATGGCACT

Sample Output
ATGCAACT

A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''
def get_most_likely_ancestor_conensus(a,b,c,d,e,f,g):
    pass
    
    
