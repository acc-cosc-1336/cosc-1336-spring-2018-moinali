#write import statement for reverse string function
from src.midterm.exam import reverse_string
'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
again = 'y'
while again == 'y':
    string1= input('enter a string to reverse: ')
    print (reverse_string(string1))
    again = input('enter y to cont: ' )
    
