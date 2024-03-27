import pygame 
from interface import *
from board import *

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
        self.width = 700
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Cambria', 35)
        self.button_font = pygame.font.SysFont('Arial', 15)
        self.menu_open = True
        self.colors = {'black': (0, 0, 0),
                       'white': ( 255, 255, 255),
                       'yellow': (255, 255, 0),
                       'red': (255, 0, 0),
                       'camel': (230, 191, 131),
                       'brown': (193, 154, 107)}
      
        self.player_vs_player_button = Button("PLAYER vs PLAYER", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 250, self.height // 2 - 25)
        self.astar_heuristic1_button = Button("A* (Heuristic 1)", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 250, self.height // 2 + 50)
        self.astar_heuristic2_button = Button("A* (Heuristic 2)", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 250, self.height // 2 + 125)
        self.monte_carlo_button = Button("Monte Carlo", 175, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 - 250, self.height // 2 + 200)
        self.mc_vs_h1 = Button("Monte Carlo vs A* (Heuristic 1)", 250, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 + 20, self.height // 2 + 200)
        self.mc_vs_h2 = Button("Monte Carlo vs A* (Heuristic 2)", 250, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 + 20, self.height // 2 + 125)
        self.h1_vs_h2 = Button("A* (Heuristic 1) vs A* (Heuristic 2)", 250, 50, self.button_font, self.colors['black'], self.colors['brown'], self.width // 2 + 20, self.height // 2 + 50)
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
                        elif self.astar_heuristic1_button.collide_point(pygame.mouse.get_pos()):
                            self.start_game_astar_h1()
                        elif self.astar_heuristic2_button.collide_point(pygame.mouse.get_pos()):
                            self.start_game_astar_h2()
                        elif self.monte_carlo_button.collide_point(pygame.mouse.get_pos()):
                            self.start_game_monte_carlo()
                        elif self.mc_vs_h1.collide_point(pygame.mouse.get_pos()):
                            self.start_mc_vs_h1()
                        elif self.mc_vs_h2.collide_point(pygame.mouse.get_pos()):
                            self.start_mc_vs_h2()
                        elif self.h1_vs_h2.collide_point(pygame.mouse.get_pos()):
                            self.start_h1_vs_h2()
                        
                            
                
                self.screen.fill(self.colors['camel']) 
                self.text("C O N N E C T    F O U R", self.colors['brown'], self.width // 2, self.height // 2 - 200)  
                self.player_vs_player_button.draw(self.screen)
                self.astar_heuristic1_button.draw(self.screen)
                self.astar_heuristic2_button.draw(self.screen)
                self.monte_carlo_button.draw(self.screen)
                self.mc_vs_h1.draw(self.screen)
                self.mc_vs_h2.draw(self.screen)
                self.h1_vs_h2.draw(self.screen)
                pygame.display.flip()

            pygame.quit()



    def start_game_interface(self):
        main(self.game_board, algorithm1=None, algorithm2=None, GUI= True)
    def start_game_astar_h1(self):
        main(self.game_board, algorithm1='astar_h1', algorithm2=None, GUI= True)
    def start_game_astar_h2(self):
        main(self.game_board, algorithm1='astar_h2', algorithm2=None, GUI= True)
    def start_game_monte_carlo(self):
        main(self.game_board, algorithm1='montecarlo', algorithm2=None, GUI= True)
    def start_mc_vs_h1(self):
        main(self.game_board, algorithm1='montecarlo', algorithm2='astar_h1', GUI= True)
    def start_mc_vs_h2(self):
        main(self.game_board, algorithm1='montecarlo', algorithm2='astar_h2', GUI= True)
    def start_h1_vs_h2(self):
        main(self.game_board, algorithm1='astar_h1', algorithm2='astar_h2', GUI= True)
    
    



pygame.init()
menu = Menu()
menu.run()
