import pygame
import sys
from board import *

class Board_Interface:
    def __init__(self, row_count, column_count, square_size, board):
        self.row_count = row_count
        self.column_count = column_count
        self.square_size = square_size
        self.radius = int(square_size / 2 - 5)
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
        
        self.board_width = self.column_count * self.square_size
        self.board_height = self.row_count * self.square_size

        # Calculate the starting position to center the board
        self.start_x = (self.width - self.board_width) // 2
        self.start_y = (self.height + 100 - self.board_height) // 2

    def draw_board(self):
        # draw grid
        for i in range(self.game_board.rows + 1):
            # Horizontal lines
            pygame.draw.line(self.screen, self.colors['GRILL'], (self.start_x, self.start_y + i * self.square_size),
                             (self.start_x + self.board_width, self.start_y + i * self.square_size), 3)
            
        for j in range(self.game_board.cols + 1):
            # Vertical lines
            pygame.draw.line(self.screen, self.colors['GRILL'], (self.start_x + j * self.square_size, self.start_y),
                             (self.start_x + j * self.square_size, self.start_y + self.board_height), 3)
        #drawing inicial state
        for i in range(self.game_board.rows):
            for j in range(self.game_board.cols):
                if self.game_board.board[i][j] == '.':
                    circle_x = self.start_x + (j * self.square_size) + (self.square_size // 2)
                    circle_y = self.start_y + (i * self.square_size) + (self.square_size // 2)
                    pygame.draw.circle(self.screen, self.colors['EMPTY'], (circle_x, circle_y), self.radius)
        

                    
                #drawingboard 
                #pygame.draw.rect(self.screen, self.GRILL, (i * self.square_size, (j + 1) * self.square_size, self.square_size, self.square_size), 3)
                
        pygame.display.update()

    def run_game(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
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
                        x, y = event.pos
                        for i in range(self.game_board.rows):
                            for j in range(self.game_board.cols):
                                circle_x = self.start_x + (j * self.square_size) + (self.square_size // 2)
                                circle_y = self.start_y + (i * self.square_size) + (self.square_size // 2)
                                distance = ((circle_x - x) ** 2 + (circle_y - y) ** 2) ** 0.5
                                if distance <= self.radius:
                                    print(f"Clicked on position [{i}, {j}]")
                                    # Handle the click here, e.g., updating the board
                                    self.game_board = self.game_board.addToCollumn(i, 'X')
                                    self.draw_board()
                        
                    
            self.screen.fill(self.colors['BACKGROUND'])
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    game = Board_Interface(6, 7, 100, board)
    game.run_game()


class Piece:
    def __init__(self, square_size):
        self.radius = int(square_size / 2 - 5)
    
    def draw(self, screen, column, row, square_size, symbol):
        x = int(column * square_size + square_size // 2)
        y = int(row * square_size + square_size // 2 + square_size)
        if symbol == 'X': 
            pygame.draw.circle(screen, (255, 0, 0), (x, y), self.radius)
        elif symbol == 'O':
            pygame.draw.circle(screen,(255, 255, 0), (x, y), self.radius)

game_board = board.Board()

game = Board_Interface(6, 7,100, game_board)

game.run_game()