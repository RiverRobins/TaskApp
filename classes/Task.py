import datetime
from tkinter import *

class Task:
    def __init__(self, title=None, description=None, deadline=datetime.datetime(year=9999, month=12, day=31, hour=0, minute=0, second=0, microsecond=0), sql=None, *args):
        if(sql is None):
            self.title = title
            self.created = datetime.datetime.now()
            self.status = "incomplete"
            self.description = description
            self.deadline = deadline
        else:
            self.id = sql[0]
            self.title = sql[1]
            self.created = sql[2]
            self.status = sql[3]
            self.description = sql[4] if sql[4] != "NULL" else None
            self.deadline = sql[5] if sql[5] != "NULL" else None
        self.dependencies = args

    def display(self, base):
        #mainframe start
        mainframe = Frame(base)
        mainframe.pack()

        #banner start
        banner = Frame(mainframe)
        banner.pack()

    def subtitle(self):
        if self.status == "incomplete":
            return

        #banner end

        #mainframe end

