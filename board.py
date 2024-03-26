import numpy as np

class Board:
    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.board = []
        self.nullSymbol = '.'
        self.p1Symbol = 'X'
        self.p2Symbol = 'O'
        self.populateBoard()
        self.end = False
        self.winner = None

    def __str__(self):
        line = ""
        result = ""
        for i in range(5, -1, -1):
            for ii in range(self.cols):
                line += self.board[i][ii]
            result += line + "\n"
            line = ""
        return result

    def populateBoard(self):
        aux = []
        for i in range(self.cols):
            aux.append(self.nullSymbol)
        for i in range(self.rows):
            self.board.append(aux.copy())

    def move(self, collumn, player):
        return self.addToCollumn(collumn, player)
            
    def addToCollumn(self, collumn, player):
        #self.board[self.rowTops[collumn]][collumn] = symbol
        # if self.checkWinner(symbol, (self.rowTops[collumn],collumn)):
        #    self.showWinner(symbol)
        #self.rowTops[collumn] -= 1 #Vai decrementando os valores da lista rowTops
        for i in range(len(self.board)):
            if self.board[i][collumn-1] == self.nullSymbol and self.possibleMoves().__contains__(collumn):
                self.board[i][collumn-1] = self.player(player)
                if len(self.possibleMoves()) == 0:
                    self.end = True
                if self.checkWinner(self.player(player), (i,collumn-1)):
                    self.showWinner(player)
                return True
        return False
        
    def checkWinner(self, player, last_move):
        row, col = last_move
        token = player  # assuming player's token is represented by 'X' or 'O'

        # Check horizontal
        count = 0
        for c in range(self.cols):
            if self.board[row][c] == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check vertical
        count = 0
        for r in range(self.rows):
            if self.board[r][col] == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check diagonal up-left-to-right
        count = 0
        for i in range(-3, 4):
            if 0 <= row + i < self.rows and 0 <= col + i < self.cols:
                if self.board[row + i][col + i] == token:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        
        # Check diagonal down-left-to-right
        count = 0
        for i in range(-3, 4):
            if 0 <= row + i < self.rows and 0 <= col - i < self.cols:
                if self.board[row + i][col - i] == token:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False
                    
    def showWinner(self, player):
        self.end = True
        self.winner = player
        # print("\n\nPLAYER "+str(self.player(player))+" WINS!\n"+str(self))

    def player(self, player):
        if player == 1:
            return self.p1Symbol
        elif player == 2:
            return self.p2Symbol
        
    def possibleMoves(self):
        return [col+1 for col in range(7) if self.board[5][col] == self.nullSymbol]