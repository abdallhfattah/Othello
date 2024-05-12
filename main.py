import pygame
from game.board import Board
from game.mygame import Game
from game.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE

FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.draw(WINDOW)
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)
    #     clock.tick(FPS)

        # if game.turn == WHITE:
        #     value, new_board = minimax(game.get_board(), 3, WHITE, game)
        #     game.ai_move(new_board)

        # if game.winner() != None:
        #     print(game.winner())
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        game.update
    pygame.quit()


main()
