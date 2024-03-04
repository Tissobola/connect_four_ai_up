import pygame
import sys
from board import *

class Piece:
    def __init__(self):
        self.square_size = 100
        self.radius = int(self.square_size / 2 - 5)
    
    def draw(self, screen, y, x, symbol):
        if symbol == 'X': 
            pygame.draw.circle(screen, (255, 0, 0), (y, x), self.radius)
        elif symbol == 'O':
            pygame.draw.circle(screen,(255, 255, 0), (y, x), self.radius)
        elif symbol == '.':
            pygame.draw.circle(screen,(255, 255, 255), (y, x), self.radius)


class Board_Interface:
    def __init__(self, row_count, column_count, square_size, board):
        self.row_count = row_count
        self.column_count = column_count
        self.square_size = square_size
        self.radius = self.radius = int(square_size / 2 - 5)
        self.width = 1200
        self.height = 700
        #interface colors
        self.colors = {
            "BLUE": (0, 0, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "YELLOW": (255, 255, 0),
            "WHITE": (255, 255, 255),
            "BACKGROUND": (230, 191, 131),
            "GRILL": (193, 154, 107),
            "EMPTY": (230, 230, 230)
        }
        #board
        self.game_board = board
        #screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        #window name
        pygame.display.set_caption("CONNECT FOUR")
        
        self.board_width = self.column_count * self.square_size #VERIFICADO
        self.board_height = self.row_count * self.square_size

        # Calculate the starting position to center the board
        self.start_x = (self.width - self.board_width) // 2
        self.start_y = (self.height + 50 - self.board_height) // 2 #VERIFICADO

    def draw_board(self):
        #draw circles 
        for row in range(self.game_board.rows - 1, -1, -1):
            for column in range(self.game_board.cols):
                circle = Piece()
                circle_x = self.start_x + (column * self.square_size) + (self.square_size // 2)
                circle_y = self.start_y + (row * self.square_size) + (self.square_size // 2)
                symbol = self.game_board.board[row][column]
                circle.draw(self.screen, circle_x, circle_y, symbol)
                
        #draw grid
        for i in range(self.game_board.rows + 1):
            # Horizontal lines
            pygame.draw.line(self.screen, self.colors['GRILL'], (self.start_x, self.start_y + i * self.square_size),
                             (self.start_x + self.board_width, self.start_y + i * self.square_size), 3)
            
        for j in range(self.game_board.cols + 1):
            # Vertical lines
            pygame.draw.line(self.screen, self.colors['GRILL'], (self.start_x + j * self.square_size, self.start_y),
                             (self.start_x + j * self.square_size, self.start_y + self.board_height), 3)
       
                
        pygame.display.update()
            
    def convert_mouse_to_board_pos(self, x, y):
    # Ajustar para o início da grade do tabuleiro
        x -= self.start_x
        y -= self.start_y

        # Encontrar a coluna
        column = x // self.square_size

        # Encontrar a linha
        row = y // self.square_size

        return row, column


    def run_game(self):
        click = pygame.mouse.get_pressed()
        running = True
        while running:
            self.draw_board()
            for event in pygame.event.get():
                # close game manually
                if event.type == pygame.QUIT:
                    running = False
                # close game using ESC
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                # mouse touches
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        x, y = pygame.mouse.get_pos()
                        row, column = self.convert_mouse_to_board_pos(x, y)
                        print(f'{row}, {column}')
                        # Handle the click here, e.g., updating the board
                        self.game_board.addToCollumn(column, 'X')
                        print(self.game_board)
                        self.draw_board()
            
                    
            self.screen.fill(self.colors['BACKGROUND'])
        pygame.quit()
