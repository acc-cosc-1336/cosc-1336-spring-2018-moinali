from src.assignments.assignment4 import factorial

def main():#void function
    '''
    Create a loop that'll run until the user doesn't type the letter 'y'
    In the loop,
    Capture one number from the keyboard and validate for a range between 1 and 10.
    Call the factorial function.
    Save the result to a variable.
    Print the variable value.

    Ask the user if they want to continue.

    TO RUN YOUR PROGRAM GO TO IN PYTHON IDLE RUN->RUN MODULE.
    IN THE PYTHON SHELL TYPE main()

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    
    keep_going = 'y'
    while keep_going == 'y':
        num = int(input('enter a number to get factorial: '))

        while num >10 or num < 0:
            print ('invalid range')
            num = int(input('enter a number to get factorial: '))
        f= factorial(num)
        
        print(f)

        keep_going = input('to keep going type y: ')


main()


#another option to run the program is to call the main() function below and Run->Run Module
