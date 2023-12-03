import pygame
from const import *


class Cell:
    def __init__(self, value, row, col, screen, is_given=False):
        self.value = str(value)
        self.row = row
        self.col = col
        self.screen = screen
        self.is_sketched = False
        self.sketched_value = None
        self.is_sketch = False
        self.is_given = is_given

    def set_cell_value(self, value):  # setter for this cell value
        self.value = str(value)  # converts to string, useful to display if it's an int
        self.is_sketch = False

    def set_sketched_value(self, value):
        self.value = str(value)  # converts to string, useful to display if it is an int
        self.is_sketch = True

    '''this function draws the box outline as well as the value of the cell'''
    def draw(self, is_selected=False):

        '''Define values based on if it's a sketch and/or if it's selected'''
        cell_color = REGULAR_LINE_COLOR if not is_selected else SELECTED_LINE_COLOR  # different colors if it's selected
        cell_width = 2 if not is_selected else 4  # different width if it's selected
        cell_coords = (self.row * 50) + 25, (self.col * 50) + 25  # get coordinates of cell
        cell_value = str(self.value)
        value_color = GIVEN_NUMBER_COLOR if self.is_given else USER_NUMBER_COLOR
        cell_box = pygame.Rect(cell_coords[0], cell_coords[1], 50, 50)  # create rectangle outline
        pygame.draw.rect(self.screen, cell_color, cell_box, width=cell_width)  # draws rectangle outline

        if cell_value == '0':  # don't print if the cell value is 0, only outline
            return False

        if self.is_sketch:
            cell_font = pygame.font.Font(None, 25)  # define 25 size font for sketch
            cell_rendered = cell_font.render(cell_value, 0, value_color)  # renders number
            self.screen.blit(cell_rendered, cell_rendered.get_rect(topleft=(cell_coords[0] + 5, cell_coords[1] + 5)))  # display, 5 and 5 to offset to make it top left
        else:
            cell_font = pygame.font.Font(None, 75)  # define 75 size font for number
            cell_rendered = cell_font.render(cell_value, 0, value_color)  # renders number
            self.screen.blit(cell_rendered, cell_rendered.get_rect(center=(cell_coords[0] + 25, cell_coords[1] + 28)))  # display, 25 and 28 to offset to make centered
        return True

    def __str__(self):
        return self.value
