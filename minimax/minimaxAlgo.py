from copy import deepcopy

from game.board import Board
from game.constants import BLACK, WHITE


# minimax => board , depth , max_player
def minimax(board, depth, alpha, beta, max_player):
    if depth == 0 or board.winner() != None:
        return board.evaluate(), board

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for new_board in get_all_moves(board, WHITE):
            # check the evaluation of this new_board
            evaluation = minimax(new_board, depth - 1, alpha, beta, False)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            # if this new_board is the max evaluation
            if maxEval == evaluation:
                best_move = new_board
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for new_board in get_all_moves(board, BLACK):
            evaluation = minimax(new_board, depth - 1, alpha, beta, True)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if minEval == evaluation:
                best_move = new_board
            if beta <= alpha:
                break
        return minEval, best_move


def simulate_move(row, col, board, color):
    board.insert_piece(row, col, color)
    return board


def get_all_moves(board: Board, color):
    moves = []
    for row, col in board.get_moves(color):
        # draw_moves(game, board, piece)
        temp_board = deepcopy(board)
        new_board = simulate_move(row, col, temp_board, color)
        moves.append(new_board)
    return moves


# def draw_moves(game, board, piece):
#     valid_moves = board.get_valid_moves(piece)
#     board.draw(game.win)
#     pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
#     game.draw_valid_moves(valid_moves.keys())
#     pygame.display.update()
#     pygame.time.delay(50)
