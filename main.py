import pygame

from game.board import Board
from game.constants import FPS, HEIGHT, WIDTH, get_coordinate_mouse
from game.mygame import Game

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Othello')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.draw(WINDOW)
    game = Game(WINDOW)
    s = 1
    while run:
        clock.tick(FPS)

        # if game.turn == WHITE:
        #     value, new_board = minimax(game.get_board(), 3, WHITE, game)
        #     game.ai_move(new_board)

        # if game.winner() != None:
        #     print(game.winner())
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_coordinate_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()   


main()
