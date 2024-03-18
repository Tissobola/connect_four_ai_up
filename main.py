import board
import interface
import pygame
import heuristic
import tree



#-------------------------------- GAME --------------------------------
game_board = board.Board()
bot = heuristic.AStarBot(game_board, 2)

turn = 0
collumn = 0

# pygame.init()
# game = interface.Board_Interface(6, 7, 100, game_board)
# game.run_game()

print(game_board)
while (not game_board.end):
  if (turn % 2) + 1 == 1:
    game_board.move(int(input()), 1)
  else:
    bot.play()
  turn += 1

  print(game_board)
