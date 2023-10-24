from graphics import Window, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win, Point(100, 100), Point(150, 50))
    c1.draw()
    c2 = Cell(win, Point(300, 300), Point(350, 250))
    c2.draw()
    c3 = Cell(win, Point(500, 100), Point(550, 50))
    c3.draw()


    c1.draw_move(c2)
    c2.draw_move(c3)

    win.wait_for_close()

main()
