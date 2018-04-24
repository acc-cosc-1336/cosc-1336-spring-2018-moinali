from src.homework.homework11.player import Player
from src.homework.homework11.game_log import GameLog
from src.homework.homework11.die6 import Die6
from src.homework.homework11.die8 import Die8
#write import statements for Die6 and Die8 classes
##src.homework.homework11.
game_log = GameLog()
d6 = Die6()
d8 = Die8()

#ASSIGNMENT 12: Write statements to create Die6 and Die8 instances

#ASSIGNMENT12: pass the Die6 and Die8 instance object variables to the Player instantiation below as parameters after
#the game_log parameter
Player(game_log,d6,d8).roll_doubles()

game_log.display_log()

#ASSIGNMENT12: Create another GameLog instance
game_log = GameLog()
#ASSIGNMENT12: Write statements to create Die6 and Die8 instances
#ASSIGNMENT12: Create a new instance of the Player class and pass it the game log, die6, and die8 instances.
#ASSIGNMENT12: Call the player instance roll_doubles.
#ASSIGNMENT12: Call the game log instance display_log method.

d12 = Die6()
d16 = Die8()

Player(game_log, d12, d16).roll_doubles()

game_log.display_log()
