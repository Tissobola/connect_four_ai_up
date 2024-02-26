class Board:
    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.board = []
        self.nullSymbol = '.'
        self.p1Symbol = 'X'
        self.p2Symbol = 'O'
        self.rowTops = [0, 0, 0, 0, 0, 0, 0]
        self.populateBoard()
        self.end = False
        
    def __str__(self):
        line = ""
        result = ""
        for i in range(self.rows-1, -1, -1):
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
        if player == 1:
            self.addToCollumn(collumn, self.p1Symbol)
        elif player == 2:
            self.addToCollumn(collumn, self.p2Symbol)
            
    def addToCollumn(self, collumn, symbol):
        self.board[self.rowTops[collumn-1]][collumn-1] = symbol
        if self.checkWinner(symbol, (self.rowTops[collumn-1],collumn-1)):
            self.showWinner(symbol)
        self.rowTops[collumn-1] += 1
        
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
            if 0 <= row - i < self.rows and 0 <= col + i < self.cols:
                if self.board[row - i][col + i] == token:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    
    def showWinner(self, player):
        print("\n\nPLAYER "+str(player)+" WINS!\n"+str(self))
        self.end = True




#-------------------------------- GAME --------------------------------   
board = Board()

turn = 0
collumn = 0

while (board.end == False):
    print(board)
    while (collumn < 1 or collumn > 7):
        collumn = int(input())
    board.move(collumn, (turn % 2) + 1)
    turn += 1
    collumn = 0
    
    
# 4 3 2 2 3 1 2 1 5 1 1