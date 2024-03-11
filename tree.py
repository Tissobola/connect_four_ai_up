import board

class Node:
    def __init__(self, value, children):
        self.value = value      # is a matrix of the board
        self.children = children    # is a dictionary {0: node, 1: node, ...}
        
    def setValue(self, value):
        self.value = value
        
    def setChildren(self, children):
        self.children = children
        
        

class Tree:
    def __init__(self, board, player):              # player is 1 or 2, board is a board object
        self.player = player                        # 1 or 2
        self.root = Node(board.board, {})           # root node with the matrix of the board as its value
        children = self.genChildren(self.root)      # new board matrixes made with different possible moves for the player
        self.root.setChildren(children)             # set the new board matrixes as children of the root
        
    def genChildren(self, node):
        temp = board.Board()
        cols = temp.cols
        temp = 0
        children = {}
        for i in range(cols):
            temporaryBoard = board.Board()
            temporaryBoard.board = self.copyBoard(node.value)
            temporaryBoard.move(i+1, self.player)
            children[i] = Node(self.copyBoard(temporaryBoard.board), {})
        return children
    
    def copyBoard(self, board):
        result = []
        for row in board:
            result.append(row.copy())
        return result