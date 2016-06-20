#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys
import curses

class Render(object):
    """ Class responsible to render views """
    def __init__(self, appName=" Default Application Name "):
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(0, 2, appName)

    def add_panel(self, **kwargs):
        self.view = []
        if not kwargs:
            try:
                module = __import__("panels.{0}.{1}".format(panel, view))
            except ImportError:
                raise
            self.view.append(module)
            return self.view
        else:
            for keys, values in kwargs.iteritems():
                try:
                    self.view.append(__import__("panels.{0}.{1}".format(keys, values)))
                except ImportError:
                    raise
            return self.view

    def compose(self):
        pass

    def save_view(self):
        pass

    def restore_view(self):
        pass

if __name__ == '__main__':
    """ Simple example of main windows rendering with a named subwindow. """
    while 1:
        app = Render(" GENERIC WIZARD ")
        app.add_panel() # Call the terminal view from the infos panel package.
