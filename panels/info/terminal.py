import curses

def info(self):
    term_size_info = self.screen.getmaxyx()

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        term_color_depth = curses.COLORS
    else:
        term_color_depth = None

    term_win = curses.newwin(10, 10, 8, 8)
    term_win.border(0)
    term_win.addstr(3, 3, "- Terminal size: "+"W="+str(term_size_info[0])+" H="+str(term_size_info[1]))
    term_win.refresh()
