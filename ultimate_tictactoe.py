"""Ultimate Tic Tac Toe Game"""
from Tkinter import *
from tkFont import Font
from copy import deepcopy

class Board:
    def __init__(self,other=None):
        self.player = 'X'
        self.opponent = 'O'
        self.empty = ' '
        self.size = 9
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x,y] = self.empty
        if other:
            self.__dict__ = deepcopy(other.__dict__)
            
    def tied(self):
        for (x,y) in self.fields:
            if self.fields[x,y] == self.empty:
                return False
        return True
        
    
    
    
            
class GUI:
    def __init__(self):
        self.app = Tk()
        self.app.title('TicTacToe')
        self.board = Board()
        self.font = Font(family="Helvetica", size=32)
        self.buttons = {}
        for x,y in self.board.fields:
            #handler function
            button = Button(self.app, font = self.font, width = 1, height = 1)
            button.grid(row=y, column=x)
            self.buttons[x,y] = button   
        #handler function
        button = Button(self.app, text='reset')
        button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky="WE")            
    
    def mainloop(self):
        self.app.mainloop()
        
if __name__ == '__main__':
    GUI().mainloop()