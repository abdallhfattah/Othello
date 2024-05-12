import pygame
from .constants import WHITE, SQUARE_SIZE, BLACK, ROWS, COLS, GREEN, WIDTH, HEIGHT
from .piece import Piece


class Board:
    def __init__(self) -> None:
        self.board = []
        self.white_left = 30
        self.black_left = 30
        self.create_board()

    def draw_grid(self, window):
        window.fill(GREEN)
        for row in range(ROWS):
            pygame.draw.line(window, BLACK, (row * 100, 0), (row * 100, WIDTH), 3)
            pygame.draw.line(window, BLACK, (0, row * 100), (HEIGHT, row * 100), 3)

    def draw(self, window):
        self.draw_grid(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    # utility function
    def evaluate(self):
        return self.white_left - self.black_left

    def get_board_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    
    def get_valid_moves(self, piece):
        moves = []
        # added [1, 1], [-1, -1], [-1, 1], [1, -1] to add diagonals
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        curr_row = piece.row
        curr_col = piece.col

        opponent_color = WHITE if piece.color == BLACK else BLACK

        for x, y in directions:
            row = curr_row + x
            col = curr_col + y
            IS_OPPONENT = False

            while row in range(8) and col in range(8):
                curr_piece = self.board[row][col]
                if curr_piece == 0:
                    if IS_OPPONENT:
                        moves.append((row, col))
                    else:
                        break
                if curr_piece != 0 and curr_piece.color == opponent_color:
                    IS_OPPONENT = True
                row += x
                col += y
        return moves

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for _ in range(COLS):
                self.board[row].append(0)
        self.board[3][3] = Piece(3, 3, WHITE)
        self.board[4][4] = Piece(4, 4, WHITE)
        self.board[3][4] = Piece(3, 4, BLACK)
        self.board[4][3] = Piece(4, 3, BLACK)
