"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in board:
        for j in i:
            if j is not EMPTY:
                count += 1
    if count % 2 == 0:
        return X
    elif count % 2 != 0:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                possibleActions.append((i,j))
    possibleActions = set(possibleActions)
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    i = action[0]
    j = action[1]

    if i < 0 or j < 0:  #checks negative move
        raise "Negative Move!!" # type: ignore
    
    if newBoard[i][j] == EMPTY:  #checks if the square is empty
        if player(board) == X:
            newBoard[i][j] = X
        elif player(board) == O:
            newBoard[i][j] = O
    else:
        raise "Wrong Move"  # type: ignore #raises exception if clicked on square that is not empty
        
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #returns None if initial board
    if board == initial_state():
        return None
    
    #CHECKS HORIZONTAL
    for i in board:
        if i == [X,X,X]:
            return X
        if i == [O,O,O]:
            return O
    
    #checks vertically
    if board[0][0] == board[1][0] == board[2][0] == X:
        return X
    if board[0][1] == board[1][1] == board[2][1] == X:
        return X
    if board[0][2] == board[1][2] == board[2][2] == X:
        return X
    
    if board[0][0] == board[1][0] == board[2][0] == O:
        return O
    if board[0][1] == board[1][1] == board[2][1] == O:
        return O
    if board[0][2] == board[1][2] == board[2][2] == O:
        return O

    #checks diagonal
    diaCountX = 0
    diaCountXback = 0
    diaCountO = 0
    diaCountOback = 0
    for i in range(len(board)):
        if board[i][i] == X:
            diaCountX += 1 
        if board[i][i] == O:
            diaCountO += 1
        if board[i][(len(board)-i)-1] == X:
            diaCountXback += 1
        if board[i][(len(board)-i)-1] == O:
            diaCountOback += 1
    if diaCountX == 3 or diaCountXback == 3:
        return X
    if diaCountO == 3 or diaCountOback == 3:
        return O
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """ 
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != EMPTY:
                count += 1
    if winner(board) or count == 9:
        return True
    else:
        return False
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

difficulty = 0.9
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if random.random() < difficulty:
        best_move = None
        if player(board) == X:
            a = -math.inf
            for action in actions(board):
                v = minValue(result(board, action))
                if v > a:
                    a = v
                    best_move = action
        elif player(board) == O:
            a = math.inf
            for action in actions(board):
                v = maxValue(result(board, action))
                if v < a:
                    a = v
                    best_move = action
        return best_move
    else:
        return random.choice(list(actions(board)))

def maxValue(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action)))
    return v

def minValue(state):
    if terminal(state):
        return utility(state)
    v = math.inf    
    for action in actions(state):
        v = min(v, maxValue(result(state, action)))
    return v