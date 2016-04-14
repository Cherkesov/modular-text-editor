__author__ = 'GoForBroke'

from abc import ABCMeta, abstractmethod
from tkinter import *


class AbstractModule(object):
    __metaclass__ = ABCMeta

    def __init__(self, text_area=None):
        self.text_area = text_area
        pass

    name = None
    sort = 0

    def do_action_wrap(self):
        cursor_pos = 0

        try:
            cursor_pos = self.text_area.index(INSERT)
        except TclError:
            pass

        selected_text = None
        selection_start = 0.0
        selection_end = 0.0

        try:
            selected_text = self.text_area.selection_get()
            selection_start = self.text_area.index(SEL_FIRST)
            selection_end = self.text_area.index(SEL_LAST)
        except TclError:
            pass

        self.do_action(self.text_area, cursor_pos, selected_text, selection_start, selection_end)
        pass

    @abstractmethod
    def do_action(self, text_area, cursor_pos, selected_text, selection_start, selection_end):
        """
        :return:
        """
        pass
