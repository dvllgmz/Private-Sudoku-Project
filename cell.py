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
        self.value = str(value)  # converts to string, useful to display if it's an int
        self.value_is_sketched = False  # stores if the value is sketched or drawn

    def set_sketched_value(self, value):
        self.value = str(value)  # converts to string, useful to display if it is an int
        self.value_is_sketched = True  # stores if the value is sketched or drawn

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
    def draw(self, is_sketch=False, is_selected=False):
        cell_color = REGULAR_LINE_COLOR if not is_selected else SELECTED_LINE_COLOR
        cell_width = 2 if not is_selected else 4

        cell_coords = self._get_coordinates(self.row, self.col)  # gets coordinates where number will go
        cell_box = pygame.Rect(cell_coords[0], cell_coords[1], 50, 50)  # create rectangle outline
        pygame.draw.rect(self.screen, cell_color, cell_box, width=cell_width)  # draws rectangle outline
        if self.value == '0':  # don't print if the cell value is 0, only outline
            return False
        cell_font = pygame.font.Font(None, 75)  # define font for number
        cell_rendered = cell_font.render(self.value, 0, GIVEN_NUMBER_COLOR)  # renders number
        self.screen.blit(cell_rendered, cell_rendered.get_rect(center=(cell_coords[0]+25, cell_coords[1]+28)))  #display
        return True
