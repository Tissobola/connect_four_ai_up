import board
from tree import Node
import copy

class MinimaxBot:
    def __init__(self, board):
        self.board = board
        # self.player = player
    

    
    def get_possible_moves(self, node, player):
        possible_moves = {}
        for col in range(node.cols):
            new_board = copy.deepcopy(node)
            if new_board.move(col + 1, player):
                possible_moves[col] = new_board
        #self.board.change_player()
        return possible_moves
    

    
    def play(self):
        
        column, score = self.minimax(self.board, 5, True)
       
            # column, score = self.minimax(self.board, 5, False)
        # print("player = ", self.board.turn)
        print("JOGADA : ", column + 1)
        print("SCORE : ", score)
        # print("player ANTES do move = ", self.board.turn)
        self.board.move(column + 1, self.board.turn)  # Adjust for 1-based indexing
        # print("player DEPOIS do move = ", self.board.turn)

        return True

    def minimax(self, node, depth, maximizingPlayer):

        if depth == 0 or self.board.is_terminal:
            return None, self.board.heuristic(node)

        if maximizingPlayer:
            # print("player maximinzingPlayer = ", self.board.turn)
            maxEval = float('-inf')
            bestColumn = None
            oponent = 3 - self.board.turn
            possible_moves = self.get_possible_moves(node, oponent)
            
            if len(possible_moves) == 0: 
                self.board.is_terminal = True
            for i, child in possible_moves.items():
                print(f"sucessor {i}\n: {child}")
                _, value_current_board = self.minimax(child, depth - 1, False)
                print("value_current_board : ", value_current_board)
                if value_current_board > maxEval:
                    maxEval = value_current_board
                    # print("max Eval = ", maxEval)
                    bestColumn = i
                    # print("MAX bestColumn = ", bestColumn + 1)
            return bestColumn, maxEval
        
        else:  # Minimizing player
            # print("player minimizingPlayer= ", self.board.turn)
            minEval = float('inf')
            bestColumn = None
            oponent = 3 - self.board.turn
            possible_moves = self.get_possible_moves(node, self.board.turn)
            if len(possible_moves) == 0: 
                self.board.is_terminal = True
            for i, child in possible_moves.items():
                print(f"sucessor {i}\n: {child}")
                _, value_current_board = self.minimax(child, depth - 1, True)
                print("value_current_board : ", value_current_board)
                if value_current_board < minEval:
                    minEval = value_current_board
                    print("min Eval = ", minEval)
                    bestColumn = i
                    # print("MIN bestColumn = ", bestColumn + 1 )
            return bestColumn, minEval
    