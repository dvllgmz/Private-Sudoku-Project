import sys

import pygame, os
from const import *  # imports constants from const.py
from board import Board

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if s
                pass

            board = Board(9, 9, screen, 'easy')
            board.draw()

        pygame.display.update()
        # to implement


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sudoku', os.path.join('assets', 'logo.png'))  # set app title
    screen = pygame.display.set_mode((500, 650))  # set app dimensions
    main()  # runs main loop
