"""2 Player Ultimate TicTacToe Game"""
import random

class UltTicTacToe(object):
    """Initialize game"""
    #Returns nothing
    def __init__(self, board = [], scoreboard = []):
        self.board = board
        self.scoreboard = scoreboard
        if len(board) == 0:
            for i in range(9):
                self.board.append([' ' for i in range(9)])
        if len(scoreboard) == 0:
            for i in range(9):
                self.scoreboard.append(' ')
        self.scoreboard = ['O', 'X', 'O', 'X', 'X', 'O', 'O', 'O', ' ']
    
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
        
    #Print board
    #Returns printed board
    def printBoard(self):
        print "        |         |        "
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[0][0], self.board[0][1], self.board[0][2], self.board[1][0], self.board[1][1], self.board[1][2], self.board[2][0], self.board[2][1], self.board[2][2])
        print "------- | ------- | -------"
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[0][3], self.board[0][4], self.board[0][5], self.board[1][3], self.board[1][4], self.board[1][5], self.board[2][3], self.board[2][4], self.board[2][5])
        print "------- | ------- | -------"
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[0][6], self.board[0][7], self.board[0][8], self.board[1][6], self.board[1][7], self.board[1][8], self.board[2][6], self.board[2][7], self.board[2][8])
        print "        |         |        "
        print "----------------------------"
        print "        |         |        "
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[3][0], self.board[3][1], self.board[3][2], self.board[4][0], self.board[4][1], self.board[4][2], self.board[5][0], self.board[5][1], self.board[5][2])
        print "------- | ------- | -------"
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[3][3], self.board[3][4], self.board[3][5], self.board[4][3], self.board[4][4], self.board[4][5], self.board[5][3], self.board[5][4], self.board[5][5])
        print "------- | ------- | -------"
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[3][6], self.board[3][7], self.board[3][8], self.board[4][6], self.board[4][7], self.board[4][8], self.board[5][6], self.board[5][7], self.board[5][8])
        print "        |         |        "
        print "----------------------------"
        print "        |         |        "
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[6][0], self.board[6][1], self.board[6][2], self.board[7][0], self.board[7][1], self.board[7][2], self.board[8][0], self.board[8][1], self.board[8][2])
        print "------- | ------- | -------"
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[6][3], self.board[6][4], self.board[6][5], self.board[7][3], self.board[7][4], self.board[7][5], self.board[8][3], self.board[8][4], self.board[8][5])
        print "------- | ------- | -------"
        print " %s|%s|%s  |  %s|%s|%s  |  %s|%s|%s " % (self.board[6][6], self.board[6][7], self.board[6][8], self.board[7][6], self.board[7][7], self.board[7][8], self.board[8][6], self.board[8][7], self.board[8][8])
        print "        |         |        "
        print ""
        print "Move Chart     Scoreboard"
        print ""
        print " %s | %s | %s     %s | %s | %s " % (1, 2, 3, self.scoreboard[0], self.scoreboard[1], self.scoreboard[2])
        print "-----------   -----------"
        print " %s | %s | %s     %s | %s | %s " % (4, 5, 6, self.scoreboard[3], self.scoreboard[4], self.scoreboard[5])
        print "-----------   -----------"
        print " %s | %s | %s     %s | %s | %s " % (7, 8, 9, self.scoreboard[6], self.scoreboard[7], self.scoreboard[8])
        print ""

    """Game rules"""
    #Determines if big board is full
    #Returns true/false
    def tied(self):
        for k,v in enumerate(self.scoreboard):
            if (v != 'X' and v != 'O' and v != '-'):
                return False
        return True
        
    #Determines winner of big board
    #Returns player/none
    def winner(self):
        for player in ('X','O'):
            positions = []
            for i in range(9):
                if self.scoreboard[i] == player:
                    positions.append(i)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None
    
    #Determines if a box is won
    #Returns player/none
    def boxWinner(self, box):
        for player in ('X', 'O'):
            positions = []
            for i in range(9):
                if self.board[box][i] == player:
                    positions.append(i)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None
        
    #Determines if a box is tied
    #Returns true/false
    def boxTied(self, box):
        for i in range(9):
            if (self.board[box][i] != 'X' and self.board[box][i] != 'O'):
                return False
        return True
        
    #Determines if game is over
    #Returns true/false
    def gameOver(self):
        if self.winner() or self.tied():
            return True
        return False
    
     #Determines if move is open
    #Returns true/false
    def openMove(self, box, position):
        return (self.board[box][position] != 'X' and self.board[box][position] != 'O')
        
    #See who goes first
    #Returns flag
    def getFirstMove(self):
        if random.randint(0,1) == 0:
            return 'X'
        else:
            return 'O'
            
    #Get enemy team
    #Returns flag
    def getEnemy(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'  
    
    #Determines big board squares occupied by player
    #Returns list
    def getSquares(self, player):
        return [k for k,v in enumerate(self.scoreboard) if v == player]
        
    #Determines unoccupied big board squares
    #Returns list
    def getOpenSquares(self):
        return [k for k,v in enumerate(self.scoreboard) if v != 'X' and v != 'O' and v != '-']

    """Player"""  
    #Get player move
    #Returns index
    def getPlayerMove(self, box, player):
        move = ''
        legal_moves = '1 2 3 4 5 6 7 8 9'.split()
        while move not in legal_moves or not self.openMove(box, int(move)-1):
            print player + ", what is your next move (1-9)"
            move = raw_input()
            try:
                position = int(move)-1
            except:
                print "Please type a number from 1-9."
        return position
        
    #Physically make move and return box/boxes to move in
    def makeMove(self, box, position, player):
        if self.winner():
            pass
        elif self.tied():
            pass
        self.board[box][position] = player
        if self.boxWinner(box):
            self.scoreboard[box] = self.boxWinner(box)
        elif self.boxTied(box):
            self.scoreboard[box] = '-'
        if (self.scoreboard[position] == 'X' or self.scoreboard[position] == 'O' or self.scoreboard[position] == '-'):
            boxes = self.getOpenSquares()
            new_boxes = []
            for b in boxes:
                b = int(b) + 1
                new_boxes.append(b)
            self.printBoard()
            if len(boxes) > 1:
                print self.getEnemy(player) + ", what box would you like to move in?"
                print new_boxes
                box = int(raw_input())-1
            else:
                box = boxes[0]
        else:
            box = position
        return box
                          
"""Creates game"""      
def main():
    while(1):
        game = UltTicTacToe()
        turn = game.getFirstMove()
        print turn + " will go first!"
        firstmove = turn
    
        if firstmove == 'X':
            player = firstmove
            game.printBoard()
            print "What box would you like to move in? (1-9)"
            box = int(raw_input())-1
            move = game.getPlayerMove(box, player)
            box = game.makeMove(box, move, player)
            turn = 'O'
        elif firstmove == 'O':
            player = firstmove
            game.printBoard()
            print "What box would you like to move in?"
            box = int(raw_input())-1
            move = game.getPlayerMove(box, player)
            box = game.makeMove(box, move, player)
            turn = 'X'
    
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'X':
                player = turn
                game.printBoard()
                print "You are in box %s." % (int(box)+1)
                move = game.getPlayerMove(box, player)
                box = game.makeMove(box, move, player)
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
                print "You are in box %s." % (int(box)+1)
                move = game.getPlayerMove(box, player)
                box = game.makeMove(box, move, player)
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
        break
            

"""Runs game"""   
main()