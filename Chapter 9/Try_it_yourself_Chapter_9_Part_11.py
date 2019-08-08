#Try it yourself 9-14: Dice
from random import randint


class Die():
    '''An attempt to model a dice'''
    
    def __init__(self, sides = 6):
        '''initializing the dice class'''
        self.sides = sides
        
    def roll_die(self):
        '''a method used to roll the dice'''
        print(randint(1, self.sides))
        
six_sided_dice = Die()
ten_sided_dice = Die(10)
twenty_sided_dice = Die(20)
six_sided_dice.roll_die()
ten_sided_dice.roll_die()
twenty_sided_dice.roll_die()
