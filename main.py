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
bot = heuristic_montecarlo.MonteCarlo_heuristics(game_board, 'O')

while not game_board.end:
    
    if game_board.turn == 'X':
        move = int(input("Player X's move: "))  # Player X's move
        game_board.move(move)
        
    if game_board.turn == 'O':
        print("Player O's turn (MCTS)")
        move = bot.get_best_move()  # MCTS player's move
        game_board.move(move)
    
    print(game_board)
    game_board.change_turn()
    


#play_game.main(Board(),algorithm1=None,algorithm2=None, GUI=True)
