from graphics import Window, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win, Point(225, 225), Point(250, 250))
    c.has_bottom_wall = False
    c.draw()


    win.wait_for_close()

main()
