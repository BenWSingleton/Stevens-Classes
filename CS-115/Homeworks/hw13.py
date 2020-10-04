#Benjamin Singleton
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *

debug=False

class Board:
    def __init__(self, width=7, height=6):
        """Constructor for the board, if no inputs are given, width=7 and height=6"""
        self.row=width
        self.col=height
        self.arr=createBoard(height, width)

    def __str__(self):
        """Returns the board in the form of a string"""
        board=""
        for row in self.arr:
            for col in row:
                board+="|"+col
            board+="|\n"
        board+="-"*self.row*2+"-"
        count=0
        bar=""
        for n in range(self.row):
            bar+=" "+str(count)
            count+=1
        board+="\n"+bar
        return board
    
    def allowsMove(self, col):
        """Returns true there is an open space on the top of a row, otherwies returns false"""
        if col<0 or col>self.col:
            return False
        for rows in range(len(self.arr)):
            if self.arr[rows][col]==" ":
                return True
        return False

    def addMove(self, col, ox):
        """Uses findHighest() to find the first open spot in col and places a move in that spot"""
        add=""
        if ox=="X":
            add+="X"
        else:
            add+="O"
        high=self.findHighest(col)
        self.arr[high][col]=add   

    def findHighest(self, col):
        """Finds the first open space from bottom up in col"""
        for n in range(len(self.arr)-1,-1,-1):
            if self.arr[n][col]==" ":
                return n 

    def setBoard(self, move_string):
        """ takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'

         For example, call b.setBoard('012345')
         to see 'X's and 'O's alternate on the
         bottom row, or b.setBoard('000000') to
         see them alternate in the left column.
         moveString must be a string of integers
         """
        nextCh = 'X' # start by playing 'X'
        for colString in move_string:
            col = int(colString)
            if 0 <= col <= self.row:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def delMove(self, col):
        """Removes a move from the board in col""" 
        if self.arr[col][len(self.arr)-1]==" ":
            return
        high=self.findHighest(col)
        self.arr[high+1][col]=" "
        
    def winsFor(self, ox):
        """Checks if i player has achieved a horizontal, vertical, or diagonal win"""
        turn=""
        if ox=="X":
            turn+="X"
        else:
            turn+="O"
        
        def horizontal():
            """Checks for horizontal wins"""
            if debug: print("DEBUG: Checking horizontal win for",turn)
            count=1
            for rows in range(self.col):
                if count==4:
                    return True
                count=1
                for cols in range(self.row-1):
                    if self.arr[rows][cols]==turn and self.arr[rows][cols]==self.arr[rows][cols+1]:
                        count+=1
                if count==4:
                    return True

        def vertical():
            """Checks for vertical wins"""
            if debug: print("DEBUG: Checking vertical win for",turn)
            for rows in range(self.col-3):
                for cols in range(self.row):
                    found = True
                    for n in range(4):
                        if self.arr[n+rows][cols]==" ":
                            found = False
                            break
                        elif self.arr[n+rows][cols]!=turn:
                            found = False
                            break
                    if found == True:
                        return True       
            return False

#start from every siongle point
#double for loop 
#with while (in range) loop inside
        #def diagonal():
         #   for rows in range(self.col):
          #      for cols in range(self.row):
           #         tempRow=rows
            #        tempCol=cols
             #       while tempRow and tempCol in range(self.col) and range(self.row):
                        
            
        
            
        

        if horizontal()==True:
            return True
        if vertical()==True:
            return True
        #if diagonal()==True:
        #    return True
        return False

    def isFull(self):
        if debug: print("DEBUG: Checking if the board is full")
        for rows in range(self.row):
            for cols in range(self.col):
                if self.arr[rows][cols]==" ":
                    return False
        return True

    def hostGame(self):
        """Runs the game"""
        print("Welcome to Connect Four!")
        print(self)
        win=False
        while True:
            if self.isFull()==True:
                print("Nobody wins, you both suck!")
                print(b)
                break
            while True:
                playerInput=input("X's Choice: ")
                if self.allowsMove(int(playerInput))==True:
                    break
                print("Enter a valid column")
            self.addMove(int(playerInput), "X")
            if self.winsFor("X")==True:
                print("X Wins -- Congratulations!")
                print(b)
                break
            print(b)
            if self.isFull()==True:
                print("Nobody wins, you both suck!")
                print(b)
                break
            while True:
                playerInput=input("O's Choice: ")
                if self.allowsMove(int(playerInput))==True:
                    break
                print("Enter a valid column")
            self.addMove(int(playerInput), "O")
            if self.winsFor("O")==True:
                print("O winns -- Congratulations!")
                print(b)
                break
            print(b)

def createBoard(row,col):
    """Creates a board"""
    board=[]
    for r in range(row):
        r=[]
        for c in range(col):
            r+=[" "]
        board.append(r)
    #print(board)
    return board
