import sys

import pygame, os
from const import *  # imports constants from const.py
from board import Board

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




def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s
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
