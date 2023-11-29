import pygame, os
from const import *  # imports constants from const.py

selected_cell = []  # stores the selected cell
board = []  # stores the board


'''
this calculates a grid with the grid location. If it's not a sketch, returns middle coords of box, else,
returns the top left coordinates of the box. Returns coordinates of the grid as a tuple
'''

def get_coordinates(horizontal, vertical, is_sketch):
    grid = []
    sketch_constant = 0 if is_sketch else 25  # whether it will find the midpoint of the box (box+half), or top left corner (box)
    for vert in range(9):  # iterates through columns
        cur = []  # temporary list, will get appended to grid to do a 2D list
        for horiz in range(9):  # iterates through rows
            cur.append([25+(vert*50)+sketch_constant, 25+(horiz*50)+sketch_constant])  # appends x and y coords to grid
        grid.append(cur)

    grid[vertical][horizontal][0] += 5 if is_sketch else 0  # horizontal adjustment for sketches only

    return tuple(grid[vertical][horizontal])  # returns the coordinate of the given box as a tuple

'''
main game function, draws the grid lines, the board, and the background.
'''
def game_screen():
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

def print_number(number, horizontal, vertical, is_sketch=False, given=False):  # writes number in ui taking in the position
    number_size = 20 if is_sketch else 50  # variable set to font size
    number_color = GIVEN_NUMBER_COLOR if given else USER_NUMBER_COLOR  # variable set to font color

    number_font = pygame.font.Font(os.path.join('assets', 'Arcon-Rounded-Regular.otf'), number_size)  # define font elem
    rendered = number_font.render(number, True, number_color)  # render the number in the board
    coordinates = get_coordinates(horizontal, vertical, is_sketch)  # gets coordinates where number will go

    number_rect = rendered.get_rect(topleft=coordinates) if is_sketch else rendered.get_rect(center=coordinates)   # renders in topleft if its a user sketch, else on middle
    screen.blit(rendered, number_rect)  # displays the number

'''
iteratively calls the print_number function with the whole board list
'''
def print_board(board):
    for vert in range(len(board)):  # for each vertical index in the 2d board:
        for horiz in range(len(board[vert])):  # for each horizontal index in each row
            if board[vert][horiz] == 0: continue  # if the board number is 0, then don't write anything and keep going
            print_number(str(board[vert][horiz]), vert, horiz, given=True)  # if not, print the number in vert, horiz.

def main():
    while True:
        pygame.event.get()
        game_screen()
        pygame.display.update()
        # to implement




if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sudoku', os.path.join('assets', 'logo.png'))  # set app title
    screen = pygame.display.set_mode((500, 650))  # set app dimensions
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    main()  # runs main loop
