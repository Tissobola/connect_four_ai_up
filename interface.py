import pygame
import sys

class ConnectFour:
    def __init__(self, row_count, column_count, square_size):
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
        self.BACKGROUND = (230, 191, 131)
        self.board = [[0] * column_count for _ in range(row_count)]
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("CONNECT FOUR")

    def draw_board(self):
        for i in range(self.column_count):
            for j in range(self.row_count):
                pygame.draw.circle(self.screen, self.BLACK, (i * self.square_size + self.square_size // 2,
                                                              j * self.square_size + self.square_size // 2 + self.square_size), self.radius)
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


if __name__ == "__main__":
    pygame.init()
    game = ConnectFour(6, 7, 100)
    game.run_game()


class CircleO:
    def __init__(self, square_size):
        self.radius = int(square_size / 2 - 5)
        self.YELLOW = (255, 255, 0)

    def draw(self, screen, column, row, square_size):
        x = int(column * square_size + square_size // 2)
        y = int(row * square_size + square_size // 2 + square_size)
        pygame.draw.circle(screen, self.YELLOW, (x, y), self.radius)


class CircleX:
    def __init__(self, square_size):
        self.radius = int(square_size / 2 - 5)
        self.RED = (255, 0, 0)

    def draw(self, screen, column, row, square_size):
        x = int(column * square_size + square_size // 2)
        y = int(row * square_size + square_size // 2 + square_size)
        pygame.draw.circle(screen, self.RED, (x, y), self.radius)
