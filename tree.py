# import board
# import numpy as np

# class Node:
#     def __init__(self, value, children, parent):
#         self.value = value      # is a matrix of the board in AStarTree and is a Board object in MCTree
#         self.children = children    # is a dictionary {0: node, 1: node, ...}
#         self.parent = parent    # is another node
        
#         #Monte Carlo
#         self.wins = 0
#         self.visits = 0
        
#     def setValue(self, value):
#         self.value = value
        
#     def setChildren(self, children):
#         self.children = children
        
#     def getChild(self, child):
#         return self.children[child]
        
#     def setParent(self, parent):
#         self.parent = parent
    
#     def getParent(self):
#         return self.parent
    
#     #Monte Carlo
    
#     def win(self):
#         self.wins += 1
        
#     def visit(self):
#         self.visits += 1
        
#     def genChildren(self, player):
#         children = {}
#         for i in self.value.possibleMoves():
#             temporaryBoard = board.Board()
#             temporaryBoard.board = np.copy(self.value.board)
#             temporaryBoard.move(i, player)
#             children[i] = Node(temporaryBoard, {}, self)
#             print(f"children {i} = {children[i]}")
#         self.setChildren(children)
    
#     def nodeHeight(self):
#         return self.calculateNodeHeight(self)

#     def calculateNodeHeight(self, node):
#         if node.parent == None: return 0
#         else:
#             return self.calculateNodeHeight(node.parent) + 1

# class AStarTree:
#     def __init__(self, board, player):              # player is 1 or 2, board is a board object
#         self.player = player                        # 1 or 2
#         self.root = Node_astar(board.board, {})           # root node with the matrix of the board as its value
#         children = self.genChildren(self.root)      # new board matrixes made with different possible moves for the player
#         self.root.setChildren(children)             # set the new board matrixes as children of the root

#     def genChildren(self, node):
#         temp = board.Board()
#         cols = temp.cols
#         temp = 0
#         children = {}
#         for i in range(cols):
#             temporaryBoard = board.Board()
#             #temporaryBoard.board = np.copy(node.value)
#             temporaryBoard.move(i+1, self.player)
#             children[i] = Node_astar(np.copy(temporaryBoard.board), {})
#         return children
    


    
# class MCTree():
#     def __init__(self, board, player):
#         self.player = player                        # 1 or 2
#         self.root = Node(board, {}, None)           # root node with the board object as its value
#         # self.root.genChildren(player)
        
# class Node_astar:
#     def __init__(self, value, children):
#         self.value = value      # is a matrix of the board in AStarTree and is a Board object in MCTree
#         self.children = children    # is a dictionary {0: node, 1: node, ...}
#         # is another node
        
#         #Monte Carlo
#         self.wins = 0
#         self.visits = 0
        
#     def setValue(self, value):
#         self.value = value
        
#     def setChildren(self, children):
#         self.children = children
        
#     def getChild(self, child):
#         return self.children[child]
        
import board
import numpy as np

class Node:
    def __init__(self, value, children, parent):
        self.value = value      # is a matrix of the board in AStarTree and is a Board object in MCTree
        self.children = children    # is a dictionary {0: node, 1: node, ...}
        self.parent = parent    # is another node
        self.wins = 0
        self.visits = 0
        
    def setValue(self, value):
        self.value = value
        
    def setChildren(self, children):
        self.children = children
        
    def getChild(self, child):
        return self.children[child]
        
    def setParent(self, parent):
        self.parent = parent
    
    def getParent(self):
        return self.parent
    
    #Monte Carlo
    
    def win(self):
        self.wins += 1
        
    def visit(self):
        self.visits += 1
        
    def genChildren(self, player):
        children = {}
        for i in self.value.possibleMoves():
            temporaryBoard = board.Board()
            temporaryBoard.board = np.copy(self.value.board)
            temporaryBoard.winner = self.value.winner
            temporaryBoard.end = self.value.end
            temporaryBoard.move(i, player)
            
            children[i] = Node(temporaryBoard, {}, self)
            print(f"Sucessor {i} : {children[i].value}")
        self.setChildren(children)
        return children
    
    def nodeHeight(self):
        return self.calculateNodeHeight(self)

    def calculateNodeHeight(self, node):
        if node.parent == None: return 0
        else:
            return self.calculateNodeHeight(node.parent) + 1
        
    def copy(self):
        boardCopy = board.Board()
        boardCopy.board = np.copy(self.value.board)
        boardCopy.winner = self.value.winner
        boardCopy.end = self.value.end

        childrenCopy = {}
        for child in self.children:
            childrenCopy[child] = self.getChild(child).copy()
        
        node = Node(boardCopy, childrenCopy, self.parent)
        node.wins = self.wins
        node.visits = self.visits
        
        return node
        

class AStarTree:
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
            temporaryBoard.board = np.copy(node.value)
            temporaryBoard.move(i+1, self.player)
            children[i] = Node(np.copy(temporaryBoard.board), {})
        return children
    
class MCTree():
    def __init__(self, board, player):
        self.player = player                        # 1 or 2
        self.root = Node(board, {}, None)           # root node with the board object as its value
        
    def __str__(self):
        result = ''
        for child in self.root.children:
            result += str(child) + ": " + str(self.root.getChild(child).wins) + "/" + str(self.root.getChild(child).visits) + " Winner: " + str(self.root.getChild(child).value.winner) + "\n"
        return result