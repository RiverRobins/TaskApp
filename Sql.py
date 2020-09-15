import mysql.connector
import random
import Creds

db = mysql.connector.connect(host="localhost", user=Creds.mySql_user, passwd=Creds.mySql_password, database="tasks")
cur = db.cursor()

def init():
    cur.execute("CREATE DATABASE IF NOT EXISTS tasks")
    cur.execute("CREATE TABLE IF NOT EXISTS daily("
                "id BIGINT UNSIGNED AUTO_INCREMENT;"
                "title VARCHAR(255),"
                "status ENUM('incomplete', 'completed', 'missed') DEFAULT 'incomplete',"
                "description TEXT,"
                ")")
    cur.execute("CREATE TABLE IF NOT EXISTS onetime("
                "id BIGINT UNSIGNED AUTO_INCREMENT;"
                "title VARCHAR(255),"
                "created DATE,"
                "status ENUM('incomplete', 'completed', 'missed') DEFAULT 'incomplete',"
                "description TEXT,"
                "deadline DATE default NULL"
                ")")
    # cur.execute("CREATE TABLE IF NOT EXISTS dependencies("
    #             ")")


def seed(clear="None", *args):
    if clear == "All":
        cur.execute("TRUNCATE TABLE daily")
        cur.execute("TRUNCATE TABLE onetime")
        # cur.execute("TRUNCATE TABLE dependencies")
    elif clear != "None":
        cur.execute(f"TRUNCATE TABLE {clear}")

    if args is None:
        seed("daily")
        seed("onetime")
        seed("dependencies")
    else:
        if "daily" in args:
            for num in range(5, random.randint(5, 20)):
                cur.execute(f"INSERT INTO daily(title, status, description) VALUES ({make(0)}, incomplete, {make(1)})")

def make(output):
    if output == 0:
        titles = ["Trash", "Recycling", "Dishes", "Feed Animals", "Clean Room", "Do Thing", "Homework", "Do Drugs", "Get Groceries", "Get Drugs", "Work Out", "Eat"]
        return titles[random.randint(0, len(titles) - 1)]
    elif output == 1:
        descriptions = ["because of", "do", "this", "or not", "creative phrase", "you need to", "or else", "because", "your responsible for", "your responsibility is", "its fun"]
        temp = ""
        for i in range(0, random.randint(2, 20)):
            temp += descriptions[random.randint(0, len(descriptions) - 1)]
