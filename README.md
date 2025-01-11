**AKINSEYE AKINWANDE 73524358
GUVEN CIRPANLI 27454246
IHSAN KARABACAK 55663115
ABDUL-RAZAK RAHAMA SAANA 81832589**

**Chess Game with AI Opponent in Python**

**Overview**

This project is a Python-based chess game that allows a player to compete against an AI opponent. It features a fully functional 8x8 chess board, implements the standard movement rules for each chess piece, and supports alternating turns between the player and the AI.
**Features**

**Chess Pieces:**

The game includes all standard chess pieces: Pawn, Rook, Knight, Bishop, Queen, and King.
Each piece has its unique movement rules implemented in the code.
**Board:**

An 8x8 board is initialized with the standard chess starting positions.
The board can display the current state of the game.

**Player Interaction:**

The player can input moves using standard algebraic notation (e.g., e2 e4).

**AI Opponent:**

The AI generates random valid moves for black pieces.

**Move Validation:
**

The game checks if a move is valid before executing it.

**How to Run
Prerequisites:**


Python 3.x installed on your system.

**Running the Game:**

 python chess_game.py


The game starts with the player controlling the white pieces.
The player is prompted to enter moves in the format: <start_position> <end_position> (e.g., e2 e4).

**Gameplay:**


The player moves first, followed by the AI.
The game continues until one side has no valid moves or a checkmate occurs.

**Code Structure
Classes:**

Piece: Base class for all chess pieces.
Pawn, Rook, Knight, Bishop, Queen, King: Derived classes implementing specific movement rules.
Board: Manages the board state, initializes the pieces, and handles move execution.
AI: Generates random valid moves for the AI opponent.

**Functions:**

valid_moves: Determines the valid moves for a piece based on its type and position.
move_piece: Executes a move if it's valid.
print_board: Displays the current board state.

**Example Gameplay
Initial board setup:**

   a  b  c  d  e  f  g  h
8  r  n  b  q  k  b  n  r  8
7  p  p  p  p  p  p  p  p  7
6  .  .  .  .  .  .  .  .  6
5  .  .  .  .  .  .  .  .  5
4  .  .  .  .  .  .  .  .  4
3  .  .  .  .  .  .  .  .  3
2  P  P  P  P  P  P  P  P  2
1  R  N  B  Q  K  B  N  R  1
   a  b  c  d  e  f  g  h


Player enters a move: e2 e4
AI responds with a random valid move.

**Future Enhancements**

Improved AI:


Implement smarter move selection using algorithms like Minimax or Alpha-Beta Pruning.
Advanced Rules:


Add support for special moves such as castling, en passant, and pawn promotion.
Implement check, checkmate, and stalemate detection.
Graphical User Interface (GUI):


Develop a GUI for the game using libraries such as Tkinter or Pygame.

**Acknowledgements**

Inspired by standard chess rules and gameplay.
Built using Python programming language.
