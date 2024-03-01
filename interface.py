import pygame
import sys
from board import *

class Board_Interface:
    def __init__(self, row_count, column_count, square_size, board):
        self.row_count = row_count
        self.column_count = column_count
        self.square_size = square_size
        self.radius = int(square_size / 2 - 5)
        self.width = column_count * square_size
        self.height = (row_count + 1) * square_size
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.WHITE = (255,255,255)
        self.BACKGROUND = (230, 191, 131)
        self.GRILL = (193, 154, 107)
        self.game_board = board
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("CONNECT FOUR")

    def draw_board(self):
        for i in range(self.game_board.rows):
            for j in range(self.game_board.cols):
                if self.game_board.board[i][j] == '.':
                    pygame.draw.circle(self.screen, self.WHITE, (i * self.square_size + self.square_size // 2, (j + 1) * self.square_size + self.square_size // 2), self.radius)
                if self.game_board.board[i][j] == 'X':
                    pygame.draw.circle(self.screen, self.RED, (i * self.square_size + self.square_size // 2, (j + 1) * self.square_size + self.square_size // 2), self.radius)
                    
                #drawingboard 
                #pygame.draw.rect(self.screen, self.GRILL, (i * self.square_size, (j + 1) * self.square_size, self.square_size, self.square_size), 3)
                
        pygame.display.update()

    def run_game(self):
        running = True
        while running:
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.BACKGROUND)
        pygame.quit()





