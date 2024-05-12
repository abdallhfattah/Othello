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

# directions
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


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
SEARCH_DEPTH = 5