"""Board module"""
import pygame

from .constants import (BLACK, COLS, CORNER_SCORE, DIRECTIONS, GREEN, MOBILITY_SCORE, HEIGHT,
                        ROWS, WHITE, WIDTH, CORNERS)
from .piece import Piece


class Board:
    """
    Board Class
    """

    def __init__(self) -> None:
        """initial state"""
        self.board = []
        self.white_left = 30
        self.black_left = 30
        self.create_board()

    def draw_grid(self, window):
        """Drawing The Green background and lines of the Window"""
        window.fill(GREEN)
        for row in range(ROWS):
            pygame.draw.line(window, BLACK, (row * 100, 0),
                             (row * 100, WIDTH), 2)
            pygame.draw.line(window, BLACK, (0, row * 100),
                             (HEIGHT, row * 100), 2)

    def draw(self, window):
        """draws the board and every piece in the Board"""
        self.draw_grid(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    # utility function
    def evaluate(self):
        # TODO : enhance the evaluation function

        # evaluate on x-squares and c-squares

        # evaluate on mobility (early game > late game)
        white_mobility = len(self.get_moves(WHITE)) * (self.white_left / 15)
        black_mobility = len(self.get_moves(BLACK)) * (self.black_left / 15)
        mobility = MOBILITY_SCORE * (white_mobility - black_mobility)

        # evaluate on corners
        corners = 0
        white_corners = 0
        black_corners = 0

        for row, col in CORNERS:
            if self.board[row][col] != 0:
                print("hellooo")
                white_corners += int(self.board[row][col].color == WHITE)
                black_corners += int(self.board[row][col].color == BLACK)

        corners = CORNER_SCORE * (white_corners - black_corners)
        if white_corners != 0 or black_corners != 0:
            print('white corners = ', end='')
            print(white_corners)
            print('black corners = ', end='')
            print(black_corners)
            print('corners: =', corners)


        # evaluate on count of pieces on board
        white_on_board = len(self.get_board_pieces(WHITE))
        black_on_board = len(self.get_board_pieces(BLACK))

        return white_on_board + corners + mobility - black_on_board

    def get_board_pieces(self, color):
        """gets the board pieces based on the color"""
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def insert_piece(self, row, col, color):
        piece = Piece(row, col, color)
        # put the piece
        self.board[row][col] = piece
        self.flip_pieces(row, col)

        # decrease the number of pieces left
        if color == WHITE:
            self.white_left -= 1
        else:
            self.black_left -= 1

    def flip_pieces(self, row, col):
        # my color
        pieces_to_flip = []

        color = self.board[row][col].color

        # try moving in 4 directions
        for x,  y in DIRECTIONS:
            curr_row = row + x
            curr_col = col + y
            # flip until you find a empty spot
            while curr_row in range(8) and curr_col in range(8):
                # found my color , or empty spot
                if self.board[curr_row][curr_col] == 0 or self.board[curr_row][curr_col].color == color:
                    break
                else:
                    pieces_to_flip.append((curr_row, curr_col))

                # update the moves
                curr_row += x
                curr_col += y

            if (curr_row in range(8) and curr_col in range(8)) and self.board[curr_row][curr_col] != 0 and self.board[curr_row][curr_col].color == color:
                for _row, _col in pieces_to_flip:
                    # flip it
                    self.board[_row][_col].flip()

            pieces_to_flip = []

        return pieces_to_flip

    def get_moves(self, color):
        """gets all the  valid move for a color"""

        # insure there is no duplication , minimizing the time taken by the minimax algorithm
        moves = set()

        # get all the pieces inside the board with color
        for piece in self.get_board_pieces(color):

            # get vaild moves for this piece
            for row, col in self.get_valid_moves(piece):
                moves.add((row, col))
        return moves

    def get_valid_moves(self, piece):
        """
        getting all the vaild moves for once piece
        """
        moves = []

        # add [1, 1], [-1, -1], [-1, 1], [1, -1] to add diagonals
        # DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # 0 1 -> right
        # 0 -1 -> left

        # 1 0 -> down
        # -1 0 -> up

        curr_row = piece.row
        curr_col = piece.col

        opponent_color = WHITE if piece.color == BLACK else BLACK

        for x, y in DIRECTIONS:
            row = curr_row + x
            col = curr_col + y

            IS_OPPONENT = False

            while row in range(8) and col in range(8):
                curr_piece = self.board[row][col]
                if curr_piece == 0 or curr_piece.color == piece.color:
                    if IS_OPPONENT and curr_piece == 0:
                        moves.append((row, col))
                    break
                if curr_piece != 0 and curr_piece.color == opponent_color:
                    IS_OPPONENT = True

                row += x
                col += y

        return moves

    def create_board(self):
        # Initail state of the board
        """
        creating a initail state of the board
        """
        for row in range(ROWS):
            self.board.append([])
            for _ in range(COLS):
                self.board[row].append(0)
        # init
        self.board[3][3] = Piece(3, 3, WHITE)
        self.board[4][4] = Piece(4, 4, WHITE)

        self.board[3][4] = Piece(3, 4, BLACK)
        self.board[4][3] = Piece(4, 3, BLACK)

    def winner(self, unmoved=0):
        white_occupy = len(self.get_board_pieces(WHITE))
        black_occupy = len(self.get_board_pieces(BLACK))
        if white_occupy + black_occupy == 64 or unmoved >= 2:
            print(white_occupy, "   ", black_occupy)
            if white_occupy == black_occupy:
                return "Tie"
            elif white_occupy > black_occupy:
                return "white"
            else:
                return "black"

        return None
