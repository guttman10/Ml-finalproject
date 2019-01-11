import numpy as np
import copy
import random

def MonteCarloTreeSearch (g,curr_state,move_list):
    best_move = 0
    second_best = 0
    move_index=0
    val_list = []
    for move in move_list:
        move_val = 0

        for i in range(0,100):
            pboard = copy.deepcopy(curr_state[0])
            turn = curr_state[1]
            test_state = (pboard, turn)
            test_state = g.next_state(g, test_state, move)

            while(g.check_winner(g,test_state) == 0):
                random_move = (random.randrange(0, 3), random.randrange(0, 3))
                test_state = g.next_state(g,test_state,random_move)

            if( g.check_winner(g, test_state) == 1 ):
                move_val += 1

        if(move_val > best_move):
            second_best = best_move
            best_move = move_index

        move_index += 1

    i=random.randrange(1, 4)
    if( i%2 == 0):
        best_move = second_best

    return move_list[best_move]


class Game(object):
    def restart(self, state):
        # Returns a representation of the starting state of the game.
        # state[0] is the board, state[1] is the turn counter
        state[1] = 0
        for i in range(0, 3):
            state[0][i] = 0


    def current_player(self, state):
        # Takes the game state and returns the current player's
        # number.
        turn = (state[1]%2) +1
        return turn

    def next_player(self, state):
        #returns next player
        turn=state[1]+1
        return turn

    def next_state(self, state, move):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        row = move[0]
        col = move[1]
        board=state[0]
        if(self.is_legal(self,board,move)):
            board[row][col]=self.current_player(self,state)
            if(self.check_winner(self,(board,state[1])) == 0):
                return [board,self.next_player(self,state)]
            else:
                return [board,state[1]]
        return state

    def is_legal(self, board,move):
        if(board[move[0]][move[1]] == 0):
            return True
        return False

    def legal_plays(self, state):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        board = state[0]
        turn = state[1]
        move_list = []
        for i in range (0,3):
            for j in range(0,3):
                move=(i,j)
                if (self.is_legal(self, board, move)):
                     move_list.append((i, j))

        return move_list


    def check_winner(self,state):
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        board=state[0]
        for i in range(0,3):
            if(sum(board[i])%3 == 0 and 0 not in board[i]):
                return self.current_player(self, state)
            if(sum(board[:, i])%3 == 0 and 0 not in board[:, i]):
                return self.current_player(self, state)

        if(sum(board.diagonal())%3 == 0 and 0 not in board.diagonal()):
            return self.current_player(self, state)
        temp = copy.deepcopy(board[:,0])
        board[:,0] = board [:,2]
        board[:,2] = temp

        if(sum(board.diagonal())%3 == 0 and 0 not in board.diagonal()):
            return self.current_player(self, state)

        if(0 not in board):
            return -1

        return 0


if __name__ == '__main__':

    a=np.array([[1,2,1],
                [2,2,1],
                [1,2,2]])
    g = Game
    state = [a, 0]
    for i in range(0,100):
        g.restart(g, state)
        while(g.check_winner(g, state) == 0):
            m = g.legal_plays(g, state)
            move = MonteCarloTreeSearch(g, state, m)
            state = g.next_state(g, state, move)
        print("Player", g.check_winner(g,state), "Wins!")
        print(state)




