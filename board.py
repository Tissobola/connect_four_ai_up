class Board:
    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.board = []
        self.nullSymbol = '.'
        self.p1Symbol = 'X'
        self.p2Symbol = 'O'
        self.populateBoard()
        self.algorithm1 = None
        self.algorithm2 = None
        self.winner = None
        self.turn = self.p1Symbol# Primeiro jogador = X
        self.end = False # Fim do jogo

    def __str__(self):
        line = ""
        result = ""
        for i in range(0, 6):
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
    
    def change_turn(self): # Muda de jogador 
        if self.turn == self.p1Symbol:
            self.turn = self.p2Symbol
        elif self.turn == self.p2Symbol:
            self.turn = self.p1Symbol
        return self.turn
        
    def move(self, collumn):
        return self.addToCollumn(collumn, self.turn)
            
    def addToCollumn(self, collumn, symbol):

        #self.board[self.rowTops[collumn]][collumn] = symbol
        # if self.checkWinner(symbol, (self.rowTops[collumn],collumn)):
        #    self.showWinner(symbol)
        #self.rowTops[collumn] -= 1 #Vai decrementando os valores da lista rowTops
        for i in range(len(self.board) -1 , -1, -1): # i = número de linhas
            if self.board[i][collumn-1] == self.nullSymbol:
                self.board[i][collumn-1] = symbol
                self.change_turn() # Muda de jogador 
                if self.checkWinner(symbol, collumn):
                   print("Ganhou")
                
                   self.winner=self.turn
                   self.end = True
                return True
        return False
        


    def checkWinner(self, player, col):
        row = 0
        while(self.board[row][col-1]!=player):
            row += 1
        
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
            if self.board[r][col-1] == token:
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
                    
    '''def showWinner(self, player):
        self.end = True
        # print("\n\nPLAYER "+str(player)+" WINS!\n"+str(self))
    '''