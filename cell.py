import pygame
from const import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.value_is_sketched = False

    def set_cell_value(self, value):  # setter for this cell value
        self.value = value
        self.value_is_sketched = False

    def set_sketched_value(self, value):
        self.value = value
        self.value_is_sketched = True

    '''
    this calculates a grid with the grid location. If it's not a sketch, returns middle coords of box, else,
    returns the top left coordinates of the box. Returns coordinates of the grid as a tuple
    '''
    @staticmethod
    def _get_coordinates(row, column):
        grid = []
        for vert in range(9):  # iterates through columns
            cur = []  # temporary list, will get appended to grid to do a 2D list
            for horiz in range(9):  # iterates through rows
                cur.append([25 + (vert * 50), 25 + (horiz * 50)])  # appends x and y coords to grid
            grid.append(cur)
        return tuple(grid[column][row])  # returns the coordinate of the given box as a tuple

    '''this function draws the box outline as well as the value of the instance'''
    def draw(self):
        if self.value == '0':  # don't print if the cell value is 0
            return False
        cell_coords = self._get_coordinates(self.row, self.col)  # gets coordinates where number will go
        cell_box = pygame.Rect(cell_coords[0], cell_coords[1], 50, 50)  # create rectangle outline
        pygame.draw.rect(self.screen, REGULAR_LINE_COLOR, cell_box, width=2)  # draws rectangle outline
        cell_font = pygame.font.Font(None, 75)  # define font for number
        cell_rendered = cell_font.render(self.value, True, GIVEN_NUMBER_COLOR)  # renders number
        self.screen.blit(cell_rendered, cell_rendered.get_rect(center=(cell_coords[0]+25, cell_coords[1]+28)))  #display
        return True
