from cell import Cell
from const import *
class Board(Cell):
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board =

    '''
    main game function, draws the grid lines, the board, and the background.
    '''

    def _game_screen():
        # grid lines
        screen.fill(BACKGROUND_COLOR)  # background
        for i in range(10):  # draws both horizontal and vertical lines, 10 lines in each
            pygame.draw.line(
                screen,
                REGULAR_LINE_COLOR,
                (25, 25 + (i * 50)),
                (500 - 25, 25 + (i * 50)),
                width=2
            )
            pygame.draw.line(
                screen,
                REGULAR_LINE_COLOR,
                (25 + (i * 50), 25),
                (25 + (i * 50), 500 - 25),
                width=2
            )
        for i in range(4):  # draws wider lines every 3, to separate the 9 subsections
            pygame.draw.line(
                screen,
                BOLD_LINE_COLOR,
                (25, 25 + (i * 150)),
                (500 - 25, 25 + (i * 150)),
                width=5
            )
            pygame.draw.line(
                screen,
                BOLD_LINE_COLOR,
                (25 + (i * 150), 25),
                (25 + (i * 150), 500 - 25),
                width=5
            )
            print_board(board)  # prints numbers

    '''
    this function takes in the value to print, the position, and whether it's a sketch and/or it's given by the game, then
    prints this value into the board
    '''

    def _print_number(number, horizontal, vertical, is_sketch=False,
                     given=False):  # writes number in ui taking in the position
        number_size = 20 if is_sketch else 50  # variable set to font size
        number_color = GIVEN_NUMBER_COLOR if given else USER_NUMBER_COLOR  # variable set to font color

        number_font = pygame.font.Font(os.path.join('assets', 'Arcon-Rounded-Regular.otf'),
                                       number_size)  # define font elem
        rendered = number_font.render(number, True, number_color)  # render the number in the board
        coordinates = get_coordinates(horizontal, vertical, is_sketch)  # gets coordinates where number will go

        number_rect = rendered.get_rect(topleft=coordinates) if is_sketch else rendered.get_rect(
            center=coordinates)  # renders in topleft if its a user sketch, else on middle
        screen.blit(rendered, number_rect)  # displays the number

    '''
    iteratively calls the _print_number function with the whole board list
    '''

    def _print_board(board):
        for vert in range(len(board)):  # for each vertical index in the 2d board:
            for horiz in range(len(board[vert])):  # for each horizontal index in each row
                if board[vert][
                    horiz] == 0: continue  # if the board number is 0, then don't write anything and keep going
                _print_number(str(board[vert][horiz]), vert, horiz,
                             given=True)  # if not, print the number in vert, horiz.

    def draw(self):
        
        