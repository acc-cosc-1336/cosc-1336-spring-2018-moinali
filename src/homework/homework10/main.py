from src.homework.homework10.player import Player
from src.homework.homework10.game_log import GameLog
#write import statement for GameLog class

#Create a game log instance
log = GameLog()


#SEnd the game_log instance to Player class as an argument

Player(log).roll_doubles()


#call the game log display method below
GameLog.display_log(log)



