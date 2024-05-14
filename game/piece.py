import pygame

from .constants import BLACK, GREY, OUTLINE, PADDING, SQUARE_SIZE, WHITE


class Piece:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.piece_pos()

    def piece_pos(self):
        self.x = (SQUARE_SIZE * self.col) + (SQUARE_SIZE // 2)
        self.y = (SQUARE_SIZE * self.row) + (SQUARE_SIZE // 2)

    def draw(self, window):
        radius = (SQUARE_SIZE // 2) - PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

    def flip(self):
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE

    def __repr__(self):
        return str(self.color)
