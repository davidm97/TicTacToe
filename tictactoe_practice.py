"""Regular Tic Tac Toe vs AI"""
import random

class TicTacToe(object):
    #Initializes game
    def __init__(self, board = []):
        if len(board) == 0:
            self.board = [' ' for i in range(9)]
        else:
            self.board = board
    
    #Winning Combos
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
    
    winners = ('X-win', 'Draw', 'O-win')
     
    #Creates board
    def printBoard(self):
        print "| %s | %s | %s |   | 1 | 2 | 3 |" % (self.board[0], self.board[1], self.board[2])
        print "-------------   -------------"
        print "| %s | %s | %s |   | 4 | 5 | 6 |" % (self.board[3], self.board[4], self.board[5])
        print "-------------   -------------"
        print "| %s | %s | %s |   | 7 | 8 | 9 |" % (self.board[6], self.board[7], self.board[8])
        print ""

    #Determine all open moves
    def getAvailableMoves(self):
        return [k for k,v in enumerate(self.board) if v==' ']
    
    #Determines if board is full
    def complete(self):
        if ' ' not in [v for v in self.board]:
            return True
        if self.winner() != None:
            return True
        return False
    
    #X wins
    def X_wins(self):
        return self.winner() == 'X'
    
    #O wins
    def O_wins(self):
        return self.winner() == '0'
    
    #Tie
    def tied(self):
        return (self.complete() == True and self.winner() == None)
    
    #Determine winner
    def winner(self):
        for player in ('X', 'O'):
            positions = self.getSquares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None
    
    #Determines squares occupied by player
    def getSquares(self, player):
        return [k for k,v in enumerate(self.board) if v == player]
    
    #Physically makes move
    def makeMove(self, position, player):
        self.board[position] = player
    
    def minimax(self, node, player, alpha, beta):
        if node.complete():
            if node.X_wins():
                return -1
            elif node.tied():
                return 0
            elif node.O_wins():
                return 1
            best = None
        for move in node.getAvailableMoves():
            node.makeMove(move, player)
            val = self.minimax(node, get_enemy(player), alpha, beta)
            node.makeMove(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
            else:
                if val < beta:
                    beta = val
        if player == '0':
            return alpha
        else:
            return beta

def determine(board, player):
    a = -2
    choices = []
    if len(board.getAvailableMoves()) == 9:
        return 4
    for move in board.getAvailableMoves():
        board.makeMove(move, player)
        val = board.minimax(board, get_enemy(player))
        board.makeMove(move, ' ')
        print "move:", move + 1, "causes:", board.winners[val + 1]
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    return random.choice(choices)


def get_enemy(player):
    if player == 'X':
        return 'O'
    return 'X'

if __name__ == "__main__":
    board = TicTacToe()
    board.printBoard()

    while not board.complete():
        player = 'X'
        player_move = int(raw_input("Next Move: ")) - 1
        if not player_move in board.getAvailableMoves():
            continue
        board.makeMove(player_move, player)
        board.printBoard()

        if board.complete():
            break
        player = get_enemy(player)
        computer_move = determine(board, player)
        board.makeMove(computer_move, player)
        board.printBoard()
    print "winner is", board.winner()    
    
       
"""
    
    #Creates duplicate board    
    def copyBoard(board):
        copy = []
        for i in board:
            copy.append(i)
        return copy
    
    #Determines if move is open
    def openMove(board, index):
        return (board[index] != 'X' and board[index] != 'O')
   
    #Gets move from player
    def getPlayerMove(board):
        move = ''
        legal_moves = '1 2 3 4 5 6 7 8 9'.split()
        while move not in legal_moves or not openMove(board, int(move)-1):
            print "What is your next move? (1-9)"
            move = raw_input()
            try:
                index = int(move) - 1
            except:
                print "Please type a number from 1-9."
        return index
    
    #Choose random legal move
    def getRandomMove(board, moves_list):
        pos_moves = []
        for i in moves_list:
            if openMove(board, i):
                pos_moves.append(i)
        if len(pos_moves) != 0:
            return choice(pos_moves)
        else:
            return None
        
    #Switch teams
    def getEnemy(flag):
        if flag == 'X':
            return 'O'
        else:
            return 'X'

    #Minimax Algorithm
    def minimax(board, flag, alpha, beta):
        if complete(board):
            if getWinner(board, flag):
                return 1
            elif getWinner(board, getEnemy(flag)):
                return -1
            else:
                return 0
        for move in getAvailableMoves(board):
            copy = copyBoard(board)
            makeMove(copy, flag, move)
            val = minimax(copy, getEnemy(flag), alpha, beta)
            if flag == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if flag == 'O':
            return alpha
        else:
            return beta

    #Creates AI        
    def getCompMove(board, flag):
        a = -2
        choices = []
        if len(getAvailableMoves(board)) == 9:
            return 4
        for move in getAvailableMoves(board):
            copy = copyBoard(board)
            val = minimax(copy, getEnemy(flag), -2, 2)
            if val > a:
                a = val
                choices = [move]
            if val == a:
                choices.append(move)
        return choice(choices)
    
    #Determines who makes first move
    def getFirstMove():
        if randint(0, 1) == 0:
            return 'player'
        else:
            return 'computer'
        
    #Do you want to play again
    def playAgain():
        print "Do you want to play again? (yes or no)"
        return raw_input().lower().startswith('y')
        
#Create game
print "Welcome to Tic Tac Toe!"

while (1):
    board = [' ']*9 
    player = 'X'
    comp = 'O'
    turn = getFirstMove()
    print "The " + turn + " will go first!"
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            printBoard(board)
            move = getPlayerMove(board)
            makeMove(board, player, move)
            if getWinner(board, player):
                printBoard(board)
                print "You have won the game!"
                gameIsPlaying = False
            else:
                if complete(board):
                    printBoard(board)
                    print "The game is a tie!"
                    gameIsPlaying = False
                else:
                    turn = 'computer'
        else:
            printBoard(board)
            move = getCompMove(board, comp)
            makeMove(board, comp, move)
            if getWinner(board, comp):
                printBoard(board)
                print "You have lost the game!"
                gameIsPlaying = False
            else:
                if complete(board):
                    printBoard(board)
                    print "The game is a tie!"
                    gameIsPlaying = False
                else:
                    turn = 'player'
    if not playAgain():
        break
"""

"""
Create player class
Create evaluator class

Methods
1. move
    - 
2. rtup
3. filter
4. func
5. select
6. get_legal_actions
    - determine block to make next move in
    - check which miniblocks we can move in
    - 
7. op
8. _min_val_ab
9. _max_val_ab
10. terminal_test
11. generate_successor
12. __eval_state
13. __assess_miniB
14. get_winner
15. is_board_full
16. get_miniboard
17. get_empty_of
18. terminal_state_reached
19. analyze
    - determines if one move can win board
20. free
    - used in analyze to determine indices

Inputs
state - 
temp_block - 
old_move - 
flag - team
gameb - 
"""

