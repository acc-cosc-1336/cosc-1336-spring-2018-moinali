'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''
def main():
    inv = {}
    keepgoing = 'y'
    while keepgoing == 'y':
        name = input('enter a name: ')
        quantity = int(input('enter a quantity: '))
        if name not in inv:
            inv[name] = quantity
        keepgoing = input('enter y to continue: ')
    
    file = open('inventory.txt','w')
    inv
    file.write(str(inv))
    file.close()
    print(inv)
    print('file updated!')
main()
