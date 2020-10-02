import datetime
from tkinter import *


class Task:
    def __init__(self, title=None, description=None, deadline="9999-12-31 20:00:00", sql=None, var="daily", *args):
        self.type = var
        if var == "onetime":
            if sql is None:
                self.title = title
                self.created = "NULL"  # datetime.datetime.now()
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
        print(datetime.datetime.now())
        print(self.deadline)
        show = ""
        if self.status == "incomplete":
            if str(self.deadline)[0:10] == str(datetime.datetime.now())[0:10]:
                print("TRUE: deadline == datetime.now")
                return f"Task is incomplete, due by {self.format_time(str(self.deadline)[-8:-1])}"
            return f"Task is incomplete, due by {self.deadline}"
        # elif self.status == "":
        else:
            return self.status
        # banner end

        # mainframe end

    def format_time(self, n):
        if int(int(n[0:2]) < 12):
            return f"{str(n[0:2])}:{str(n[4:5])} AM"
        else:
            return f"{str(n[0:2])}:{str(n[4:5])} PM"

