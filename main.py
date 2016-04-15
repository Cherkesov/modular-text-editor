__author__ = 'GoForBroke'

from tkinter import *

root = Tk(className=" Hello Duck!")
root.wm_minsize(800, 600)

def hello():
    pass


main_menu_bar = Menu(root)

text_area = Text(root, width=80, height=20, font='Arial 12', wrap=WORD)
text_area.pack()

file_menu = Menu(main_menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=hello)
file_menu.add_command(label="Save", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
main_menu_bar.add_cascade(label="File", menu=file_menu)

main_menu_bar.add_command(label="Выйти", command=root.quit)
root.config(menu=main_menu_bar)

plugins_menu = Menu(main_menu_bar, tearoff=0)
import os

for module in os.listdir(os.path.dirname(__file__) + "/modules"):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    module_name = module[:-3]
    print(module_name)
    module_ = __import__("modules." + module_name, locals(), globals(), fromlist=[module_name])
    class_ = getattr(module_, module_name)
    instance = class_(text_area=text_area)
    plugins_menu.add_command(label=instance.name, command=instance.do_action_wrap)

    instance.on_register(text_area)

# del module
main_menu_bar.add_cascade(label="Плагины", menu=plugins_menu)

root.mainloop()
