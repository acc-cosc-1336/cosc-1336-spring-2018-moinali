from src.homework.homework11.die import Die
#HOMEWORK12: add import statement for Die class
'''
Define a Die6 class that inherits from the Die class.
Create a constructor with only one parameter self.
In the constructor, call the Die class constructor(__init__ method) and pass it parameter arguments self and 8.
Define a class method named roll.
In the method:
 a)display 'Rolled 8 sided die' (MAKE SURE TO USE THE SIDES CLASS ATTRIBUTE; DON'T USE THE NUMBER 8).
 b)call and return the Die class roll method(This will return the roll value).

'''
class Die8(Die):
    def __init__(self):
        Die.__init__(self,8)

    def roll(self):
        print('Rolled 8 sided die')
        self.value = random.randint(1, self.sides)
        return self.value
