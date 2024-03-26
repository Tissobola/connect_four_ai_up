import board_old

class Node:
    def __init__(self, value, children):
        self.value = value      # is a matrix of the board
        self.children = children    # is a dictionary {0: node, 1: node, ...}
        
    def setValue(self, value):
        self.value = value
        
    def setChildren(self, children):
        self.children = children
        
        

class Tree:
    def __init__(self, board, player):              # player is X or O, board is a board object
        self.player = player                        # X or O
        self.board = board                       
        self.root = Node(board.board, {})           # root node with the matrix of the board as its value
        children = self.get_possible_moves(self.board, self.player)      # new board matrixes made with different possible moves for the player
        self.root.setChildren(children)             # set the new board matrixes as children of the root
        
    # def genChildren(self, node):
    #     temp = board.Board()
    #     cols = temp.cols
    #     temp = 0
    #     children = {}
    #     for i in range(cols):
    #         temporaryBoard = board.Board()
    #         temporaryBoard.board = self.copyBoard(node.value)
    #         temporaryBoard.move(i+1)
    #         children[i] = Node(self.copyBoard(temporaryBoard.board), {})
    #     return children
    
    # def genChildren(self, node):
    #     children = {}
    #     for i in range(self.board.cols):  # Itera sobre todas as colunas do tabuleiro
    #         temporaryBoard = board.Board()
    #         temporaryBoard.board = self.copyBoard(node.value)
    #         if not temporaryBoard.move(i + 1):  # Tenta fazer o movimento na coluna i
    #             continue  # Se não for possível, passa para a próxima coluna
    #         children[i] = Node(self.copyBoard(temporaryBoard.board), {})  # Adiciona o filho com o movimento i
    #     # print("Children Tree = " + str(children))
    #     return children
    
    def get_possible_moves(self, node, player):
        children = {}
        for col in range(self.board.cols):
            temporary_board = board_old.Board()
            temporary_board.board = self.copyBoard(node)  # Faz uma cópia do tabuleiro atual
            temporary_board.turn = player
            if temporary_board.move(col + 1):  # Tenta fazer o movimento na coluna col
                children[col] = temporary_board 
                # print(f"adicionou ao dicionário na coluna {col + 1}") # Adiciona a coluna como uma jogada possível
                  # Sai do loop após adicionar um movimento válido
        # for key, value in children.items():
        #     print(key+1, ' : ')
        #     print(value)
        
        return children


    # def copyBoard(self, board):
    #     result = []
    #     for row in board:
    #         result.append(row.copy())
    #     return result

    def copyBoard(self, board):
        result = []
        for row in range(self.board.rows):
            result_row = []
            for col in range(self.board.cols):
                result_row.append(self.board.board[row][col])  # Copia cada elemento da linha
            result.append(result_row)  # Adiciona a linha à cópia
        return result