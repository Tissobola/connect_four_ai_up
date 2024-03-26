import tree
import board_old

class MiniMax:
    def __init__(self, board, player):
        self.board = board
        self.player = player
    

    def minimax(self, node, depth, maxPlayer):
        if depth == 0 or self.board.game_end():
            return self.evaluate(node.value)

        if maxPlayer:
            maxEval = float('-inf')
            for child in tree.Node.children:
                eval = self.minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = float('inf')
            for child in node.children.values():
                eval = self.minimax(child, depth - 1, True)
                minEval = min(minEval, eval)
            return minEval
'''
    def best_move(self, depth):
        best_score = float('-inf')
        best_move = None
        for move, child in self.root.children.items():
            score = self.minimax(child, depth, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move'''
    

   