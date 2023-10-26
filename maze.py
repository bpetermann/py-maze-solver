from graphics import Point
from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y= cell_size_y
        self._cells = []
        self.win = win
        self._create_cells()    

    def _create_cells(self):
        self._cells = []   
        for i in range(self.num_cols):
            row = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1+ j * self.cell_size_y

                p1 = Point(x1, y1)
                p2 = Point(x1 + self.cell_size_x, y1 + self.cell_size_y)
                row.append(Cell(self.win, p1, p2))
            self._cells.append(row)
        self._draw_cell()

    def _draw_cell(self):
        if self.win is None:
            return 
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].draw()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


        

