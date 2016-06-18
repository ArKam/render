import curses

def default(self):
    copyrights_win = curses.newwin(10, 10, 8, 8)
    copyrights_win.border(0)
    copyrights_win.addstr(3, 3, "This is a copyrights statement.")
    copyrights_win.refresh()
