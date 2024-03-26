import tree
import board_old

#h(n): minimize the chances of the opponent to win and maximize the chances of the bot to win
#g(n): uniform cost search minimizes the cost of the path from the root to the current n - constant
#f(n) = h(n) + g(n)



def astar(board):
    successors = board.genChildren()
    
    best_score = float('inf')
    #for suc_col, suc_board in successors.items():
        #print(suc_col, ": ", suc_board)
    i = 1
    for successor in successors.items():
        suc_col, suc_board = successor
        #print(f"Col: {suc_col}")
        print(f"scores {i} successor = {suc_board.score}")
        
        
        if suc_board.score < best_score:
            best_score = suc_board.score
            best_successor = suc_col

        i += 1
    print("best_score:", best_score)
    return best_successor


# class AStarBot:
#     def __init__(self, board, player):
#         self.board = board      # board object
#         self.player = player    # X or O
#         self.start_node = board
#         self.open = []  # set of nodes to be evaluated
#         self.closed = []  # set of nodes already evaluated



#     def h(self, node):
#         count_x = 0
#         count_o = 0
#         # Count occurrences of 'X' and 'O' in the node
#         for i in range(self.board.rows):
#             for j in range(self.board.cols):
            

#                 # Horizontal segments
#                 if j <= self.board.cols - 4:
#                     segment = [node.board[i][j+k] for k in range(4)]
#                     count_x += segment.count('X')
#                     count_o += segment.count('O')

#                 # Vertical segments
#                 if i <= self.board.rows - 4:
#                     segment = [node.board[i+k][j] for k in range(4)]
#                     count_x += segment.count('X')
#                     count_o += segment.count('O')

#                 # Diagonal segments (top-left to bottom-right)
#                 if i <= self.board.rows - 4 and j <= self.board.cols - 4:
#                     segment = [node.board[i+k][j+k] for k in range(4)]
#                     count_x += segment.count('X')
#                     count_o += segment.count('O')

#                 # Diagonal segments (bottom-left to top-right)
#                 if i >= 3 and j <= self.board.cols - 4:
#                     segment = [node.board[i-k][j+k] for k in range(4)]
#                     count_x += segment.count('X')
#                     count_o += segment.count('O')

#         if count_x == 4:  # 'X' wins
#             return 512
#         elif count_o == 4:  # 'O' wins
#             return -512
#         else:
#             # Evaluate segments
#             score = 0
#             for i in range(self.board.rows):
#                 for j in range(self.board.cols):
                    
#                     # Horizontal segments
#                     if j <= self.board.cols - 4:
#                         segment = [node.board[i][j+k] for k in range(4)]
#                         score += self.evaluate_segment(segment)

#                     # Vertical segments
#                     if i <= self.board.rows - 4:
#                         segment = [node.board[i+k][j] for k in range(4)]
#                         score += self.evaluate_segment(segment)

#                     # Diagonal segments (top-left to bottom-right)
#                     if i <= self.board.rows - 4 and j <= self.board.cols - 4:
#                         segment = [node.board[i+k][j+k] for k in range(4)]
#                         score += self.evaluate_segment(segment)

#                     # Diagonal segments (bottom-left to top-right)
#                     if i >= 3 and j <= self.board.cols - 4:
#                         segment = [node.board[i-k][j+k] for k in range(4)]
#                         score += self.evaluate_segment(segment)

#             # Add move bonus
#             if self.player == 'X':
#                 score += 16
#             else:
#                 score -= 16
#             return score

#     def evaluate_segment(self, segment):
#         count_x = segment.count('X')
#         count_o = segment.count('O')
#         if count_o == 3 and count_x == 0:
#             return -50
#         elif count_o == 2 and count_x == 0:
#             return -10
#         elif count_o == 1 and count_x == 0:
#             return -1
#         elif count_x == 1 and count_o == 0:
#             return 1
#         elif count_x == 2 and count_o == 0:
#             return 10
#         elif count_x == 3 and count_o == 0:
#             return 50
#         else:
#             return 0

#     # def expand_node(self, node):
#     #     children = tree.Tree(self.board, self.player).genChildren(node)
#     #     return children


#     def g(self, node):
#         return 1
    
    
#     def f(self, node):
        
#         return self.h(node) + self.g(node)
    

#     def oponent(self):
#         if self.player == self.board.p1Symbol:
#             return self.board.p2symbol
#         if self.player == self.board.p2Symbol:
#             return self.board.p1Symbol


#     def a_star(self, player):
        
#         tree_obj = tree.Tree(self.board, self.player)
#         possible_moves = tree_obj.get_possible_moves(self.board, player)
#         a_star_column = None
#         f_values = []
#         best_play = None
#         min_f_value = float('inf')
#         for play in possible_moves:
#             f_value = self.f(possible_moves[play])
#             f_values.append(f_value)
#             if(f_value < min_f_value): 
#                 min_f_value = f_value
#                 best_play = possible_moves[play]
#                 a_star_column = play

#         if a_star_column == None or best_play == None:
#             raise ValueError
#         return best_play, a_star_column

        

#     def play(self):
#         if self.board.turn == self.board.p2Symbol:
#             best_play, a_star_column = self.a_star(self.board.turn)
#             print(f"best_play: {best_play}, a_star_column:{a_star_column}")
#             if best_play is not None:
#                 self.board.change_turn()
#                 return best_play, a_star_column
#         else:
#             self.board.change_turn()
       