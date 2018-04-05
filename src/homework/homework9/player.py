#write import statement for Die class
from src.homework.homework9.die import Die
'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''

        self.die1 = Die()
        self.die2 = Die()

        


    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        d1 = 1
        d2 = 2
        count = 0
        while d1 != d2:
            count +=1
            d1 = self.die1.roll()
            d2 = self.die2.roll()
            print('die 1: ',d1,'die 2: ',d2,)
        else:
            print('Double rolled!! \n It took total of',count,'attempts')



