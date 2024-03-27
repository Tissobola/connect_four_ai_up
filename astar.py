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
        bestMove = self.bestMove(movesTree)
        self.board.move(bestMove, self.player)

    def bestMove(self, movesTree):   # movesTree is the tree of different moves, forbidenMoves is a list of positions to which it shouldn't make a move
        bestMove = None
        for move in movesTree.root.children:
            f = self.f(movesTree.root.getChild(move))
            g = self.g()
            h = self.h(movesTree.root.getChild(move))
            # print(move, ":", f, "=", h, "+", g)
            if bestMove == None:
                if movesTree.root.children.__contains__(4):
                    bestMove = (4, self.f(movesTree.root.getChild(4)))
                else:
                    bestMove = (move, f)
            if f < bestMove[1]:
                # print("esse")
                bestMove = (move, f)
        return bestMove[0]

    def f(self, node):
        return self.h(node) + self.g()

    def g(self):
        return 1

    def h(self, node):
        currentBoard = node.value.board
        selfConsecutives = []
        selfConsecutives.append(self.checkRows(currentBoard, self.player))
        selfConsecutives.append(self.checkCols(currentBoard, self.player))
        selfConsecutives.append(self.checkDiagonalsUpLeftToRight(currentBoard, self.player))
        selfConsecutives.append(self.checkDiagonalsDownLeftToRight(currentBoard, self.player))
        opponentConsecutives = []
        opponentConsecutives.append(self.checkRows(currentBoard, util.opponent(self.player)))
        opponentConsecutives.append(self.checkCols(currentBoard, util.opponent(self.player)))
        opponentConsecutives.append(self.checkDiagonalsUpLeftToRight(currentBoard, util.opponent(self.player)))
        opponentConsecutives.append(self.checkDiagonalsDownLeftToRight(currentBoard, util.opponent(self.player)))
        results = [0, 0, 0, 0]
        for i in range(len(selfConsecutives)):
            for ii in range(1, len(selfConsecutives)):
                results[ii] += ((ii+1)**(ii+1))*(opponentConsecutives[i][ii] - selfConsecutives[i][ii])     # multiplies the number of consecutive pieces by the number of sequences with that many pieces
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
                            if currentBoard[r][c] != self.board.player(util.opponent(currentPlayer)):
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
                            if currentBoard[r][c] != self.board.player(util.opponent(currentPlayer)):
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
                            if currentBoard[r+s][s] != self.board.player(util.opponent(currentPlayer)):
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
                            if currentBoard[s][aux] != self.board.player(util.opponent(currentPlayer)):
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
                    if currentBoard[s][r-s] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[s][r-s] != self.board.player(util.opponent(currentPlayer)):
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
            for r in range(1, len(currentBoard)):
                for s in range(r, len(currentBoard)):
                    
                    aux = len(currentBoard)+1+r-s
                    if (aux > len(currentBoard)):
                        aux = len(currentBoard)
                    
                    if currentBoard[s][aux] == self.board.player(currentPlayer):
                        counter += 1
                        inSequence = True
                    else:
                        if inSequence:
                            if currentBoard[s][aux] != self.board.player(util.opponent(currentPlayer)):
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