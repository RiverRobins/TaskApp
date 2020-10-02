import mysql.connector
import random
import Creds
from classes.Task import Task

db = mysql.connector.connect(host="localhost", user=Creds.mySql_user, passwd=Creds.mySql_password, database="tasks_db")
cur = db.cursor()


def initial():
    cur.execute("CREATE DATABASE IF NOT EXISTS tasks_db")
    cur.execute("""CREATE TABLE IF NOT EXISTS daily(
                id BIGINT UNSIGNED AUTO_INCREMENT,
                title VARCHAR(255),
                status ENUM('incomplete', 'completed', 'missed') DEFAULT 'incomplete',
                description TEXT,
                deadline DATETIME,
                PRIMARY KEY (id)
                )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS onetime(
                id BIGINT UNSIGNED AUTO_INCREMENT,
                title VARCHAR(255),
                created DATE,
                status ENUM('incomplete', 'completed', 'missed') DEFAULT 'incomplete',
                description TEXT,
                deadline DATE default NULL,
                PRIMARY KEY (id)
                )""")
    # cur.execute("CREATE TABLE IF NOT EXISTS dependencies("""
    #             ")""")


def update_status(item_id, new_status, table="daily"):
    cur.execute(f"UPDATE {table} SET status = '{new_status}' WHERE id = {item_id}")


# def refresh():
#     cur.execute("SELECT * FROM daily WHERE status = 'incomplete'")
#     daily_tasks_sql = cur.fetchall()
#     cur.execute("SELECT * FROM onetime WHERE status = 'incomplete'")
#     onetime_tasks_sql = cur.fetchall()
#     daily_str = ""
#     onetime_str = ""
#     for i in daily_tasks_sql:
#         if i[4] == "":
#             cur.execute("")

def seed(clear="None", table="All"):
    if clear == "All":
        cur.execute("TRUNCATE TABLE daily")
        cur.execute("TRUNCATE TABLE onetime")
        # cur.execute("TRUNCATE TABLE dependencies")
    elif clear != "None":
        cur.execute(f"TRUNCATE TABLE {clear}")

    if table == "All":
        seed(table="daily")
        seed(table="onetime")
    elif table == "daily":
        for num in range(5, random.randint(5, 20)):
            cur.execute(f"INSERT INTO daily(title, status, description, deadline) VALUES ('{make(0)}', 'incomplete', '{make(1)}', CONCAT(CURRENT_DATE, ' 20:00:00'))")
    elif table == "onetime":
        for num in range(5, random.randint(5, 30)):
            cur.execute(f"INSERT INTO onetime(title, status, created, description, deadline) VALUES ('{make(0)}', 'incomplete', CURRENT_DATE, '{make(1)}', CONCAT(CURRENT_DATE, ' 20:00:00'))")


def make(output):
    if output == 0:
        titles = ["Trash", "Recycling", "Dishes", "Feed Animals", "Clean Room", "Do Thing", "Homework", "Do Drugs", "Get Groceries", "Get Drugs", "Work Out", "Eat"]
        return titles[random.randint(0, len(titles) - 1)]
    elif output == 1:
        descriptions = ["because of", "do", "this", "or not", "creative phrase", "you need to", "or else", "because", "your responsible for", "your responsibility is", "its fun"]
        temp = "Do "
        for i in range(0, random.randint(2, 20)):
            temp += descriptions[random.randint(0, len(descriptions) - 1)] + " "


def get_daily_tasks():
    cur.execute("SELECT * FROM daily")
    tasks = []
    for i in cur.fetchall():
        # print("From daily: " + str(i))
        tasks.append(Task(sql=i))
    return tasks
