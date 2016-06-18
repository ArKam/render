#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys
import curses

class Render(object):
    """ Class responsible to render views """
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(0, 2, " GENERIC WIZARD ")

    def panel(self, category=None):
        target = category
        __default_panel = "copyrights"
        try:
            if target is not None:
                panel, view = target.split(".")
                __import__("panels.{0}.{1}".format(panel, view))
                # self.screen.addstr(4, 2, "Panel called: "+panel)
                # self.screen.addstr(5, 2, "View called: "+view)
                # self.screen.addstr(6, 2, "Category is: "+"{0}-{1}".format(panel, view))
            else:
                __import__("panels.%s" % __default_panel)
        except ImportError:
            raise

if __name__ == '__main__':
    render = Render()
    render.panel('infos.terminal') # Call the terminal view from the infos panel package.
    # render.panel() Call the copyrights view by default
