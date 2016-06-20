import curses
import sys

def display(copyright="declaration.md"):
    copyright_win = curses.newwin(4, 2, 10, 10)
    copyright_win.border(0)
    try:
        with open(copyright) as declaration:
            for lines in declaration:
                copyright_win.addstr(3, 3, lines)
                copyright_win.refresh()
    except OSError:
        raise

def action(self):
    pass

if __name__ == '__main__':
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    screen.refresh()
    display("testing.md")
    curses.endwin()
