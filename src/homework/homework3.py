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

