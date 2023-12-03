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

                # fonts
                main_menu_font = pygame.font.Font('freesansbold.ttf', 50)
                button_font = pygame.font.Font('freesansbold.ttf', 30)

                # background
                screen.fill(BACKGROUND_COLOR)

                # title
                title_text = main_menu_font.render('Sudoku', 1, BOLD_LINE_COLOR)
                title_rect = title_text.get_rect(center=(250, 150))
                screen.blit(title_text, title_rect)

                #buttons
                medium_button = button_font.render('Medium', 1, COLOR_WHITE)
                medium_button.get_rect(center=(250, 350))
                medium_surface = pygame.Surface((medium_button.get_size()[0] + 40, medium_button.get_size()[1] + 40))
                medium_surface.fill(REGULAR_LINE_COLOR)
                medium_surface.blit(medium_button, (20, 20))
                # use this line to control text location
                medium_rectangle = medium_surface.get_rect(center=(250, 350))

                easy_button = button_font.render('Easy', 1, COLOR_WHITE)
                easy_button.get_rect(center=(250, 250))
                easy_surface = pygame.Surface((medium_button.get_size()[0] + 40, medium_button.get_size()[1] + 40))
                easy_surface.fill(BOLD_LINE_COLOR)
                easy_surface.blit(easy_button, (42, 20))
                # use this line to control text location
                easy_rectangle = easy_surface.get_rect(center=(250, 250))


                hard_button = button_font.render('Hard', 1, COLOR_WHITE)
                hard_button.get_rect(center=(250, 450))
                hard_surface = pygame.Surface((medium_button.get_size()[0] + 40, medium_button.get_size()[1] + 40))
                hard_surface.fill(COLOR_RED)
                hard_surface.blit(hard_button, (40, 20))
                # use this line to control text location
                hard_rectangle = hard_surface.get_rect(center=(250, 450))


                quit_button = button_font.render('Quit', 1, COLOR_WHITE)
                quit_button.get_rect(center=(250, 550))
                quit_surface = pygame.Surface((medium_button.get_size()[0] + 40, medium_button.get_size()[1] + 40))
                quit_surface.fill(COLOR_RED)
                quit_surface.blit(quit_button, (42, 20))
                # use this line to control text location
                quit_rectangle = quit_surface.get_rect(center=(250, 550))

                screen.blit(easy_surface, easy_rectangle)
                screen.blit(medium_surface, medium_rectangle)
                screen.blit(hard_surface, hard_rectangle)
                screen.blit(quit_surface, quit_rectangle)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rectangle.collidepoint(event.pos):
                        board = Board(9, 9, screen, 'easy')
                        board.draw()
                        current_screen = 'game'
                    elif medium_rectangle.collidepoint(event.pos):
                        board = Board(9, 9, screen, 'medium')
                        board.draw()
                        current_screen = 'game'
                    elif hard_rectangle.collidepoint(event.pos):
                        board = Board(9, 9, screen, 'hard')
                        board.draw()
                        current_screen = 'game'
                    elif quit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            if current_screen == 'game':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell = board.click(event.pos[0], event.pos[1])
                    if cell is not None:
                        board.select(cell[0], cell[1])  # selects the box based on coords if it exists
                    board.draw()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if board.select()[0] != 0:  # checks if cell is within bounds
                            board.select(board.select()[1], board.select()[0]-1)
                        else:
                            board.select(board.select()[1], 8)
                    if event.key == pygame.K_DOWN:
                        if board.select()[0] != 8:
                            board.select(board.select()[1], board.select()[0]+1)
                        else:
                            board.select(board.select()[1], 0)
                    if event.key == pygame.K_LEFT:
                        if board.select()[1] != 0:  # checks if cell is within bounds
                            board.select(board.select()[1]-1, board.select()[0])
                        else:
                            board.select(8, board.select()[0])
                    if event.key == pygame.K_RIGHT:
                        if board.select()[1] != 8:
                            board.select(board.select()[1]+1, board.select()[0])
                        else:
                            board.select(0, board.select()[0])
                    if event.unicode.isdigit():  # if user presses a number (converts event to unicode which gives key)
                        board.sketch(str(event.unicode))  # sketches this number, converts to unicode then to string
                    if event.key == pygame.K_RETURN:
                        board.place_number()
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    board.draw()

                continue

        pygame.display.update()
        # to implement


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sudoku', os.path.join('assets', 'logo.png'))  # set app title
    screen = pygame.display.set_mode((500, 650))  # set app dimensions
    main()  # runs main loop
