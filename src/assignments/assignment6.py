def get_count_A_C_G_and_T_in_string(dna_string):
    dna_string = dna_string.upper()
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for ch in dna_string:
        if ch == "A":
            countA += 1
        if ch == "C":
            countC += 1
        if ch == "G":
            countG += 1
        if ch == "T":
            countT += 1
    return countA, countC, countG, countT







    
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''

