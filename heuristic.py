import board

#h(n): estimated cost of the minimum path between the current state and the objective
#g(n): uniform cost search minimizes the cost of the path from the root to the current n
#f(n) = h(n) + g(n)

class AStarBot:
    def __init__(self, board):
        self.board = board
        
    def play(self):
        self.board.move()
        
    def f(self, node):
        return self.h(node) + self.g(node)
    
    def g(self, node):
        return 0
    
    def h(self, node):
        return 0