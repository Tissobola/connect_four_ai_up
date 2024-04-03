from time import sleep
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw
    
import src.common.board as board


collumn_count = 7
row_count = 6
square_size = 100

# Set the dimensions of the screen
width = collumn_count * square_size 
height = (row_count + 1) * square_size


colors = {
    "BLUE": (0, 0, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "YELLOW": (255, 255, 0),
    "WHITE": (255, 255, 255),
    "BACKGROUND": (230, 191, 131),
    "GRILL": (193, 154, 107),
    "EMPTY": (230, 230, 230)
    }


def draw_hover_piece(screen, current_player, column, piece_surface):
    if current_player == 'X':
        color = colors["RED"]
    else:
        color = colors["BLUE"]

    center_x = (column * square_size) + (square_size // 2)
    center_y = square_size // 2

    piece_surface.fill((0, 0, 0, 0))
    pygame.gfxdraw.aacircle(piece_surface, square_size // 2, square_size // 2,
                            square_size // 2 - 5, color)
    pygame.gfxdraw.filled_circle(piece_surface, square_size // 2, square_size // 2,
                                 square_size // 2 - 5, color)

    screen.blit(piece_surface, (center_x - square_size // 2, center_y - square_size // 2))



def draw_board(game, screen):
    def draw_pieces():
        def draw(color):
            pygame.gfxdraw.aacircle(screen, c * square_size + square_size // 2,
                                    (game.rows - r) * square_size + square_size // 2,
                                    square_size // 2 - 5, color)
            pygame.gfxdraw.filled_circle(screen, c * square_size + square_size // 2,
                                         (game.rows - r) * square_size + square_size // 2,
                                         square_size // 2 - 5, color)

        for c in range(game.cols):
            for r in range (game.rows):
                draw(colors["WHITE"])
                if game.board[r][c] == 'X':
                    draw(colors["RED"])
                elif game.board[r][c] == 'O':
                    draw(colors["BLUE"])
                    
        
        

    if game.end:
       
        font = pygame.font.Font(None, 64)
        if game.winner == 'X':
            winner_text = font.render("Red wins!", True, colors["RED"])
        elif game.winner == 'O':
            winner_text = font.render("Blue wins!", True, colors["BLUE"])
        else:
            winner_text = font.render("It's a tie!", True, colors["BLACK"])
        text_rect = winner_text.get_rect(center=(width // 2, square_size // 2))
        screen.blit(winner_text, text_rect)

        draw_pieces()
        pygame.display.update()
        pygame.time.delay(4000)
        exit()
    screen.fill(colors["BACKGROUND"])
    pygame.gfxdraw.box(screen, (0, 0, width, square_size), colors["WHITE"])
    draw_pieces()

def input_column():
    while True:
        column = input("Choose a column: ")
        if column.isdigit():
            column = int(column)
            if 1 <= column <= collumn_count:
                return column

def play_on_terminal(game, verbose=True):
    while True:
        if verbose:
            print(game)
            if game.end:
                if game.winner == 'X':
                    print("Red wins!")
                elif game.winner == 'O':
                    print("Blue wins!")
                else:
                    print("It's a tie!")
                break
            elif game.turn == 1:
                print("Blue's turn")
                if game.algorithm2 is None:
                    column = input_column()
                else:
                    column = algorithms_move(game, game.algorithm1)
                    sleep(0.5)
                if not game.move(column, game.turn):
                    print("Invalid move")
            else:
                print("Red's turn")
                if game.algorithm2 is None:
                    if game.algorithm1 is None:
                        column = input_column()
                    else:
                        column = algorithms_move(game, game.algorithm1)
                        sleep(0.5)
                else:
                    column = algorithms_move(game, game.algorithm2)
                    sleep(0.5)
                if not game.move(column, game.turn):
                    print("Invalid move")
                print()
        else:
            if not game.end:
                if game.turn == 2:
                    game.move(algorithms_move(game, game.algorithm1))
                else:
                    game.move(algorithms_move(game, game.algorithm2))

def play_game(game):
    
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(60)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Connect 4 - player vs ' + str(game.algorithm1))

    while not game.end:
        draw_board(game, screen)
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            draw_hover_piece(screen, game.player(game.turn), pygame.mouse.get_pos()[0] // square_size,
                             pygame.Surface((square_size, square_size), pygame.SRCALPHA))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // square_size
            if game.move(column + 1, game.turn):
                if not game.end and game.algorithm1 is not None:
                    draw_board(game, screen)
                    pygame.display.update()
                    algorithms_move(game, game.algorithm1)
        pygame.display.update()
        
    draw_board(game, screen)
    

def algorithm_vs_algorithm(game):
    pygame.init()
    clock = pygame.time.Clock() 
    clock.tick(60)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Connect 4 - ' + str(game.algorithm1) + ' vs ' + str(game.algorithm2))

    draw_board(game, screen)
    pygame.display.update()
    
    while True:
        draw_board(game, screen)
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            exit()
            
        # print(game.turn)
        if game.turn == 1:
            algorithms_move(game, game.algorithm1)
        elif game.turn == 2:
            algorithms_move(game, game.algorithm2)
        
        draw_board(game, screen)
        pygame.time.delay(100)
        pygame.display.update()


import src.a_star.astar_h2 as astar_h2
import src.a_star.astar_h1 as astar_h1
import src.mcts.montecarlo as montecarlo
import src.minimax.minimax as minimax
import src.alphabeta.alphabeta as alphabeta
    
def algorithms_move(game_board, algorithm):
    if algorithm=="astar_h1":
        bot = astar_h1.AStarBot(game_board, game_board.turn)
        bot.play()
    elif algorithm=="astar_h2":
        bot = astar_h2.AStarBot(game_board, game_board.turn)
        bot.play()
    elif algorithm=="montecarlo":
        bot = montecarlo.MonteCarlo(game_board, game_board.turn)
        bot.play()
    elif algorithm=="minimax":
        bot = minimax.MinimaxBot(game_board, game_board.turn)
        bot.play()
    elif algorithm=="alphabeta":
        bot = alphabeta.AlphaBeta(game_board)
        bot.play()
    elif algorithm == None:
        game_board.move(int(input()), game_board.turn)

def main(game, algorithm1, algorithm2, GUI):
    game.algorithm1 = algorithm1
    game.algorithm2 = algorithm2

    if not GUI:
        play_on_terminal(game)
    else:
        if game.algorithm1 is not None:
                if game.algorithm2 is not None:
                    algorithm_vs_algorithm(game)
                else:
                    play_game(game)
        else:
            play_game(game)
            