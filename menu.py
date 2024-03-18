import pygame 
from interface import *
from board import *
import heuristic

class Button:
    def __init__(self, text, width, height, font, text_color, backgroud_color, x_pos, y_pos):
        self.text = text
        self.width = width
        self.height = height
        self.font = font
        self.text_color = text_color
        self.background_color = backgroud_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.colors = {'black': (0, 0, 0),
                       'white': ( 255, 255, 255),
                       'yellow': (255, 255, 0),
                       'red': (255, 0, 0),
                       'camel': (230, 191, 131),
                       'brown': (193, 154, 107)}
        self.rect = pygame.Rect(x_pos, y_pos, width, height)


    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, (self.x_pos, self.y_pos, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.colors['black'])
        text_rect = text_surface.get_rect(center=(self.x_pos + self.width / 2, self.y_pos + self.height / 2))

        screen.blit(text_surface, text_rect)


    def collide_point(self, pos):
        return self.rect.collidepoint(pos)
  


class Menu:
    def __init__(self):
        self.width = 1024
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Cambria', 35)
        self.button_font = pygame.font.SysFont('Arial', 15)
        self.menu_open = True
        self.colors = {'black': (0, 0, 0),
                       'white': (255, 255, 255),
                       'yellow': (255, 255, 0),
                       'red': (255, 0, 0),
                       'camel': (230, 191, 131),
                       'brown': (193, 154, 107)}
      
        self.player_vs_player_button = Button("PLAYER vs PLAYER", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 100, self.height // 2 - 25)
        self.astar_button = Button("A*", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 100, self.height // 2 + 50)
        self.monte_carlo_button = Button("Monte Carlo", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 100, self.height // 2 + 125)
        self.game_board = Board()
    def setup(self):
        self.screen.fill(self.colors['camel'])
        pygame.display.set_caption("Connect Four Game")

    def text(self, message, text_color, x_pos, y_pos):
        text = self.font.render(message, True, self.colors['black'])
        text_rect = text.get_rect(center=(x_pos, y_pos))
        self.screen.blit(text, text_rect)
    

    def run(self):
            self.setup()
            while self.menu_open:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.menu_open = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.player_vs_player_button.collide_point(pygame.mouse.get_pos()):
                            self.start_game_interface()
                        elif self.astar_button.collide_point(pygame.mouse.get_pos()):
                            self.start_game_interface_astart()
                        
                            
                
                self.screen.fill(self.colors['camel']) 
                self.text("C O N N E C T    F O U R", self.colors['brown'], self.width // 2, self.height // 2 - 200)  
                self.player_vs_player_button.draw(self.screen)
                self.astar_button.draw(self.screen)
                self.monte_carlo_button.draw(self.screen)
                pygame.display.flip()

            pygame.quit()



    def start_game_interface(self):
        game_interface = Board_Interface (self.game_board.rows, self.game_board.cols, 100, self.game_board)
        game_interface.run_game()
    
    def start_game_interface_astar(self):
        game_board = Board()
        bot = heuristic.AStarBot(game_board, 2)
        game_interface = Board_Interface (self.game_board.rows, self.game_board.cols, 100, self.game_board)
        game_interface.run_game()
    



pygame.init()
menu = Menu()
menu.run()
