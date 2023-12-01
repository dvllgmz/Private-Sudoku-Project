from cell import Cell
from const import *
import pygame  #FIXME: broken, sudoku_generator not needed yet


class Board:
    removed_cells = {'easy': 30, 'medium': 40, 'hard': 50}

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        #self.board = sudoku_generator.generate_sudoku(9, Board.removed_cells[difficulty])
        '''TEMPORARY CODE TO TEST PROGRAM  (replaces this ^)'''
        temp = [['5', '3', '0', '0', '7', '0', '0', '0', '0'],
                ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
                ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
                ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
                ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
                ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
                ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
                ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
                ['0', '0', '0', '0', '8', '0', '0', '7', '9']]
        temp2 = []
        for col in range(len(temp)):
            tmp = []
            for row in range(len(temp[col])):
                tmp.append(Cell(temp[col][row], row, col, self.screen, is_given=True))
            temp2.append(tmp)
        self.board = temp2
        '''END TEMPORARY CODE TO TEST PROGRAM'''
        self.user_board = []  # generates user board with user inputs

        for column in range(9):
            self.user_board.append([])
            for row in range(9):
                self.user_board[column].append(Cell('0', row, column, screen))

        self.current_selected = None
        self.current_selected_pos = None

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        for row in self.board:
            for cell in row:
                cell.draw()

        for i in range(4):  # draws 4 wider lines to separate into the 9 subsections
            pygame.draw.line(  # (horizontal lines)
                self.screen,
                BOLD_LINE_COLOR,  # from const.py
                (25, 25 + (i * 150)),       # from x = 25, y = every 150
                (500 - 25, 25 + (i * 150)),  # to x = 475, y = every 150
                width=5
            )
            pygame.draw.line(  # (vertical lines)
                self.screen,
                BOLD_LINE_COLOR,  # from const.py
                (25 + (i * 150), 25),      # from x = every 150, y = 25
                (25 + (i * 150), 500 - 25),  # to x = every 150, y = 475
                width=5
            )
        if self.current_selected is not None:
            self.current_selected.draw(is_selected=True)  # shows overlay of selected cell if any is selected

    def select(self, col=None, row=None):
        if col is None and row is None:
            pass  # if function is called without args, don't modify anything
        else:
            self.current_selected_pos = [row, col]
            self.current_selected = self.board[row][col]  # else, update it to the values passed in
        return self.current_selected_pos  # returns the location of the currently selected cell

    def click(self, x, y):
        if 25 <= x <= 475 and 25 <= y <= 475:  # if the click is in the range of the board
            return (x-25)//50, (y-25)//50  # divides coordinates // 50 to get number of column, subtracts margin
        else:
            return None  # if not in range of board

    def clear(self):
        for column in self.user_board:
            for cell in column:
                cell.set_cell_value('0')

    def sketch(self, value):
        if self.current_selected.value == '0':
            self.current_selected.set_sketched_value(value)
