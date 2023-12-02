from cell import Cell
from const import *
import pygame  #FIXME: import and implement sudoku_generator once it's done


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
        self.current_selected_value = None

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        for row in self.board:  # draws the game board
            for cell in row:
                cell.draw()
        for row in self.user_board:  # draws the user board over the game board
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
            self.current_selected = self.user_board[row][col]  # else, update it to the values passed in
        return self.current_selected_pos  # returns the location of the currently selected cell

    def click(self, x, y):
        if 25 <= x <= 475 and 25 <= y <= 475:  # if the click is in the range of the board
            return (x-25)//50, (y-25)//50  # divides coordinates // 50 to get number of column, subtracts margin
        else:
            return None  # if not in range of board

    def clear(self):
        self.current_selected.set_cell_value(0)

    def sketch(self, value):
        position = self.current_selected_pos
        if str(self.board[position[0]][position[1]]) == '0': # checks if value doesn't already exist in the game board
            position = self.current_selected_pos  # gets the position of the selected cell
            self.user_board[position[0]][position[1]].set_sketched_value(value)  # sets sketched value to cell in user board

    def place_number(self, value=None):
        position = self.current_selected_pos
        if value is None:
            value = str(self.current_selected)  # gets value
        self.user_board[position[0]][position[1]].set_cell_value(value)
    def reset_to_original(self): # Reset all cells in the board to their original values (0 if cleared, otherwise original)
        for row in range(9):
            for col in range(9):
                self.user_board[row][col].set_cell_value(self.board[row][col].get_cell_value())
                # Iterates through clearing what isn't original
    def is_full(self): # Returns a Boolean value indicating whether the board is full or not
        for row in range(9):
            for col in range(9):
                if self.user_board[row][col].get_cell_value() == '0':
                    return False
        return True

    def update_board(self): # Updates the underlying 2D board with values in all cells
        for row in range(9):
            for col in range(9): # Iterates through the board
                self.board[row][col].set_cell_value(self.user_board[row][col].get_cell_value())
                # user_board -> board (2D)
    def find_empty(self): # Finds an empty cell and returns its row and col as a tuple (x,y)
        for row in range(9):
            for col in range(9): # Iterates through the board
                if self.board[row][col].get_cell_value() == '0': # checks if its empty
                    return row, col
                    # Returns it as a tuple
        return None # prevents logic error
    def check_board(self): # Check whether the Sudoko board is solved correctly
        for row in range(9): # checks each row
            if len(set(self.board[row])) != 9: # Checks each row for duplicates, because its a set
                return False # Incorrect
        for col in range(9): # checks each column
            if len(set(self.board[i][col] for i in range(9))) != 9: # Checks each column for duplicates, because its a set
                return False # Incorrect
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3): # 0, 3, 6 are the starting index for the rows of boxes
                if len(set(self.board[i][j] for i in range(box_row, box_row + 3) for j in
                           range(box_col, box_col + 3))) != 9:
                    '''okay, so, it basically checks each box. I iterate through each row top to bottom
                    adding the numbers to the set, then it checks the length of the set because if there was a
                    duplicate it wouldn't be 9'''
                    return False
        return True # need to add the win screen in the main or sudoko
