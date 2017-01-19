#minimax tictactoe for light practice and showing concepts to tutoring students

#represent tictactoe board spaces are 1-9 represented to user  like so 
# 1 2 3                    0 1 2  
# 4 5 6  and internally as 3 4 5 but flattened as [0 1 2 3 4 5 6 7 8]
# 7 8 9                    6 7 8 
# class representing the game
class Game:
    
    def __init__(self):
         # single list to store board
        self._board = ["-"for x in range(9)]
        #list of possible move wins
        self._winList =[
            [0,1,2],[3,4,5],[6,7,8],
                [0,4,8],[2,4,6],
            [0,3,6],[1,4,7],[2,5,8]
        ]
        # force human to be X can change later
        self._player ="X"
        self._computer = "O"
    # get the board not sure if necessary as i cut this out 
    def getBoard(self):
        return self._board
    
    #play a move
    def play(self,char,space):
        self._board[space]=char

    #check if winner this could be cleaner
    def checkWin(self):
        players =("X","O")
        for player in players:
            for combination in self._winList:
                #check all 3 positions of the combination to see if its the same player
                if self._board[combination[0]]==player and self._board[combination[1]]==player and self._board[combination[2]]==player:
                    return player
        return "-"

    #return valid movees
    def validMoves(self):
        valid =[]
        for i in range(len(self._board)):
            if self._board[i] =="-":
                valid.append(i)
        return valid

    #check if game is down returns tuple of true and winner if it is otherwise false and None
    # could add tuple passing to minimax possibly
    def isDone(self):
        if len(self.validMoves()) ==0 or self.checkWin() != "-":
            return (True,self.checkWin())
        return (False,None)

        #minimax with alpha beta pruning  node represents board state alpha best we've found beta worst we've found
    def minimax(self,player,alpha,beta):
       
            #computer lost
        if self.checkWin()=="X":
            return -1
            #computer won
        elif self.checkWin() =="O":
            return 1
            #tie
        elif len(self.validMoves()) ==0:
            return 0
        # in progress game get children preform minimax with alpha beta
        for space in self.validMoves():
            # play an empty space
            self.play(player,space)
            # comps move
            if player =="O":
                #find score of this branch
                score= self.minimax(self.getOtherPlayer(player),alpha,beta)
                #reset board
                self.play("-",space)
            # check if we found better move
                if score > alpha:
                    alpha = score
                if alpha >=beta:
                    return alpha
            #players move
            elif player == "X":
                 #check if they have a better move
                score = self.minimax(self.getOtherPlayer(player),alpha, beta)
                #reset board
                self.play("-",space)
                if score < beta:
                    beta = score
                if beta <= alpha:
                    return beta

        if player == "X":
            return beta
        return alpha

    #computers turn returns move it should make
    def playComputer(self):
        # impossible heuristic value to start with
        maxvalue = -2
        # impossible move to start with
        moveToMake =-10
        for space in self.validMoves():
            self.play("O", space)
            #check for best move
            # pass -2 and 2 as alpha  and beta  to start 2 is arbitrary as it's outside my heuristic range
            value = self.minimax(self.getOtherPlayer("O"),maxvalue, -maxvalue)
            #reset board
            self.play("-",space)
            if value > maxvalue:
                maxvalue = value
                moveToMake = space
        self.play("O",moveToMake)


    # return opposite of passed player
    def getOtherPlayer(self, player):
        if player =="X":
            return "O"
        return "X"

    def __str__(self):
        s =""
        for i in range(9):
            if i%3 ==0:
                s+="\n"
            s+=" "+self._board[i]
        return s

# could do more validation game breaks if character is given will fix later
if __name__ =="__main__":
    game = Game()
    print("Welcome to Tic Tac Toe when asked to enter a move the positions on the board are labelled as so\n" \
    "1 2 3\n4 5 6\n7 8 9\n")

    while(not game.isDone()[0]):
        valids = game.validMoves()
        print(game)
        userMove = input("Please enter a move: ")
        while int(userMove) >9 or int(userMove) <1 or int(userMove)-1 not in valids:
            userMove = input("Invalid move please enter a valid move: ")
        game.play("X",int(userMove)-1)
        if game.isDone()[0]:
            break
        game.playComputer()
    
    if game.isDone()[1] == "X":
        print("You have won! wait... how?")
        print(game)
    elif game.isDone()[1]=="O":
        print("The computer has won")
        print(game)
    else:
        print("The game was a tie")
        print(game)
        


