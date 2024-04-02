import random
import numpy as np
import src.common.utils as util
import src.mcts.nodemc as nodemc


class MonteCarlo:
    def __init__(self, state, player):
        self.tree = nodemc.MCTree(state, player)      # tree based on the board object
        self.player = player    # 1 or 2
        self.state = state  # Board object
        self.simulations = 10000
        self.p1Symbol = 'X'
        self.p2Symbol = 'O'
        self.c = 1/2
    
    def def_player(self, player):
        if player == 1:
            return self.p1Symbol
        elif player == 2:
            return self.p2Symbol
    
    def selection(self):
        return self.selecting(self.tree.root)
    
    def selecting(self, node):
        while not node.possibleMoves:
            result = self.bestMove(node)
            if result == None:
                return None
            node = result                
            
        return node

    
    def bestMove(self, node):
        # calcular o melhor ucb entre os nós filhos
        
        if len(node.children) != 0:
            best = max(self.ucb1(node, move) for move in node.children)
        else:
            return None

        # lista com todos os nos que tem best como ucb
        best_nodes = []
        for move in node.children:
            if self.ucb1(node, move) == best:
                best_nodes.append(node.children[move])
        return random.choice(best_nodes)
        
      
    def ucb1(self, node, move):
        ucb1 = float('inf')
        if not node.getChild(move).visits == 0 :
            exploitation = node.getChild(move).wins / node.getChild(move).visits
            exploration = np.sqrt(np.log(node.visits) / node.getChild(move).visits)
            ucb1 = exploitation + self.c * exploration
        return ucb1

    def expansion(self, node):
        column = random.choice(node.possibleMoves)
        node.remove_pm(column) # remove a jogada da lista

        if node.nodeHeight() % 2 == 0:
            new_node = node.genChild(column, self.player)
        else:
            new_node = node.genChild(column, util.opponent(self.player))
        return new_node


    def simulation(self, node):
        if len(node.value.possibleMoves()) == 0: # verificar empate
            return False
        turn = node.nodeHeight() % 2
        while not node.value.end:
            move = random.choice(node.value.possibleMoves())
            if (turn % 2) + 1 == 1:
                node.value.move(move, self.player)
            else:
                node.value.move(move, util.opponent(self.player))
            turn += 1
            if node.value.end:
                break
        if node.value.winner == self.def_player(self.player):
            return True
        else: return False

  
    def backPropagation(self, node, won):
        while node is not None:
            node.visit()
            if won:
                node.win()
            node = node.getParent()


        
        
    def play(self):
        self.tree = nodemc.MCTree(self.state, self.player)      # tree based on the board object
        for _ in range(self.simulations):
            node = self.selection()
            
            if node == None:
                best = self.bestMove(self.tree.root)
                self.state.move(best.column, self.player)
                return
            
            expanded_node = self.expansion(node)
            
            if expanded_node.value.winner != self.def_player(self.player):
                tempNode = expanded_node.copy()
                won = self.simulation(tempNode) # correta - true or false
            else:
                won = True
            self.backPropagation(expanded_node, won)

        best = self.bestMove(self.tree.root)
        self.state.move(best.column, self.player)