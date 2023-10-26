from graphics import Line, Point
class Cell:
    def __init__(self, p1, p2, win = None ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.p1 = p1
        self.p2 = p2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is None:
            return
       
        color1 = "black" if self.has_top_wall else "white"
        line = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
        self._win.draw_line(line, color1)
        
        color2 = "black" if self.has_right_wall else "white"
        line = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x , self.p2.y))
        self._win.draw_line(line, color2)
        
        color3 = "black" if self.has_bottom_wall else "white"
        line = Line(Point(self.p2.x , self.p2.y), Point(self.p1.x, self.p2.y))
        self._win.draw_line(line, color3)
       
        color4 = "black" if self.has_left_wall else "white"
        line = Line(Point(self.p1.x, self.p2.y), Point(self.p1.x, self.p1.y))
        self._win.draw_line(line, color4)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        start_x = self.p1.x + ((self.p2.x - self.p1.x) / 2)
        start_y = self.p1.y - ((self.p1.y - self.p2.y) / 2) 
        end_x = to_cell.p1.x + ((to_cell.p2.x - to_cell.p1.x) / 2)
        end_y = to_cell.p1.y - ((to_cell.p1.y - to_cell.p2.y) / 2)

        color = "gray" if undo else "red"
        
        line = Line(Point(start_x, start_y), Point(end_x, start_y))
        self._win.draw_line(line, color)
        line = Line(Point(end_x, start_y), Point(end_x, end_y))
        self._win.draw_line(line, color)

 

