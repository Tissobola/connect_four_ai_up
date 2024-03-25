import random
import board
import numpy as np
import utils as util
import tree

class MonteCarlo:
    def __init__(self, state, player):
        self.state = state      # Board object
        self.player = player    # 1 or 2
    
    def runSimulation(self):
        node = self.state
        turn = 0
        while not node.end:
            move = random.choice(node.possibleMoves())
            if (turn % 2) + 1 == 1:
                node.move(move, self.player)
            else:
                node.move(move, util.opponent(self.player))
            turn += 1
            if node.end:
                break
            node = node
        return self.getWinner(node)

    def getWinner(self, node):
        if node.winner == self.player:  # Player wins
            return -1
        elif node.winner == None:   # No winner
            return 0
        else:
            return 1   # Opponent wins

    def getBestMove(self, simulations):
        scores = {move: 0 for move in self.state.possibleMoves()}
        for move in scores:
            for _ in range(simulations):
                tempState = board.Board()
                tempState.board = np.copy(self.state.board)
                tempState.move(move, self.player)
                mc = MonteCarlo(tempState, self.player)
                scores[move] += mc.runSimulation()
                print(scores)
        bestMove = max(scores, key=scores.get)
        return bestMove
    
    def play(self):
        self.state.move(self.getBestMove(2500), self.player)
        
class MonteCarlo2:
    def __init__(self, state, player):
        self.tree = tree.MCTree(state, player)      # tree based on the board object
        self.player = player    # 1 or 2
        self.board = state  # Board object
    
    def selection(self):
        return self.selecting(self.tree.root)
    
    def selecting(self, node):
        if len(node.children) == 0:
            return node
        return self.selecting(node.getChild(self.bestMove(node)))
    
    def bestMove(self, node):
        bestMove = None
        for move in node.children:
            ucb1 = self.ucb1(node, move)
            if bestMove == None:
                bestMove = (move, ucb1)
            else:
                if ucb1 > bestMove[1]:
                    bestMove = (move, ucb1)
        return bestMove[0]
    
    def ucb1(self, node, move):
        try:
            exploitation = node.getChild(move).wins / node.getChild(move).visits
            exploration = 2*np.log(node.visits / node.getChild(move).visits)
            ucb1 = exploitation + exploration
        except:
            ucb1 = 0
        return ucb1

    def expansion(self, node):
        if node.nodeHeight() % 2 == 0:
            node.genChildren(self.player)
        else:
            node.genChildren(util.opponent(self.player))

    def simulation(self, node):
        if len(node.value.possibleMoves()) == 0:
            return False
        turn = node.nodeHeight() % 2
        while not node.value.end:
            print(node.value.end, node.value.possibleMoves())
            move = random.choice(node.value.possibleMoves())
            if (turn % 2) + 1 == 1:
                node.value.move(move, self.player)
            else:
                node.value.move(move, util.opponent(self.player))
            turn += 1
            if node.value.end:
                break
            node = node
        if node.value.winner == self.player: return True
        else: return False

    def backPropagation(self, node, won):
        # if node.parent.parent == None:
        #     return
        # else:
        #     node.parent.visit()
        #     if won:
        #         node.parent.win()
        #     return self.backPropagation(node.parent, won)
        if node.parent == None:
            return
        elif node.parent.parent == None:
            return
        else:
            node.parent.visit()
            if won:
                node.parent.win()
            return self.backPropagation(node.parent, won)
        
    def play(self):
        self.tree = tree.MCTree(self.board, self.player)      # tree based on the board object
        numberOfSimulations = 1000
        n = numberOfSimulations
        for i in range(n):
            # print("foi", i)
            node = self.selection()
            self.expansion(node)
            tempBoard = board.Board()
            tempBoard.board = np.copy(node.value.board)
            # tempBoard.end = node.getChild(move).value.end
            tempNode = tree.Node(tempBoard, {}, node)
            
            node.visit()
            won = self.simulation(tempNode)
                
            if won: node.win()
                
            self.backPropagation(node, won)
        self.tree.root.value.move(self.bestMove(self.tree.root), self.player)
        return