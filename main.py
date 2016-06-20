#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys
import curses

class Render(object):
    """ Class responsible to render views """
    def __init__(self, appName=" Default Name "):
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(0, 2, appName)

    def panel(self, category=None):
        target = category
        __default_panel = "copyrights"
        try:
            if target is not None:
                panel, view = target.split(".")
                self.screen.refresh()
                self.dynamic = __import__("panels.{0}.{1}".format(panel, view))
            else:
                self.default = __import__("panels.%s" % __default_panel)
                self.default.__default_panel.__default_panel.display() # Need to be cleaned.
        except ImportError:
            raise

if __name__ == '__main__':
""" Simple example of main windows rendering with a named subwindow. """
    while 1:
        render = Render(" GENERIC WIZARD ")
        render.panel('infos.terminal') # Call the terminal view from the infos panel package.
