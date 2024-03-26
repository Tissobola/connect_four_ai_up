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
        best_f = float('inf')
        node = tree.Node_astar(self.board, {})
   
        self.get_successors(node)
        for col in node.children:
            f_value = self.f()
            if f_value < best_f:
                best_f = f_value
                a_star_col = col
        node.value.move(a_star_col, node.value.turn)
        
    def get_successors(self, node):
        matrix = node.value
        for i in range (matrix.cols):
            if matrix.move(i + 1, node.value.turn):
                node.children[i] = matrix.move(i + 1, node.value.turn)
        


    

    def f(self):
        return self.h() + self.g()

    def g(self):
        return 1
    
  
    def h(self):
        def evaluate_segment(segm):
            if self.winner == "X":
                return 512
            elif self.winner == "O":
                return -512

            elif "O" in segm and "X" not in segm:
                if segm.count("O") == 3:
                    return -50
                elif segm.count("O") == 2:
                    return -10
                elif segm.count("O") == 1:
                    return -1
            elif segm.count("-") == 4:
                return 0
            elif "X" in segm and "O" not in segm:
                if segm.count("X") == 1:
                    return 1
                elif segm.count("X") == 2:
                    return 10
                elif segm.count("X") == 3:
                    return 50
            return 0

        # Evaluate all possible straight segments
        self.score = 0
        for i in range(6):
            for j in range(4):
                if j + 3 < 7:  # check if the indices are within range
                    segment = [self.board[i][j + k] for k in range(4)]
                    self.score += evaluate_segment(segment)
        for i in range(4):
            for j in range(7):
                if i + 3 < 6:  # check if the indices are within range
                    segment = [self.board[i + k][j] for k in range(4)]
                    self.score += evaluate_segment(segment)
        for i in range(3):
            for j in range(4):
                if i + 3 < 6 and j + 3 < 7:  # check if the indices are within range
                    segment = [self.board[i + k][j + k] for k in range(4)]
                    self.score += evaluate_segment(segment)
        for i in range(3):
            for j in range(3, 7):
                if i + 3 < 6 and j - 3 >= 0:  # check if the indices are within range
                    segment = [self.board[i + k][j - k] for k in range(4)]
                    self.score += evaluate_segment(segment)

        return self.score