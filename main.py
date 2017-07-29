from maze.Maze import Maze
from view.textview import TextView

def main():
    m = Maze(10,10)
    view = TextView()
    view.show(m)

if __name__ == '__main__':
    main()