import board
import interface
import pygame

game_board = board.Board()

turn = 0
collumn = 0

pygame.init()
game = interface.Board_Interface(6, 7, 100, game_board)
'''while (game_board.end == False):
    print(game_board)
    while (collumn < 1 or collumn > 7):
        collumn = int(input())
    game_board.move(collumn, (turn % 2) + 1)
    turn += 1
    collumn = 0
    '''
game.run_game()

    
