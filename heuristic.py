import board
import tree

#h(n): minimize the chances of the opponent to win and maximize the chances of the bot to win
#g(n): uniform cost search minimizes the cost of the path from the root to the current n
#f(n) = h(n) + g(n)

class AStarBot:
    def __init__(self, board, player):
        self.board = board      # board object
        self.player = player    # 1 or 2
        
    def play(self):
        self.board.move()
        
    def f(self, node):
        return self.h(node) + self.g(node)
    
    def g(self, node):
        return 0
    
    def h(self, node):
        current_board = node.board
        
    def checkRows(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for ii in range(len(current_board)):
                for iii in range(len(current_board[0])):
                    if current_board[ii][iii] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        if current_board[ii][iii] == self.board.nullSymbol:
                            break
        return consecutives
    
    def checkCols(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for ii in range(len(current_board[0])):
                for iii in range(len(current_board)):
                    if current_board[iii][ii] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        if current_board[iii][ii] == self.board.nullSymbol: #Verify behavior later
                            break
        return consecutives
    
    def checkDiagonalsUpLeftToRight(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(current_board)):
                for s in range(r):
                    if current_board[r+s][s] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        if current_board[r+s][s] == self.board.nullSymbol:
                            break
            for c in range(1, len(current_board[0])):
                for s in range(len(current_board[0]) - c):
                    if current_board[s][c+s] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        if current_board[s][c+s] == self.board.nullSymbol:
                            break
        return consecutives
    
    def checkDiagonalsDownLeftToRight(self, current_board):             #TODO
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(current_board)):
                for s in range(r):
                    if current_board[r+s][s] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        if current_board[r+s][s] == self.board.nullSymbol:
                            break
        return consecutives
                        
    def opponent(self, player):
        if player == 1:
            return 2
        elif player == 2:
            return 1