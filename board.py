from cell import Cell
from const import *
import sudoku_generator, pygame


class Board:
    removed_cells = {'easy': 30, 'medium': 40, 'hard': 50}

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        #self.board = sudoku_generator.generate_sudoku(9, Board.removed_cells[difficulty])
        self.current_selected = None


    def draw(self):
        for row in self.board:
            for cell in self.board:
                cell.draw()

        for i in range(4):  # draws wider lines every 3, to separate the 9 subsections
            pygame.draw.line(
                self.screen,
                BOLD_LINE_COLOR,
                (25, 25 + (i * 150)),
                (500 - 25, 25 + (i * 150)),
                width=5
            )
            pygame.draw.line(
                self.screen,
                BOLD_LINE_COLOR,
                (25 + (i * 150), 25),
                (25 + (i * 150), 500 - 25),
                width=5
            )

    def select(self, row, col):
        self.current_selected = self.board[col][row]  # set to index, convert 2d to 1d

    def click(self, x, y):
        if 25 <= x <= 475 and 25 <= y <= 475:
            return tuple((x-25)//50, (y-25)//50)
        else:
            return None

    def clear(self):
        for cell in self.board:
            cell.set_cell_value('0')

    def sketch(self, value):
        pass
