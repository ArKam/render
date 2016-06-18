def info(self):
    term_size_info = self.screen.getmaxyx()

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        term_color_depth = curses.COLORS
    else:
        term_color_depth = None

    subwin = curses.newwin(10, 10, 8, 8)
    subwin.border(0)
    subwin.addstr(3, 3, "- Terminal size: "+"W="+str(term_size_info[0])+" H="+str(term_size_info[1]))
    subwin.refresh()
