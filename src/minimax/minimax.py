import src.common.board as board
from src.common.tree import Node
import copy

class MinimaxBot:
    def __init__(self, board, player):
        self.board = board
        self.player = player
    

    
    def get_possible_moves(self, node, player):
        possible_moves = {}
        for col in range(node.cols):
            new_board = copy.deepcopy(node)
            if new_board.move(col + 1, player):
                possible_moves[col] = new_board
        return possible_moves
    

    
    def play(self):
        
        if self.player == 2:
            maximizingPlayer = True
        else:
            maximizingPlayer = False

        column, score = self.minimax(self.board, 5, maximizingPlayer)
        
        if column == None:
            column = self.board.possibleMoves[0]
        self.board.move(column + 1, self.board.turn)  # Adjust for 1-based indexing

        return True

    def minimax(self, node, depth, maximizingPlayer):

        if depth == 0 or self.board.is_terminal:
            return None, self.board.heuristic(node)

        if maximizingPlayer:
            maxEval = float('-inf')
            bestColumn = None
            oponent = 3 - self.board.turn
            possible_moves = self.get_possible_moves(node, oponent)
            
            if len(possible_moves) == 0: 
                self.board.is_terminal = True
            for i, child in possible_moves.items():
                _, value_current_board = self.minimax(child, depth - 1, False)
                if value_current_board > maxEval:
                    maxEval = value_current_board
                    bestColumn = i
            return bestColumn, maxEval
        
        else:  # Minimizing player
            minEval = float('inf')
            bestColumn = None
            oponent = 3 - self.board.turn
            possible_moves = self.get_possible_moves(node, self.board.turn)
            if len(possible_moves) == 0: 
                self.board.is_terminal = True
            for i, child in possible_moves.items():
                _, value_current_board = self.minimax(child, depth - 1, True)
                if value_current_board < minEval:
                    minEval = value_current_board
                    bestColumn = i
            return bestColumn, minEval
    


    