import tree 
import board
import utils as util

#h(n): minimize the chances of the opponent to win and maximize the chances of the bot to win
#g(n): uniform cost search minimizes the cost of the path from the root to the current n
#f(n) = h(n) + g(n)

class AStarBot:
    def __init__(self, board, player):
        self.board = board      # board object
        self.player = player    # 1 or 2

    def play(self):
        movesTree = tree.AStarTree(self.board, self.player)
        forbiddenMove = []
        while True:
            bestMove = self.bestMove(movesTree, [])
            if not self.board.move(bestMove[0], self.player):
                forbiddenMove.append(bestMove[0])
            else:
                return True

    def bestMove(self, movesTree, forbidenMoves):   # movesTree is the tree of different moves, forbidenMoves is a list of positions to which it shouldn't make a move
        print("entrou")
        print("key = ", movesTree.root.children[0])
        bestMove = (1, self.f(movesTree.root.children[0]))
        for i in movesTree.root.children:
            if not forbidenMoves.__contains__(i+1):
                print(f'children {i}:\n {movesTree.root.children[i].value}')
                f = self.f(movesTree.root.children[i])
                print(f'pontuacao:{f}')
                if f < bestMove[1]:
                    bestMove = (i+1, f)
        return bestMove
 
    def f(self, node):
        return self.h(node) + self.g()

    def g(self):
        return 1
    
    def evaluate_segment(self, segment):
        count_x = segment.count('X')
        count_o = segment.count('O')
        if count_o == 3 and count_x == 0:
            return -50
        elif count_o == 2 and count_x == 0:
            return -10
        elif count_o == 1 and count_x == 0:
            return -1
        elif count_x == 1 and count_o == 0:
            return 1
        elif count_x == 2 and count_o == 0:
            return 10
        elif count_x == 3 and count_o == 0:
            return 50
        elif count_x == 4:
            return 512
        elif count_o == 4:
            return -512
        else:
            return 0

    def h(self, node):
        score = 0
        # Count occurrences of 'X' and 'O' in the node
        for i in range(self.board.rows):
            for j in range(self.board.cols):        
                # Horizontal segments
                if j <= self.board.cols - 4:
                    segment = [node.value.board[i][j+k] for k in range(4)]
                    score += self.evaluate_segment(segment)
                    
                # Vertical segments
                if i <= self.board.rows - 4:
                    segment = [node.value.board[i+k][j] for k in range(4)]
                    score += self.evaluate_segment(segment)

                # Diagonal segments (top-left to bottom-right)
                if i <= self.board.rows - 4 and j <= self.board.cols - 4:
                    segment = [node.value.board[i+k][j+k] for k in range(4)]
                    score += self.evaluate_segment(segment)

                # Diagonal segments (bottom-left to top-right)
                if i >= 3 and j <= self.board.cols - 4:
                    segment = [node.value.board[i-k][j+k] for k in range(4)]
                    score += self.evaluate_segment(segment)

                # Move bonus for player
                if self.board.turn == 1:
                    score += 16
                elif self.board.turn == 2:
                    score -= 16
                    
        return score