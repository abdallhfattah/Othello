# Othello Game - Game Directory

This directory contains modules related to the game logic and user interface of the Othello game.

## Modules

### board.py

- **Description**: Defines the Othello board and related functions.
- **Contents**: Includes classes and functions for managing the game board, checking for valid moves, and updating the board state.

### constants.py

- **Description**: Contains constants used throughout the game.
- **Contents**: Includes definitions for game constants such as screen dimensions, colors, difficulty levels, and utility scores.

### controller.py

- **Description**: Manages the game state and user interactions.
- **Contents**: Implements the GameController class, which handles user input, updates the game state, and controls the flow of the game.

### disk.py

- **Description**: Defines the disk piece used in the game.
- **Contents**: Contains the Disk class, representing a disk piece on the game board. It includes methods for setting the color of the disk and rendering it on the board.

### __init__.py

- **Description**: Python package initialization file.
- **Contents**: Typically empty, used to indicate that the directory should be treated as a package.

### __pycache__

- **Description**: Automatically generated directory by Python for compiled bytecode.
- **Contents**: Contains compiled bytecode files for the Python modules in the directory.

## Board Module

The `board.py` module defines the Othello board and related functionality. Here's a brief overview of its key components:

- **Initialization**: The `__init__` method initializes the board state and sets up the initial configuration.
- **Drawing Functions**: The `draw_grid` and `draw` methods handle the visualization of the game board and pieces.
- **Utility Functions**: Methods like `evaluate`, `get_board_pieces`, `insert_piece`, `flip_pieces`, `get_moves`, and `get_valid_moves` are responsible for various aspects of game state evaluation and manipulation.
- **Winner Determination**: The `winner` method determines the winner of the game based on the current board state.

## Constants Module

The `constants.py` module contains constants used throughout the game, including colors, screen dimensions, difficulty levels, and utility scores.

## Disk Module

The `disk.py` module defines the Disk class, representing a disk piece used in the game. It includes methods for drawing the disk, flipping its color, and obtaining its string representation.

## Usage

To use the modules in this directory, import them into your Python scripts as needed. For example:

```python
from game import board, constants, controller, disk
```

## Contributing
Contributions to the game logic and user interface are welcome! Feel free to open issues for any bugs or suggestions for improvements. Pull requests are also appreciated.