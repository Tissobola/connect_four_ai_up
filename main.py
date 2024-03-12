import heuristic
import tree
import board

#-------------------------------- GAME --------------------------------   
game = board.Board()
bot = heuristic.AStarBot(game, 2)

turn = 0
collumn = 0

print(game)
while (not game.end):
    if (turn % 2) + 1 == 1:
        game.move(int(input()), 1)
    else:
        bot.play()
    turn += 1
    print(game)
    
# 1 4 2 2 1 3 1 2