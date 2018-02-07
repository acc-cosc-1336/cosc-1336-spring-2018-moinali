def sum_odd_numbers(num):
    '''
    WITH A FOR LOOP
    Given a number calculate and return the sum of odd numbers from 1 to num.
    Example: if num is 11 the sum total is 1+3+5+7+9+11 = 36
    :param num: Number greater than 0
    :return: the sum of all the odd numbers from 1 to num
    '''
    total = 0
    #write your code starting here; use total as the sum total
    for i in range(0,num+1):
        if i % 2 == 1:
            total += i
            
    return total

def list_of_even_numbers(num):
    '''
    WITH  WHILE LOOP
    Given a number return a list of all the even numbers from 1 to num
    Example: if num is 12 return the list 2,4,6,8,10,12,
    :param num:
    :return: A list of all even numbers up to a num
    '''
    even_numbers = ''
    #write your code starting here; you'll need to concatenate evens to even_numbers
    i = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            even_numbers += str(i)+","
    return even_numbers

def main1():
    '''
    You will make calls to sum_odd_numbers and list_of_even_numbers functions above.
    Example:
    Call list sum_odd_numbers and save its return value to a result variable
    result = sum_odd_numbers(10)
    print(result)

    For your assignment:

    Prompt user for a number from keyboard
    This is the number of times the program will loop and ...
    In the loop call the sum_odd_numbers(index) with the current value of the loop index and save return value
    print the value
    In the loop call the list_even_numbers(index) with the current value of the loop index and save return value
    print the value

    WHAT IS LOOP INDEX?
    for i in range(1,5): #i is loop index
       #other code

    while i < 10: #i is loop index
       #other code

    TO RUN YOUR PROGRAM IN IDLE SELECT RUN->RUN MODULE OR THE F5 KEY
    IN THE PYTHON SHELL TYPE main1() to run the code in this function

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    #write your code here
    """num = int(input("number of loops? '))
    loops = 0
    total = 0
    while loops < num:
        sum_odd_numbers(loops):
#return
#print
        list_even_numbers(loops)
          
        loops = loops + 1"""

def main2():
    '''
    WRITE ALL THE CODE IN HERE,

    Write a program that continues while user wants to continue
    Prompt the user for a whole number from the keyboard
    Generate a random value and compare it to the number the user provides
    If the numbers match display You guessed number!
    otherwise display Invalid guess
    The program will continue as long as user enters y when prompted to continue

    TO RUN YOUR PROGRAM IN IDLE SELECT RUN->RUN MODULE OR THE F5 KEY
    IN THE PYTHON SHELL TYPE main2() to run the code in this function

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    #write your code here
   """ keep_going = 'y'
    while keep_going == 'y':
        x = randint(1, 100)
        guess = int(input('guess a number: '))
        if guess == x:
            #return 'you guessed number'
        else:
            #return 'Invalid guess Hint: whole number between 1 to 100' 
        keep_going = input("enter y if you want to continue: ")"""
    

