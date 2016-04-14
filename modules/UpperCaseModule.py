__author__ = 'GoForBroke'

from tkinter import *
from mte import classes


class UpperCaseModule(classes.AbstractModule):
    name = 'Upper case'
    sort = 0

    def do_action(self, text_area, cursor_pos, selected_text, selection_start, selection_end):
        # self.text_area.insert(
        #     '1.0',
        #     'Добавить Текст\n\ в начало первой строки'
        # )
        try:
            text_area.tag_config("a", foreground="blue", underline=1)
            text_area.insert(INSERT, "click here!", "a")

            print('--------------------------------')
        except TclError:
            pass
        pass
