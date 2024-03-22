# import board
# import interface
# import pygame
# import tree
# import astar


# #-------------------------------- GAME --------------------------------
# game_board = board.Board()
# bot = astar.AStarBot(game_board, 2)

# turn = 0
# collumn = 0
# '''
# pygame.init()
# game = interface.Board_Interface(6, 7, 100, game_board)
# print(game)
# '''
# while (not game.end):
#   if (turn % 2) + 1 == 1:
#     game.move(int(input()), 1)
#   else:
#     bot.play()
#   turn += 1
#   print(game)
    
# game.run_game()



import play_game
from board import Board


play_game.main(Board(),algorithm1=None,algorithm2=None, GUI=True)
