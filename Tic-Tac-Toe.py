import numpy as np
import copy
import random

class Game(object):
    def restart(self,state):
        # Returns a representation of the starting state of the game.
        # state[0] is the board, state[1] is the turn counter
        state[1] = 0
        for i in range (0,3):
            state[0][i] =0


    def current_player(self, state):
        # Takes the game state and returns the current player's
        # number.
        turn = (state[1]%2) +1
        return turn

    def next_player(self, state):
        #returns next player
        turn=state[1]+1
        return turn

    def next_state(self, state, play):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        row = play[0]
        col = play[1]
        board=state[0]
        if(self.is_legal(self,board,row,col)):
            board[row][col]=self.current_player(self,state)
            return [board,self.next_player(self,state)]
        return state

    def is_legal(self,board,row,col):
        if(board[row][col] == 0):
            return True
        return False

    def legal_plays(self, state_history):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        pass




    def check_winner(self,state):
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        board=state[0]
        for i in range(0,3):
            if(sum(board[i])%3 == 0 and 0 not in board[i]):
                return self.current_player(self,state)
            if(sum(board[:,i])%3 == 0 and 0 not in board[:,i]):
                return self.current_player(self,state)

        if(sum(board.diagonal())%3 == 0 and 0 not in board.diagonal()):
            return self.current_player(self,state)
        temp = copy.deepcopy(board[:,0])
        board[:,0] = board [:,2]
        board[:,2] = temp

        if(sum(board.diagonal())%3 == 0 and 0 not in board.diagonal()):
            return self.current_player(self,state)

        if(0 not in board):
            return -1;

        return 0;

if __name__ == '__main__':
    a=np.array([[1,2,1],
                [2,2,1],
                [1,2,2]])
    g = Game
    state = [a,0]
    g.restart(g,state)

    for x in range(0,10000):
        g.restart(g,state)
        while(g.check_winner(g,state) == 0):
            x = random.randrange(0,3)
            y = random.randrange(0,3)
            state=g.next_state(g,state,[x,y])
        print(state)
        print(g.check_winner(g,state))



