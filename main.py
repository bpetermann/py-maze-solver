from graphics import Window, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    m = Maze(200, 200, 3, 2, 50, 50, win)
    win.wait_for_close()

main()
