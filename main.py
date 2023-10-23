from graphics import Window, Line, Point

def main():
    win = Window(800, 600)

    line = Line(Point(0, 0), Point(0,50))
    line = Line(Point(0, 50), Point(50,50))
    line = Line(Point(50, 50), Point(50,0))
    line = Line(Point(50, 0), Point(0,0))



    win.draw_line(line, "black")
    win.wait_for_close()

main()
