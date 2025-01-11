import random

# Base Class for Chess Pieces
class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = None

    def valid_moves(self, board, x, y):
        return []  # To be overridden by specific pieces

    def __str__(self):
        return self.symbol


# Specific Chess Pieces
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "P" if color == "white" else "p"

    def valid_moves(self, board, x, y):
        moves = []
        direction = -1 if self.color == "white" else 1
        if 0 <= x + direction < 8 and board[x + direction][y] is None:
            moves.append((x + direction, y))
        if 0 <= x + direction < 8 and y - 1 >= 0 and board[x + direction][y - 1] and board[x + direction][y - 1].color != self.color:
            moves.append((x + direction, y - 1))
        if 0 <= x + direction < 8 and y + 1 < 8 and board[x + direction][y + 1] and board[x + direction][y + 1].color != self.color:
            moves.append((x + direction, y + 1))
        return moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "R" if color == "white" else "r"

    def valid_moves(self, board, x, y):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            i, j = x, y
            while 0 <= i + dx < 8 and 0 <= j + dy < 8:
                i += dx
                j += dy
                if board[i][j] is None:
                    moves.append((i, j))
                elif board[i][j].color != self.color:
                    moves.append((i, j))
                    break
                else:
                    break
        return moves


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "N" if color == "white" else "n"

    def valid_moves(self, board, x, y):
        moves = []
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for dx, dy in directions:
            i, j = x + dx, y + dy
            if 0 <= i < 8 and 0 <= j < 8 and (board[i][j] is None or board[i][j].color != self.color):
                moves.append((i, j))
        return moves


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "B" if color == "white" else "b"

    def valid_moves(self, board, x, y):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            i, j = x, y
            while 0 <= i + dx < 8 and 0 <= j + dy < 8:
                i += dx
                j += dy
                if board[i][j] is None:
                    moves.append((i, j))
                elif board[i][j].color != self.color:
                    moves.append((i, j))
                    break
                else:
                    break
        return moves


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "Q" if color == "white" else "q"

    def valid_moves(self, board, x, y):
        return Rook(self.color).valid_moves(board, x, y) + Bishop(self.color).valid_moves(board, x, y)


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "K" if color == "white" else "k"

    def valid_moves(self, board, x, y):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dx, dy in directions:
            i, j = x + dx, y + dy
            if 0 <= i < 8 and 0 <= j < 8 and (board[i][j] is None or board[i][j].color != self.color):
                moves.append((i, j))
        return moves


# Board Class
class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        for i in range(8):
            self.board[1][i] = Pawn("black")
            self.board[6][i] = Pawn("white")
        self.board[0][0] = self.board[0][7] = Rook("black")
        self.board[7][0] = self.board[7][7] = Rook("white")
        self.board[0][1] = self.board[0][6] = Knight("black")
        self.board[7][1] = self.board[7][6] = Knight("white")
        self.board[0][2] = self.board[0][5] = Bishop("black")
        self.board[7][2] = self.board[7][5] = Bishop("white")
        self.board[0][3] = Queen("black")
        self.board[7][3] = Queen("white")
        self.board[0][4] = King("black")
        self.board[7][4] = King("white")

    def print_board(self):
        print("   a  b  c  d  e  f  g  h")
        for i, row in enumerate(self.board):
            print(f"{8 - i} ", end="")
            for piece in row:
                print(f" {piece if piece else '.'} ", end="")
            print(f" {8 - i}")
        print("   a  b  c  d  e  f  g  h")

    def move_piece(self, start, end):
        sx, sy = 8 - int(start[1]), ord(start[0]) - ord("a")
        ex, ey = 8 - int(end[1]), ord(end[0]) - ord("a")
        piece = self.board[sx][sy]
        if piece and (ex, ey) in piece.valid_moves(self.board, sx, sy):
            self.board[ex][ey] = piece
            self.board[sx][sy] = None
            return True
        return False


# AI Opponent
class AI:
    @staticmethod
    def make_move(board, color):
        moves = []
        for x in range(8):
            for y in range(8):
                piece = board[x][y]
                if piece and piece.color == color:
                    for move in piece.valid_moves(board, x, y):
                        moves.append(((x, y), move))
        if moves:
            return random.choice(moves)
        return None


# Game Loop
def play_game():
    board = Board()
    turn = "white"
    ai = AI()

    while True:
        board.print_board()
        if turn == "white":
            print("Your turn (white).")
            move = input("Enter your move (e.g., e2 e4): ").split()
            if len(move) != 2:
                print("Invalid input. Try again.")
                continue
            if board.move_piece(move[0], move[1]):
                turn = "black"
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn (black).")
            ai_move = ai.make_move(board.board, "black")
            if ai_move:
                start, end = ai_move
                start_pos = f"{chr(start[1] + ord('a'))}{8 - start[0]}"
                end_pos = f"{chr(end[1] + ord('a'))}{8 - end[0]}"
                board.move_piece(start_pos, end_pos)
                print(f"AI moved from {start_pos} to {end_pos}")
                turn = "white"
            else:
                print("AI has no valid moves. Game over.")
                break

if __name__ == "__main__":
    play_game()
