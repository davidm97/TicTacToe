"""Two Player TicTacToe"""

import random

class TicTacToe(object):
    def __init__(self, board = []):
        if len(board) == 0:
            self.board = [' ' for i in range(9)]
        else:
            self.board = board
            
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
        
    #Print Board
    def printBoard(self):
        print "| %s | %s | %s |   | 1 | 2 | 3 |" % (self.board[0], self.board[1], self.board[2])
        print "-------------   -------------"
        print "| %s | %s | %s |   | 4 | 5 | 6 |" % (self.board[3], self.board[4], self.board[5])
        print "-------------   -------------"
        print "| %s | %s | %s |   | 7 | 8 | 9 |" % (self.board[6], self.board[7], self.board[8])
        print ""
        
    #Determines if board is full
    def tied(self):
        for k,v in enumerate(self.board):
            if (v != 'X' and v != 'O'):        
                return False
        return True
    
    #Determines winner
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
    
    #Determines if game is over
    def gameOver(self):
        if self.winner() or self.tied():
            return True
        return False
        
    #Determines squares occupied by player
    def getSquares(self, player):
        return [k for k,v in enumerate(self.board) if v == player]
        
    #Physically makes move
    def makeMove(self, position, player):
        self.board[position] = player
    
    #See who goes first
    def getFirstMove(self):
        if random.randint(0,1) == 0:
            return 'X'
        else:
            return 'O'
    
    #Determine if move is open
    def openMove(self, position):
        return (self.board[int(position)] != 'X' and self.board[int(position)] != 'O')    
    
    #Get move input
    def getPlayerMove(self, player):
        move = ''
        legal_moves = '1 2 3 4 5 6 7 8 9'.split()
        while move not in legal_moves or not self.openMove(int(move)-1):
            print player + ", what is your next move? (1-9)"
            move = raw_input()
            try:
                position = int(move)-1
            except:
                print "Please type a number from 1-9."
        return position
        
    #Get enemy team
    def getEnemy(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'
    
    #Minimax algorithm
    def minimax(self, player):
        if self.gameOver():
            if self.winner() == 'X':
                return (-1, None)
            elif self.winner() == 'O':
                return (1, None)
            elif self.tied():
                return (0, None)
        elif player == 'O':
            best = [(-2, None)]
            for k,v in enumerate(self.board):
                if (v != 'X' and v != 'O'):
                    self.makeMove(k,player)
                    value = self.minimax(self.getEnemy(player))[0]
                    #self.printBoard()
                    #print value
                    self.board[k] = ' '
                    if value > best[0][0]:
                        best = [(value, k)]
                    elif value == best[0][0]:
                        best.append((value, k))
            return random.choice(best)
        else:
            best = [(2, None)]
            for k,v in enumerate(self.board):
                if (v != 'X' and v != 'O'):
                    self.makeMove(k,player)
                    value = self.minimax(self.getEnemy(player))[0]
                    #self.printBoard()
                    #print value
                    self.board[k] = ' '
                    if value < best[0][0]:
                        best = [(value, k)]
                    elif value == best[0][0]:
                        best.append((value, k))
            return random.choice(best)
    
    #Get best move
    def bestMove(self, player):
        return self.minimax(player)[1]
    
    #Get computer move
    def getCompMove(self, player):
        return self.bestMove(player)
        
    #Ask to play again
    def playAgain(self):
        print "Do you want to play again? (yes or no)"
        response = raw_input()
        if response.startswith('y'):
            return True
        else:
            return False

def main():       
    #Create Game
    print "Welcome to Tic Tac Toe!"

    while(1):
        game = TicTacToe()
        turn = game.getFirstMove()
        print turn + " will go first!"
        gameIsPlaying = True
    
        while gameIsPlaying:
            if turn == 'X':
                player = turn
                game.printBoard()
                move = game.getPlayerMove(player)
                game.makeMove(move, player)
                if game.winner():
                    game.printBoard()
                    print "X has won the game!"
                    gameIsPlaying = False
                elif game.tied():
                    game.printBoard()
                    print "The game has ended in a tie!"
                    gameIsPlaying = False
                else:
                    turn = 'O'
                
            elif turn == 'O':
                player = turn
                game.printBoard()
                move = game.getCompMove(player)
                game.makeMove(move, player)
                if game.winner():
                    game.printBoard()
                    print "O has won the game!"
                    gameIsPlaying = False
                elif game.tied():
                    game.printBoard()
                    print "The game has ended in a tie!"
                    gameIsPlaying = False
                else:
                    turn = 'X'
        if not game.playAgain():
            break       
    
main()                