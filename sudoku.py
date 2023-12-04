import sys
import pygame, os
from const import *  # imports constants from const.py
from board import Board


def main():
    # fonts
    main_menu_font = pygame.font.Font('freesansbold.ttf', 50)
    button_font = pygame.font.Font('freesansbold.ttf', 30)
    small_button_font = pygame.font.Font('freesansbold.ttf', 22)

    # background
    screen.fill(BACKGROUND_COLOR)

    # title
    title_text = main_menu_font.render('Sudoku', 1, BOLD_LINE_COLOR)
    title_rect = title_text.get_rect(center=(250, 150))

    # buttons
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
    hard_surface.fill(COLOR_ORANGE)
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

    win_text = main_menu_font.render('YOU WIN!', 1, BOLD_LINE_COLOR)
    win_rect = win_text.get_rect(center=(250, 150))

    quit_button_win = button_font.render('Quit', 1, COLOR_WHITE)
    quit_button_win.get_rect(center=(250, 350))
    quit_surface_win = pygame.Surface((medium_button.get_size()[0] + 40, medium_button.get_size()[1] + 40))
    quit_surface_win.fill(COLOR_RED)
    quit_surface_win.blit(quit_button_win, (42, 20))
    # use this line to control text location
    quit_rectangle_win = quit_surface_win.get_rect(center=(250, 550))

    lose_text = main_menu_font.render('Game over =(', 1, BOLD_LINE_COLOR)
    lose_rect = lose_text.get_rect(center=(250, 150))

    restart_lose_button = button_font.render('Restart', 1, COLOR_WHITE)
    restart_lose_button.get_rect(center=(125, 350))
    restart_lose_surface = pygame.Surface((medium_button.get_size()[0] + 40, medium_button.get_size()[1] + 40))
    restart_lose_surface.fill(COLOR_RED)
    restart_lose_surface.blit(restart_lose_button, (23, 20))
    restart_rectangle = restart_lose_surface.get_rect(center=(250, 350))

    reset_button = small_button_font.render('Reset', 1, COLOR_WHITE)
    reset_button_text_rect = reset_button.get_rect(center=(100, 550))
    reset_surface = pygame.Surface((reset_button.get_size()[0] + 40, reset_button.get_size()[1] + 40))
    reset_surface.fill(COLOR_RED)
    reset_surface.blit(reset_button, (20, 20))
    # use this line to control text location
    reset_rectangle = reset_surface.get_rect(center=(100, 550))
    reset_rectangle.topleft = reset_button_text_rect.topleft

    restart_game_button = small_button_font.render('Restart', 1, COLOR_WHITE)
    restart_game_button_text = restart_game_button.get_rect(center=(240, 550))
    restart_game_surface = pygame.Surface((reset_button.get_size()[0] + 40, reset_button.get_size()[1] + 40))
    restart_game_surface.fill(COLOR_RED)
    restart_game_surface.blit(restart_game_button, (12, 20))
    # use this line to control text location
    restart_game_rectangle = restart_game_surface.get_rect(center=(240, 550))
    restart_game_rectangle.topleft = restart_game_button_text.topleft

    exit_game_button = small_button_font.render('Exit', 1, COLOR_WHITE)
    exit_game_button_text = exit_game_button.get_rect(center=(350, 550))
    exit_game_surface = pygame.Surface((reset_button.get_size()[0] + 40, reset_button.get_size()[1] + 40))
    exit_game_surface.fill(COLOR_RED)
    exit_game_surface.blit(exit_game_button, (27, 20))
    # use this line to control text location
    exit_game_rectangle = restart_game_surface.get_rect(center=(350, 550))
    exit_game_rectangle.topleft = exit_game_button_text.topleft

    current_screen = 'main_menu'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_screen == 'main_menu':
                screen.blit(title_text, title_rect)
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
                screen.blit(reset_surface, reset_rectangle)
                screen.blit(restart_game_surface, restart_game_rectangle)
                screen.blit(exit_game_surface, exit_game_rectangle)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell = board.click(event.pos[0], event.pos[1])
                    if reset_rectangle.collidepoint(event.pos):
                        board.reset_to_original()
                    elif restart_game_rectangle.collidepoint(event.pos):
                        screen.fill(BACKGROUND_COLOR)
                        current_screen = 'main_menu'
                        continue
                    elif exit_game_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                    if cell is not None:
                        board.select(cell[0], cell[1])  # selects the box based on coords if it exists
                    board.draw()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if board.select()[0] != 0:  # checks if cell is within bounds
                            board.select(board.select()[1], board.select()[0] - 1)
                        else:
                            board.select(board.select()[1], 8)
                    if event.key == pygame.K_DOWN:
                        if board.select()[0] != 8:
                            board.select(board.select()[1], board.select()[0] + 1)
                        else:
                            board.select(board.select()[1], 0)
                    if event.key == pygame.K_LEFT:
                        if board.select()[1] != 0:  # checks if cell is within bounds
                            board.select(board.select()[1] - 1, board.select()[0])
                        else:
                            board.select(8, board.select()[0])
                    if event.key == pygame.K_RIGHT:
                        if board.select()[1] != 8:
                            board.select(board.select()[1] + 1, board.select()[0])
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
                    screen.fill(BACKGROUND_COLOR)
                    board.draw()

            if current_screen == 'win':
                screen.blit(quit_surface_win, quit_rectangle_win)
                screen.blit(win_text, win_rect)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            if current_screen == 'lose':
                screen.blit(lose_text, lose_rect)
                screen.blit(restart_lose_surface, restart_rectangle)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rectangle.collidepoint(event.pos):
                        board = Board(9, 9, screen, 'easy')
                        board.draw()
                        current_screen = 'game'

        pygame.display.update()
        # to implement


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sudoku', os.path.join('assets', 'logo.png'))  # set app title
    screen = pygame.display.set_mode((500, 650))  # set app dimensions
    main()  # runs main loop

