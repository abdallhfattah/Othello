# Othello Game - Minimax Algorithm

This directory contains the implementation of the Minimax algorithm for the AI gameplay in the Othello game.

## Algorithm Implementation

The `minimaxAlgo.py` module implements the Minimax algorithm with Alpha-Beta Pruning for making intelligent moves by the AI player. Here's a brief overview of its key components:

- **Minimax Function**: The `minimax` function is the core of the algorithm. It recursively evaluates possible moves and selects the best move for the AI player.
- **Simulation of Moves**: The `simulate_move` function simulates placing a piece on the board to evaluate its potential outcome.
- **Getting All Possible Moves**: The `get_all_moves` function generates all possible future board states resulting from valid moves for a given player.
- **Depth and Pruning**: The algorithm considers a specified depth to limit the search space and employs Alpha-Beta Pruning to improve efficiency by eliminating unnecessary branches.

## Usage

To use the Minimax algorithm for AI gameplay in the Othello game, import the `minimaxAlgo` module and call the `minimax` function with the appropriate parameters. For example:

```python
from minimax import minimaxAlgo
```
# Assuming 'board' is the current game board and 'depth' is the specified depth level
best_move = minimaxAlgo.minimax(board, depth, float('-inf'), float('inf'), True)[1]
