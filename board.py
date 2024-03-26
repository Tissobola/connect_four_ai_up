import copy

class Board:
    def __init__(self, cols = 7, rows = 6, board = [], nullSymbol= '.', p1Symbol = 'X', p2Symbol = 'O', algorithm1 = None, algorithm2 = None, score = 0, winner = None, end = False):
        self.cols = cols
        self.rows = rows
        self.board = board
        self.nullSymbol= nullSymbol
        self.p1Symbol = p1Symbol
        self.p2Symbol = p2Symbol
        self.populateBoard()
        self.algorithm1 = algorithm1
        self.algorithm2 = algorithm2
        self.score = score
        self.winner = winner
        self.turn = p1Symbol # First player = X
        self.end = end # End of game 

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
            # print("current_player = ", self.turn)
            self.turn = self.p2Symbol
        elif self.turn == self.p2Symbol:
            # print("current player = ", self.turn)
            self.turn = self.p1Symbol
        return self.turn
    
    def update_score(self):
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
    


    def genChildren(self):
        children = {}
        for i in range(self.cols):
            temporaryBoard = self.copyBoard()
            if temporaryBoard.move(i+1):
                children[i] = temporaryBoard
        return children
    

    
    def copyBoard(self):
        result = Board()
        for row in range(self.rows):
            result_row = []
            for col in range(self.cols):
                result_row.append(self.board[row][col])  
            result.append(result_row) 
        return result
    

    def checkWinner(self, player, col):
        row = 0
    
        # while(self.board[row][col-1]!=player):
        #     row += 1
    
        while self.board[row][col - 1] != player:  # Verifica se row está dentro do intervalo válido
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
            if 0 <= row + i < self.rows and 0 <= col - 1 + i < self.cols:
                # print(f"Checking \ ({row + i}, {col + i}): {self.board[row + i][col - 1 + i]}")
                if self.board[row + i][col - 1 + i] == token:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        
        # Check diagonal down-left-to-right
        count = 0
        for i in range(-3, 4):
            if 0 <= row + i < self.rows and 0 <= col - 1 - i < self.cols:
                # print(f"Checking / ({row + i}, {col - i}): {self.board[row + i][col - 1 - i]}")
                if self.board[row + i][col - 1 - i] == token:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False
    

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