import board
from tree import Node

class MinimaxBot:
    def __init__(self, board, player):
        self.board = board
        self.player = player
    
    def play(self):
        current_node = Node(self.board, {}, None)
        if self.player == 2:
            maximizingPlayer = False
        else: maximizingPlayer = True
        column, play_value = self.minimax(current_node, 5, maximizingPlayer)
        # print("coluna = ", column)
        # print("play_value = ", play_value)
        self.board.move(column, self.player)
        return True
    
    def evaluate_segment(self, segment):
        count_x = segment.count('X')
        count_o = segment.count('O')
        if count_o == 3 and count_x == 0:
            return -50
        elif count_o == 2 and count_x == 0:
            return -10
        elif count_o == 1 and count_x == 0:
            return -1
        elif count_x == 1 and count_o == 0:
            return 1
        elif count_x == 2 and count_o == 0:
            return 10
        elif count_x == 3 and count_o == 0:
            return 50
        elif count_x == 4:
            return 512
        elif count_o == 4:
            return -512
        else:
            return 0

    def h(self, node):
        score = 0
        # Count occurrences of 'X' and 'O' in the node
        for i in range(self.board.rows):
            for j in range(self.board.cols):  

                     
                # Horizontal segments
                if j <= self.board.cols - 4:
                    segment = [node.value.board[i][j+k] for k in range(4)]
                    score += self.evaluate_segment(segment)
                    
                   
    
                # Vertical segments
                if i <= self.board.rows - 4:
                    segment = [node.value.board[i+k][j] for k in range(4)]
                    score += self.evaluate_segment(segment)
                    
            
                # Diagonal segments (top-left to bottom-right)
                if i <= self.board.rows - 4 and j <= self.board.cols - 4:
                    segment = [node.value.board[i+k][j+k] for k in range(4)]
                    score += self.evaluate_segment(segment)
                    
       
                # Diagonal segments (bottom-left to top-right)
                if i >= 3 and j <= self.board.cols - 4:
                    segment = [node.value.board[i-k][j+k] for k in range(4)]
                    score += self.evaluate_segment(segment)
                    

        # Move bonus for player
        if self.board.turn == 1:
            score += 16
        elif self.board.turn == 2:
            score -= 16
            
        return score


    def minimax(self, node, depth, maximizingPlayer): # recursive function
        # print("node type = ", type(node))
        # tree = Node(self.board, {}, None)
        if depth == 0 or node.end :
            
            return None, self.h(node) 

        if maximizingPlayer:
            maxEval = float('-inf')
            bestColumn = None
            children = node.genChildren(self.player)
            if len(children) == 0: node.end = True
            for column, child in children.items():
                _, value_current_board = self.minimax(child, depth - 1, False)
                
                if value_current_board > maxEval:
                    maxEval = value_current_board
                    bestColumn = column

            return bestColumn, maxEval
        
        
        
        else: # minimizingPlayer
            minEval = float('inf')
            bestColumn = None
            # children = node.genChildren(self.player)
            opponent_player = 1 if self.player == 2 else 2  # Determine the opponent's player number
            children = node.genChildren(opponent_player)  # Use the opponent's player number
            if len(children) == 0: 
                node.end = True
            for key, value in children.items():
                print(f"{key} : {value.value}")
            if len(children) == 0: node.end = True
            for column, child in children.items():
                _, value_current_board = self.minimax(child, depth - 1, True)
    
                if value_current_board < minEval:
                    minEval = value_current_board
                    bestColumn = column
            return bestColumn, minEval
        
        


