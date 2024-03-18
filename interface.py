import pygame
import sys
from board import *


# Class to create the game pieces 
class Piece:
    def __init__(self):
        self.square_size = 100
        self.radius = int(self.square_size / 2 - 5)
    
    def draw(self, screen, x, y, symbol):
        if symbol == 'X': 
            pygame.draw.circle(screen, (255, 0, 0), (x, y), self.radius)
        elif symbol == 'O':
            pygame.draw.circle(screen,(0, 0, 139), (x, y), self.radius)
        elif symbol == '.':
            pygame.draw.circle(screen,(255, 255, 255), (x, y), self.radius)


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
        
        self.clock = pygame.time.Clock()
        
        self.board_width = self.column_count * self.square_size #VERIFICADO
        self.board_height = self.row_count * self.square_size

        # Calculate the starting position to center the board
        self.start_x = (self.width - self.board_width) // 2
        self.start_y = (self.height - self.board_height + 50) // 2 #VERIFICADO

    def draw_board(self):
        #draw circles 
        for row in range(self.game_board.rows):
            for column in range(self.game_board.cols):
                circle = Piece()
                circle_x = self.start_x + (column * self.square_size) + (self.square_size // 2)
                circle_y = self.start_y + ((self.game_board.rows - row - 1) * self.square_size) + (self.square_size // 2)
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
        column = (x // self.square_size) + 1

        # Encontrar a linha
        row = y // self.square_size

        return row, column
    
    def win_text(self, color):
        font = pygame.font.Font(None, 36)  
        text = font.render(f"Player {color} wins!", True, self.colors[color])  
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))  
        background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)
        pygame.draw.rect(self.screen, (255, 255, 255), background_rect)
        self.screen.blit(text, text_rect)  #draw the win text
            
    def run_game(self):
        click = pygame.mouse.get_pressed()
        running = True
        game_turn = 1
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
                        # Handle the click here, e.g., updating the board
                        print(f'{column}')
                        if game_turn == 1:
                            self.game_board.move(column, game_turn)
                            if self.game_board.checkWinner('X', (row, column -1)):
                                print("Entrei")
                                self.draw_board()
                                #win text -> red 
                                self.win_text("RED")
                                
                                pygame.display.flip() 
                                pygame.time.delay(500)
                                
                                running = False
                                
                            game_turn = 2
                        else: 
                            self.game_board.move(column, game_turn)
                            
                            if self.game_board.checkWinner('O', (row, column-1)):
                                self.draw_board()
                                
                                self.win_text("BLUE")
                                
                                pygame.display.flip()
                                
                                pygame.time.delay(500)
                                running = False  
                                
                            
                            game_turn = 1
                        
                        
                        print(self.game_board)
            
                    
            self.screen.fill(self.colors['BACKGROUND'])
        pygame.quit()
