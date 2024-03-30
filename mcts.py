import random
import board
import numpy as np
import utils as util
import tree

class MonteCarlo:
    def __init__(self, state, player):
        self.tree = tree.MCTree(state, player)      # tree based on the board object
        self.player = player    # 1 or 2
        self.state = state  # Board object
        self.simulations = 1000
        self.backPropagationp1Symbol = 'X'
        self.p2Symbol = 'O'
        self.c = np.sqrt(2)
    
    def def_player(self, player):
        if player == 1:
            return self.p1Symbol
        elif player == 2:
            return self.p2Symbol
    
    def selection(self):
        return self.selecting(self.tree.root)
    
    def selecting(self, node):
        print('selecting')

        if len(node.children) == 0:
            return node
        return self.selecting(node.getChild(self.bestMove(node)))
    
    def bestMove(self, node):
        bestMove = None
        for move in node.children:
            ucb1 = self.ucb1(node, move)
            print(ucb1)
            if bestMove == None:
                bestMove = (move, ucb1)
            else:
                if ucb1 > bestMove[1]:
                    bestMove = (move, ucb1)
        return bestMove[0]
    
    def ucb1(self, node, move):
        ucb1 = 0
        if not node.getChild(move).visits == 0 :
            exploitation = node.getChild(move).wins / node.getChild(move).visits
            exploration = np.sqrt(np.log(node.visits) / node.getChild(move).visits)
            print(f'{exploitation} + {self.c * exploration}')
            
            ucb1 = exploitation + self.c * exploration
        return ucb1

    def expansion(self, node):
        print('expansion')
        if node.nodeHeight() % 2 == 0:
            node.genChildren(self.player)
        else:
            node.genChildren(util.opponent(self.player))

    def simulation(self, node):
        print('simulation')
        if len(node.value.possibleMoves()) == 0:
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
        print(node.value.winner)
        if node.value.winner == self.def_player(self.player):
            print(f'entrei sou vencedor {node.value.winner}')
            return True
        else: return False

    def backPropagation(self, node, won):
        print('backpropagation')
        if node.parent == None:
            return
        else:
            node.parent.visit()
            if won:
                print('backpropagation win')
                node.parent.win()
            return self.backPropagation(node.parent, won)
        
    def play(self):
        self.tree = tree.MCTree(self.state, self.player)      # tree based on the board object
        for _ in range(self.simulations):
            node = self.selection()
            self.expansion(node)
            for child in node.children:
                childNode = node.getChild(child)
                childNode.visit()
                if childNode.value.winner != self.def_player(self.player):
                    tempNode = childNode.copy()
                    won = self.simulation(tempNode)
                    if won: childNode.win()
                else:
                    childNode.win()
                    won = True
                self.backPropagation(node.getChild(child), won)
        best = self.bestMove(self.tree.root)
                
        print(self.tree)
        # print("Best move:", best)
        
        self.state.move(best, self.player)