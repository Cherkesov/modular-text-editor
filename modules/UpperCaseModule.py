__author__ = 'GoForBroke'

from tkinter import *
from mte import classes


class UpperCaseModule(classes.AbstractModule):
    name = 'Upper case'
    sort = 0

    def on_register(self, text_area):
        text_area.tag_config("bold", foreground="blue", underline=1)
        # text_area.tag_config("bold", font="bold")
        pass

    def do_action(self, text_area, cursor_pos, selected_text, selection_start, selection_end):
        # self.text_area.insert(
        #     '1.0',
        #     'Добавить Текст\n\ в начало первой строки'
        # )

        if selection_start is not None and selection_end is not None:
            text_area.delete(selection_start, selection_end)
            text_area.insert(selection_start, selected_text.upper(), "bold")
            pass

        # try:
        #     text_area.tag_config("a", foreground="blue", underline=1)
        #     text_area.insert(INSERT, "click here!", "a")
        #
        #     print('--------------------------------')
        # except TclError:
        #     pass
        # pass
