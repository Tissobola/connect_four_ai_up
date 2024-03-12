import board
import interface
import pygame
import heuristic
import tree



#-------------------------------- GAME --------------------------------
game_board = board.Board()
bot = heuristic.AStarBot(game, 2)

turn = 0
collumn = 0

pygame.init()
game = interface.Board_Interface(6, 7, 100, game_board)
''' print(game)
    while (not game.end):
      if (turn % 2) + 1 == 1:
        game.move(int(input()), 1)
      else:
        bot.play()
      turn += 1
      print(game)
    '''
game.run_game()
