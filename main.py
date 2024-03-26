
import board_old
import play_game
import pygame
import tree
from algorithms import astar


#-------------------------------- GAME --------------------------------


# game_board = board.Board()

# turn = 0
# collumn = 0

# pygame.init()
# game_board = board.Board()

# play_game.main(game_board,algorithm1=None,algorithm2=None, GUI=True)

# #-------------ASTAR---------------------
# import board
# import tree
# from algorithms import astar
# game_board = board.Board()
# bot = astar.AStarBot(game_board, game_board.p2Symbol)
# print(game_board)
# turn = 0
# collumn = 0
# print(game_board)
# while not game_board.end:
#     print(game_board)
#     if game_board.turn == game_board.p1Symbol:
#         column = int(input("Player 1 (X), enter column: "))
#         game_board.move(column)
#     else:
#         bot.play()
# print(game_board)
    


#-------------ASTAR NEW---------------------
import board
import tree
from algorithms import astar

game_board = board.Board()
print(game_board)

while (not game_board.end):
  if game_board.turn == game_board.p1Symbol:
    #game_board.move(int(input()), 1)

    column = int(input("Player 1 (X), enter column: "))
    game_board.move(column)
    print("Game Board:")
    print(game_board)
    
  else:
    game_board.move(astar(game_board))
    # print("score = ", game_board.score)
    print("Game Board:")
    print(game_board)
  

    
  
  





#---------PLAYER VS PLAYER---------------------
# while not game_board.end:
#     print(game_board)
#     if game_board.turn == game_board.p1Symbol:
#         column = int(input("Player 1 (X), enter column: "))
#         game_board.move(column)
#     else:
#         column = int(input("Player 2 (O), enter column: "))
#         game_board.move(column)
        
# print(game_board)
   

#...............................
    
# game_board.run_game()
# game_board.run_game()



# import play_game
# from board import Board
# from algorithms import astar


# play_game.main(Board(),algorithm1=None,algorithm2=None, GUI=True)



#play_game.main(Board(), algorithm1="astar", algorithm2=None, GUI=True)
