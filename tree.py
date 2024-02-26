import board

class Node:
    def __init__(self, value, children):
        self.value = value      # is a matrix of the board
        self.children = children    # is a dictionary {1: node, 2: node, ...}
        
        

class Tree:
    def __init__(self, board, player):
        self.player = player
        self.root = Node(board.board, {})
        children = self.genChildren(self.root)
        
    def genChildren(self, node):
        children = {}
        for i in range(board.Board.cols):
            temporaryBoard = board.Board()
            temporaryBoard.board = node.value.copy()
            temporaryBoard.move(i+1, self.player)
            children[i] = Node(temporaryBoard.board, {})
        return children
        