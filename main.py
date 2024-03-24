import board
import interface
import heuristic_montecarlo
import pygame
import tree
from algorithms import astar
import play_game
from board import Board

# -------------------------------- GAME --------------------------------
game_board = board.Board()
bot = astar.AStarBot(game_board, 2)

turn = 0
collumn = 0

game_board = board.Board()
print(game_board)

while (not game_board.end):
    if game_board.turn == 'X':
        game_board.move(int(input()))
        game_board.change_turn()
    else:
        print('montecarlo')
        heuristic_montecarlo.play_MCTS(game_board, game_board.turn)
    game_board.change_turn()
    print(game_board)
    
game_board.run_game()


play_game.main(Board(),algorithm1=None,algorithm2=None, GUI=True)
