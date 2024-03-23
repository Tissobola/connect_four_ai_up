
import tree
import board
import math
import random

#selection, expansion, simulation, backpropagation

C = math.sqrt(2)
class MonteCarlo_heuristics:
    def __init__(self, game_board, player):
        self.game_board = game_board
        self.player = player  # 'X' or 'O'
        self.tree = tree.Tree(game_board,player)
         
 
    
    def select(self, node, visited):
        print('SELECT')
        while not node.isLeaf():
            best_ucb1 = float('-inf')
            selected_node = None
            for children_node in node.children.values():
                if children_node.simulations == 0:
                    # If a child has not been explored, select it immediately
                    return children_node
                if children_node.value in visited:
                    break
                exploitation = children_node.wins / children_node.simulations
                exploration = C * math.sqrt(math.log(node.simulations) / children_node.simulations)
                ucb1_value = exploitation + exploration
                if ucb1_value > best_ucb1:
                    best_ucb1 = ucb1_value
                    selected_node = children_node
            node = selected_node
        return selected_node
    
    def expand(self, node):
        print('EXPAND')
        children = self.tree.genChildren(node)
        
        return children 

    def simulate(self, node):
        print('SIMULATION')
        
        temp_board = board.Board()
        temp_board.board = node.value
        while not temp_board.end:
            random_move = random.randint(1, temp_board.cols)
            temp_board.move(random_move)
            self.player = 'X' if self.player == 'O' else 'O'
        result = temp_board.end
        if result: # is win
            node.wins += 1 
        node.simulations += 1
        return result 
    
    
    def backpropagate(self, node, result):
        print('BACKPROPAGATE')
        while not node.isLeaf():
            node.wins = node.wins + 1 if result else node.wins
            node.simulations += 1
            node = node.parent
            
    def get_best_move(self):
        iterations = 100000  # Number of MCTS iterations
        visited = set()
        for _ in range(iterations):
            selected_node = self.select(self.tree.root, visited)
            if not selected_node.isLeaf():
                self.expand(selected_node)
                simulation_result = self.simulate(selected_node)
                self.backpropagate(selected_node, simulation_result)
            visited.add(tuple(tuple(row) for row in selected_node.value))
        # After MCTS iterations, select the best move based on statistics
        best_move = max(self.tree.root.children.items(), key=lambda x: x[1].simulations)[0] + 1
        return best_move
    
def play_MCTS(board, player):
    mcts = MonteCarlo_heuristics(board, player)
    best_move = mcts.get_best_move()
    return best_move