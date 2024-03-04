import tree
import board

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
        current_board = node.value
        consecutives = []
        consecutives.append(self.checkRows(current_board))
        consecutives.append(self.checkCols(current_board))
        consecutives.append(self.checkDiagonalsUpLeftToRight(current_board))
        consecutives.append(self.checkDiagonalsDownLeftToRight(current_board))
        results = [0, 0, 0, 0]
        for i in range(len(consecutives)):
            print(consecutives[i])
            # for ii in range(len(consecutives)):
                # results[ii] += consecutives[i][ii]

    def checkRows(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(current_board)):
                for c in range(len(current_board[0])):
                    if current_board[r][c] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        # if current_board[r][c] == self.board.nullSymbol:
                        #     break
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
    
    def checkCols(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            for c in range(len(current_board[0])):
                inSequence = False
                counter = 0
                for r in range(len(current_board)):
                    if current_board[r][c] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        # if current_board[r][c] == self.board.nullSymbol: #Verify behavior later
                        #     break
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
    
    def checkDiagonalsUpLeftToRight(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(current_board)):
                for s in range(len(current_board)):
                    if ((s+r > len(current_board) - 1 - r) or (s > len(current_board))):
                        break
                    if current_board[r+s][s] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        # if current_board[r+s][s] == self.board.nullSymbol:
                        #     break
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
            inSequence = False
            counter = 0
            for r in range(len(current_board)-1, -1, -1):
                for s in range(len(current_board)):
                    aux = len(current_board)-r+s
                    if((s > r) or (aux > len(current_board))):
                        break
                    if current_board[s][aux] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        # if current_board[s][c+s] == self.board.nullSymbol:
                        #     break
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
    
    def checkDiagonalsDownLeftToRight(self, current_board):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(current_board)):
                for s in range(r+1):
                    if current_board[r-s][s] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        # if current_board[r-s][s] == self.board.nullSymbol:
                        #     break
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
            inSequence = False
            counter = 0
            for r in range(len(current_board)):
                for s in range(len(current_board)):
                    aux = r+s
                    aux2 = len(current_board)-s+r
                    if (aux > len(current_board)-1):
                        aux = len(current_board)-1
                    if (aux2 > 6):
                        aux2 = 6
                    if current_board[aux][aux2] == self.board.player(self.player):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if counter == i:
                                consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                        # if current_board[r+s][len(current_board)-s] == self.board.nullSymbol:
                        #     break
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
                        
    def opponent(self, player):
        if player == 1:
            return 2
        elif player == 2:
            return 1