# dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
RED = (255, 0, 0)

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

BLUE = (0, 0, 255)

GREY = (128, 128, 128)

GREEN = (0, 188, 140)

# Diagonal directions ([1, 1], [-1, -1], [-1, 1], [1, -1])
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

CORNER_SCORE = 50
MOBILITY_SCORE = 5


CORNERS = [[0, 0], [0, 7], [7, 0], [7, 7]]
X_SQUARES = [[1, 1], [1, 6], [6, 1], [6, 6]]
C_SQUARES = [[1, 0], [6, 0], [0, 1], [7, 1], [0, 6], [7, 6], [1, 7], [6, 7]]

# Render
FPS = 60

# Utility function


def get_coordinate_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


PADDING = 15
OUTLINE = 2

# ai level
EASY = 2
MEDIUM = 4
HARD = 6
