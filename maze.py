from graphics import Point
from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y= cell_size_y
        self._cells = []
        self.win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()    
        self._break_walls_r(0, 0)
        self._draw_cell()
        self._reset_cells_visted()
        self.way = []

    def _create_cells(self):
        self._cells = []   
        for i in range(self.num_cols):
            row = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1+ j * self.cell_size_y

                p1 = Point(x1, y1)
                p2 = Point(x1 + self.cell_size_x, y1 + self.cell_size_y)
                row.append(Cell(p1, p2, self.win))
            self._cells.append(row)
        self._break_entrance_and_exit()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols -1][self.num_rows -1].has_bottom_wall = False


    def _draw_cell(self):
        if self.win is None:
            return 
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].draw()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def solve(self):
        return self._solve_r(0, 0)
            

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if (i > 0 
            and not self._cells[i - 1][j].visited 
            and not self._cells[i][j].has_left_wall):
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        if (i < self.num_cols - 1 
            and not self._cells[i + 1][j].visited 
            and not self._cells[i][j].has_right_wall):
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (j > 0 
            and not self._cells[i][j - 1].visited 
            and not self._cells[i][j].has_top_wall):
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if (j < self.num_rows - 1 
            and not self._cells[i][j + 1].visited 
            and not self._cells[i][j].has_bottom_wall): 
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                  return True
                else:
                 self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []

            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited: 
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._cells[i][j].draw()
                return
            
            index = random.randrange(len(possible_directions))
            next_cell = possible_directions[index]

            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_cell[0], next_cell[1]) 
            
    def _reset_cells_visted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False





            


        

