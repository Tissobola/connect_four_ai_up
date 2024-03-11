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
        movesTree = tree.Tree(self.board, self.player)
        best_move = (4, self.f(movesTree.root.children[3]))
        for i in movesTree.root.children:
            f = self.f(movesTree.root.children[i])
            g = self.g(movesTree.root.children[i])
            h = self.h(movesTree.root.children[i])
            # print(i+1, f, "=", h, "+", g)
            if f < best_move[1]:
                # print("esse")
                best_move = (i+1, f)
        self.board.move(best_move[0], self.player)
        
    def f(self, node):
        return self.h(node) + self.g(node)
    
    def g(self, node):
        currentBoard = node.value
        newConsecutives = []
        newConsecutives.append(self.checkRows(currentBoard, self.player))
        newConsecutives.append(self.checkCols(currentBoard, self.player))
        newConsecutives.append(self.checkDiagonalsUpLeftToRight(currentBoard, self.player))
        # print(self.checkDiagonalsUpLeftToRight(currentBoard, self.player))
        newConsecutives.append(self.checkDiagonalsDownLeftToRight(currentBoard, self.player))
        # print(self.checkDiagonalsDownLeftToRight(currentBoard, self.player))
        for i in range(len(newConsecutives)):
            for ii in range(len(newConsecutives)-1, -1, -1):
                if newConsecutives[i][ii] != 0:
                    return 4 - ii
    
    def countPieces(self, board):
        counter = 0
        for line in board:
            for i in range(len(line)):
                if line[i] == self.player:
                    counter += 1
        return counter
    
    def h(self, node):
        currentBoard = node.value
        selfConsecutives = []
        selfConsecutives.append(self.checkRows(currentBoard, self.player))
        selfConsecutives.append(self.checkCols(currentBoard, self.player))
        selfConsecutives.append(self.checkDiagonalsUpLeftToRight(currentBoard, self.player))
        selfConsecutives.append(self.checkDiagonalsDownLeftToRight(currentBoard, self.player))
        opponentConsecutives = []
        opponentConsecutives.append(self.checkRows(currentBoard, self.opponent()))
        opponentConsecutives.append(self.checkCols(currentBoard, self.opponent()))
        opponentConsecutives.append(self.checkDiagonalsUpLeftToRight(currentBoard, self.opponent()))
        opponentConsecutives.append(self.checkDiagonalsDownLeftToRight(currentBoard, self.opponent()))
        results = [0, 0, 0, 0]
        for i in range(len(selfConsecutives)):
            for ii in range(len(selfConsecutives)):
                results[ii] += ii*opponentConsecutives[i][ii] - ii*selfConsecutives[i][ii]          # multiplies the number of consecutive pieces(-1) and the number of sequences with that many pieces
                # results[ii] += (ii+1)*opponentConsecutives[i][ii] - (ii+1)*selfConsecutives[i][ii]     # multiplies the number of consecutive pieces and the number of sequences with that many pieces
        return sum(results)

    def checkRows(self, currentBoard, currentPlayer):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(currentBoard)):
                for c in range(len(currentBoard[0])):
                    if currentBoard[r][c] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[r][c] != self.board.player(self.opponent()):
                                if counter == i:
                                    consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
    
    def checkCols(self, currentBoard, currentPlayer):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            for c in range(len(currentBoard[0])):
                inSequence = False
                counter = 0
                for r in range(len(currentBoard)):
                    if currentBoard[r][c] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[r][c] != self.board.player(self.opponent()):
                                if counter == i:
                                    consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
    
    def checkDiagonalsUpLeftToRight(self, currentBoard, currentPlayer):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(currentBoard)):
                for s in range(len(currentBoard)):
                    if ((s+r > len(currentBoard) - 1 - r) or (s > len(currentBoard))):
                        break
                    if currentBoard[r+s][s] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[r+s][s] != self.board.player(self.opponent()):
                                if counter == i:
                                    consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
            inSequence = False
            counter = 0
            for r in range(len(currentBoard)-1, -1, -1):
                for s in range(len(currentBoard)):
                    aux = len(currentBoard)-r+s
                    if((s > r) or (aux > len(currentBoard))):
                        break
                    if currentBoard[s][aux] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[s][aux] != self.board.player(self.opponent()):
                                if counter == i:
                                    consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
    
    def checkDiagonalsDownLeftToRight(self, currentBoard, currentPlayer):
        consecutives = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            inSequence = False
            counter = 0
            for r in range(len(currentBoard)):
                for s in range(r+1):
                    if currentBoard[r-s][s] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[r-s][s] != self.board.player(self.opponent()):
                                if counter == i:
                                    consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
            inSequence = False
            counter = 0
            for r in range(len(currentBoard)):
                for s in range(len(currentBoard)):
                    aux = r+s
                    aux2 = len(currentBoard)-s+r
                    if (aux > len(currentBoard)-1):
                        aux = len(currentBoard)-1
                    if (aux2 > 6):
                        aux2 = 6
                    if currentBoard[aux][aux2] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[aux][aux2] != self.board.player(self.opponent()):
                                if counter == i:
                                    consecutives[i-1] += 1
                        counter = 0
                        inSequence = False
                if inSequence:
                    if counter == i:
                        consecutives[i-1] += 1
                counter = 0
                inSequence = False
        return consecutives
                        
    def opponent(self):
        if self.player == 1:
            return 2
        elif self.player == 2:
            return 1