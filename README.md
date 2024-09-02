# Tic-Tac-Toe Game with AI

This project is a command-line Tic-Tac-Toe game where you can play against an AI. The AI uses the minimax algorithm to make optimal moves. The game is implemented in Python and provides a simple and interactive way to play Tic-Tac-Toe.

## Features

- Play as either "X" or "O"
- The AI uses the minimax algorithm to make decisions
- Error handling for invalid moves
- Displays the game board after each move
- Provides the game result at the end (win, lose, or tie)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GauravHemrajani/Tic-Tac-Toe.git
2. Navigate to the project directory:
   cd Tic-Tac-Toe
3. Run the game:
   python tictactoe.py

## How to Play
1. The game will ask you to choose your symbol (X or O).
2. The game will print the current state of the board.
3. If it’s your turn, you will be prompted to enter your move. The format for entering a move is row,col (e.g., 1,2).
4. If you enter an invalid move (e.g., selecting an occupied cell or entering a position out of bounds), the game will ask you to try again.
5. The AI will take its turn after yours.
6. The game will continue until there's a winner or the board is full (tie).

## Dependencies:
Python 3.x
Ensure that you have Python installed on your system. There are no external dependencies required for this project.

## Project Structure:
tictactoe.py: The main file to run the Tic-Tac-Toe game.
funcs.py: Contains the game logic including the minimax algorithm and other helper functions.

## Contact:
For any questions or feedback, please contact hemrajanifamily@gmail.com.
