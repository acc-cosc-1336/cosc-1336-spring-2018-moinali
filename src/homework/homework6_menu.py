#write import statements for homework 6 functions
from src.homework.homework6 import get_dna_complement
from src.homework.homework6 import transcribe_dna_into_rna
from src.homework.homework6 import get_gc_content
from src.homework.homework6 import get_point_mutations
def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    #print('5) DNA motif')
    #print('6) Most likely Ancestor')
    print('7) Exit')
    print()

def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
    '''
    Write code to:
    Loop as long as user wants to continue.
    Prompt user for two dna strings of length 10 with letter range A,C,G, and T only.  
    Call the function get_point_mutations and display the mutations to screen.
    Ask user if they want to continue.
    '''

    
    
    keep_going = 'y'
    while keep_going == 'y':
        dna_string1 = input("Enter first string with 10 letters(A,C,G,T): ")           
        dna_string2 = input("Enter second string with 10 letters(A,C,G,T): ")
        print(get_point_mutations(dna_string1, dna_string2))
        
        keep_going = input("Enter y to continue or any other key to EXIT: ")
    

def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complment and display the complement to screen.
    '''
    file = open('dna_complement.dat', 'r')
##    for line in file:
##        get_dna_compliment(line)
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
    line5 = file.readline()

    a= get_dna_complement(line1)
    b= get_dna_complement(line2)
    c= get_dna_complement(line3)
    d= get_dna_complement(line4)
    e= get_dna_complement(line5)
    file.close()
    print(line1,':',a)
    print(line2,':',b)
    print(line3,':',c)
    print(line4,':',d)
    print(line5,':',e)
    
        

def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''
    file = open('transcribe_dna_to_rna.dat', 'r')
##    for line in file:
##        transcribe_dna_into_rna(line)
##    print (line)
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
    line5 = file.readline()

    a= transcribe_dna_into_rna(line1)
    b= transcribe_dna_into_rna(line2)
    c= transcribe_dna_into_rna(line3)
    d= transcribe_dna_into_rna(line4)
    e= transcribe_dna_into_rna(line5)
    file.close()
    print(line1,':',a)
    print(line2,':',b)
    print(line3,':',c)
    print(line4,':',d)
    print(line5,':',e)
    

def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''
    file = open('compute_gc_content.dat', 'r')
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
    line5 = file.readline()

    a= get_gc_content(line1)
    b= get_gc_content(line2)
    c= get_gc_content(line3)
    d= get_gc_content(line4)
    e= get_gc_content(line5)
    file.close()
    print(line1,':',a)
    print(line2,':',b)
    print(line3,':',c)
    print(line4,':',d)
    print(line5,':',e)

    

def handle_option_5():
    pass #optional 

def handle_option_6():
    pass #optional
run_menu()
