import sys

import pygame, os
from const import *  # imports constants from const.py
from board import Board


def main_menu():  # prints main menu  #fixme: IMPLEMENT QUIT BUTTON AND BUTTON AREA DETECTION
    start_button = pygame.Rect(100, 200, 300, 150)  # start button box
    pygame.draw.rect(screen, BOLD_LINE_COLOR, start_button)  # draws button
    start_button_font = pygame.font.Font(None, 50)  # initializes font
    start_button_rendered = start_button_font.render('START GAME', 1, GIVEN_NUMBER_COLOR)  # renders font
    screen.blit(start_button_rendered, start_button_rendered.get_rect(center=(250, 275)))  # renders text

def main():
    current_screen = 'main_menu'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_screen == 'main_menu':
                main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:  #fixme: Check area where mouse is clicked
                    #fixme: Finish the home screen and implement board generation and button area detection

                    board = Board(9, 9, screen, 'easy')
                    board.draw()
                    current_screen = 'game'
                continue

            if current_screen == 'game':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell = board.click(event.pos[0], event.pos[1])
                    if cell is not None:
                        board.select(cell[0], cell[1])  # selects the box based on coords if it exists
                    board.draw()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if board.select()[0] != 0:  # check if cell is within bounds
                            board.select(board.select()[1], board.select()[0]-1)
                    if event.key == pygame.K_DOWN:
                        if board.select()[0] != 8:  # check if cell is within bounds
                            board.select(board.select()[1], board.select()[0]+1)
                    if event.key == pygame.K_LEFT:
                        if board.select()[1] != 0:  # checks if cell is within bounds
                            board.select(board.select()[1]-1, board.select()[0])
                    if event.key == pygame.K_RIGHT:
                        if board.select()[1] != 8:  # check if cell is within bounds
                            board.select(board.select()[1]+1, board.select()[0])
                    if event.unicode.isdigit():  # if user presses a number (converts event to unicode which gives key)
                        board.sketch(str(event.unicode))  # sketches this number, converts to unicode then to string
                    if event.key == pygame.K_RETURN:
                        board.place_number()
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                    board.draw()

                continue

        pygame.display.update()
        # to implement


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sudoku', os.path.join('assets', 'logo.png'))  # set app title
    screen = pygame.display.set_mode((500, 650))  # set app dimensions
    main()  # runs main loop
