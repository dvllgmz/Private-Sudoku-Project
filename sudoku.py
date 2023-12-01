import sys

import pygame, os
from const import *  # imports constants from const.py
from board import Board

def main():
    current_screen = 'main_menu'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_screen == 'main_menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board = Board(9, 9, screen, 'easy')
                    board.draw()
                    current_screen = 'game'
                continue

            if current_screen == 'game':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell = board.click(event.pos[0], event.pos[1])
                    print(cell)
                    if cell is not None:
                        board.select(cell[0], cell[1])  # selects the box based on coords if it exists
                    board.draw()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if board.select()[1] != 0:  # checks if cell is within bounds
                            board.select(board.select()[0], board.select()[1]-1)
                    if event.key == pygame.K_DOWN:
                        board.select(board.select()[0], board.select()[1]+1)
                    if event.key == pygame.K_LEFT:
                        if board.select()[0] != 0:  # checks if cell is within bounds
                            board.select(board.select()[0]-1, board.select()[1])
                    if event.key == pygame.K_RIGHT:
                        board.select(board.select()[0]+1, board.select()[1])
                    if event.unicode.isdigit():
                        pass

                    board.draw()

                continue

        pygame.display.update()
        # to implement


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sudoku', os.path.join('assets', 'logo.png'))  # set app title
    screen = pygame.display.set_mode((500, 650))  # set app dimensions
    main()  # runs main loop
