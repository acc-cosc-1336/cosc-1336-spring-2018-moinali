#write the import for function for assignment7 sum_list_values
from src.assignments.assignment7 import sum_list_values
'''
Create a function named process_list that calls the sum_list_values function.
Prints the list values and the sum of the element in the list as follows:
joe 10 15 20 30 40 sum: 115

Create a main function.
In the function loop as long as user wants to add another list.
Prompt the user for name and append to the list.
Prompt the user for number of numeric values in the list.
Iterate the number of times the user enters and prompt end-user for n numeric values.

Call the main function
--------------------
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

'''
def process_list(list1):
    total = sum_list_values(list1)
    print(list1, total)


def main():
    cont = 'y'
    while cont == 'y':
        list1 = []
        name = input('enter a name: ')
        list1.insert(0, name)
        n = int(input('how many numbers: '))
        i =0
        while i < n:
            num = int(input('enter a num: '))
            list1.append(num)
            i+=1                 
        cont = input('press y to keep adding names: ')
        process_list(list1)
main()
        
