from graphics import Line, Point

class Cell:
    def __init__(self, win, p1, p2 ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.p1 = p1
        self.p2 = p2
        self._win = win

    def draw(self):
        if self.has_top_wall:
            line = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x , self.p2.y))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self.p2.x , self.p2.y), Point(self.p1.x, self.p2.y))
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(Point(self.p1.x, self.p2.y), Point(self.p1.x, self.p1.y))
            self._win.draw_line(line)