import common.board as board
import bots.minimax.minimax as minimax
import montecarlo
import random

def random_play(player, game):
    move = random.randint(1, 7)
    game.move(move, player)

#-------------------------------- GAME --------------------------------

games = 50
p1_wins = 0
p2_wins = 0
ties = 0

for i in range(games):
    print("Test number:", i)
    game_board = board.Board()
    
    bot1 = montecarlo.MonteCarlo(game_board, 1)
    bot2 = minimax.MinimaxBot(game_board, 2)

    turn = 0

    while (not game_board.end):
        if (turn % 2) + 1 == 1:
            # random_play(1, game_board)
            bot1.play()
        else:
            bot2.play()
        turn += 1

    if game_board.winner == 'X':
        p1_wins += 1
        print("Winner: P1")
    elif game_board.winner == 'O':
        p2_wins += 1
        print("Winner: P2")
    else:
        ties += 1
        print("Tie")
        
print(games, "games")
print("Player 1 victories:", p1_wins)
print("Player 2 victories:", p2_wins)
print("Ties:", ties)