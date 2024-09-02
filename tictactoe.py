import funcs as ttt
import copy
import time

X = "X"
O = "O"
EMPTY = None

board = ttt.initial_state()
aiTurn = False
run = True

userChoice = input("What do you want to play as, X or O: ").upper()
user = None
if userChoice == "X":
    user = X
if userChoice == "O":
    user = O

def printBoard(board):
    newBoard = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if newBoard[i][j] == EMPTY:
                newBoard[i][j] = "_"
    print("----0---1---2-----")
    print(f"0 | {newBoard[0][0]} | {newBoard[0][1]} | {newBoard[0][2]} |")
    print("---------------")
    print(f"1 | {newBoard[1][0]} | {newBoard[1][1]} | {newBoard[1][2]} |")
    print("---------------")
    print(f"2 | {newBoard[2][0]} | {newBoard[2][1]} | {newBoard[2][2]} |")
    print("------------------")

if user == None:
    print('Please choose either X or O!')
    run = False
if run == True:
    printBoard(board)

while run:
    if ttt.terminal(board): # if game over, stop the loop and print the result
        if ttt.utility(board) == 1: # if X won the game
            if user == X:
                print("User wins!")
            if user == O:
                print("AI wins!")
        if ttt.utility(board) == -1: # if O won the game
            if user == O:
                print("User wins!")
            if user == X:
                print("AI wins!")
        if ttt.utility(board) == 0: # if tie
            print("Tie!")
        run = False

    playerTurn = ttt.player(board)

    if user != playerTurn:
        if aiTurn == True and not ttt.terminal(board):
            aiMove = ttt.minimax(board)
            board = ttt.result(board, aiMove)
            print("AI is thinking")
            time.sleep(1)
            printBoard(board)
            aiTurn = False
        else:
            aiTurn = True

    if user == playerTurn:
        if aiTurn == False and not ttt.terminal(board):
            while True:
                try:
                    userPlay = input("Enter the move that you want to play (format: row,col): ")
                    userPlay.replace(" ", "")
                    userPlay = tuple(map(int, userPlay.split(',')))
                    if board[userPlay[0]][userPlay[1]] != EMPTY:
                        raise ValueError("Invalid move: Position already taken.")
                    board = ttt.result(board, userPlay)
                    break
                except (ValueError, IndexError):
                    print("Invalid move. Please enter a valid position in the format 'row,col' and ensure the spot is empty.")
            printBoard(board)
            aiTurn = True