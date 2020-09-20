import datetime
from tkinter import *


class Task:
    def __init__(self, title=None, description=None, deadline="9999-12-31 20:00:00", sql=None, var="daily", *args):
        self.type = var
        if var == "onetime":
            if sql is None:
                self.title = title
                self.created = "NULL"  # datetime.datetime.now()
                print(datetime.datetime.now())
                self.status = "incomplete"
                self.description = description
                self.deadline = deadline
            else:
                self.id = sql[0]
                self.title = sql[1]
                self.status = sql[2]
                self.created = sql[3]
                self.description = sql[4] if sql[4] != "NULL" else None
                if sql[5] is not None or sql[5] == "NULL":
                    self.deadline = None
                else:
                    self.deadline = sql[5]
        else:
            if sql is None:
                self.title = title
                self.created = "NULL"  # datetime.datetime.now()
                print(datetime.datetime.now())
                self.status = "incomplete"
                self.description = description
                self.deadline = deadline
            else:
                self.id = sql[0]
                self.title = sql[1]
                self.status = sql[2]
                self.description = sql[3] if sql[3] != "NULL" else None
                self.deadline = sql[4]
        self.dependencies = args

    def display(self, base):
        # mainframe start
        mainframe = Frame(base)
        mainframe.pack()

        # banner start
        banner = Frame(mainframe)
        banner.pack()

    def subtitle(self):
        if self.status == "incomplete":
            return f"Task is incomplete, due by {self.deadline}"
        # elif self.status == "":
        else:
            return self.status
        # banner end

        # mainframe end

