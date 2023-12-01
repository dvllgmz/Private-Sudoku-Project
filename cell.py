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

    def draw(self):
        screen.