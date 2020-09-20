from tkinter import *
from classes import Task


def daily_card_display(base, task):
    mainframe = Frame(base)
    mainframe.pack()

    title = Label(mainframe, text=task.title)
    title.pack()
    subtitle = Label(mainframe, text=task.subtitle())
    subtitle.pack()
    description = Label(mainframe, text=task.description)
    description.pack()

    button_done = Button(mainframe, text="Done")
    button_done.pack()
    button_failed = Button(mainframe, text="Incompleted")
    button_failed.pack()


def format_time(n):
    if int(n[0, 2] < 12):
        return f"{n[0, 2]}:{n[4, 5]} AM"
    else:
        return f"{n[0, 2] - 12}:{n[4, 5]} PM"
