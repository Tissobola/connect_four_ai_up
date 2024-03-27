import board
import pygame
import astar_h1
import astar_h2
import tree
import mcts



#-------------------------------- GAME --------------------------------
game_board = board.Board()
""" bot1 = astar_h1.AStarBot(game_board, 1)
bot2 = mcts.MonteCarlo(game_board, 2)

turn = 0
collumn = 0

# pygame.init()
# game = interface.Board_Interface(6, 7, 100, game_board)
# game.run_game()
print(game_board)
while (not game_board.end):
  if (turn % 2) + 1 == 1:
    print('astar')
    bot1.play()
  else:
    print('montecarlo')
    bot2.play()
    
  turn += 1

  print(game_board.__str__())   

#--------------------------------------interface testes-------------------------------------------------------------
 """
import interface 
#for menu
#player vs player
#interface.main(game_board, algorithm1=None, algorithm2=None, GUI= True)

#player vs astar-nossa
#interface.main(game_board, algorithm1='astar_h1', algorithm2=None, GUI= True)

#player vs montecarlo
#interface.main(game_board, algorithm1='montecarlo', algorithm2=None, GUI= True)

#player vs astar-professor 
#interface.main(game_board, algorithm1='astar_h2', algorithm2=None, GUI= True)

#astar_h1 vs astar_h2
#interface.main(game_board, algorithm1='astar_h1', algorithm2='astar_h2', GUI= True)
