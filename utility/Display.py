from tkinter import *
from classes import Task


def daily_card(base, task):
    mainframe = Frame(base)
    mainframe.pack()

    title = Label(mainframe, text=task.title)
    subtitle = Label(mainframe, text=f"{task.status}, due by {format_time(task.deadline[10, -1])}" if(task.status == "incomplete") else task.status)
    description = Label(mainframe, text=task.description)

    button_done = Button(mainframe, text="Done")
    button_failed = Button(mainframe, text="Incompleted")


def format_time(n):
    if int(n[0, 2] < 12):
        return f"{n[0, 2]}:{n[4, 5]} AM"
    else:
        return f"{n[0, 2] - 12}:{n[4, 5]} PM"
