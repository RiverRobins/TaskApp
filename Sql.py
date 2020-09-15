import mysql.connector
import random

db = mysql.connector.connect(host="localhost", user=creds.mySql_user, passwd=creds.mySql_password, database="people")
cur = db.cursor()

def init():
    cur.execute("CREATE DATABASE IF NOT EXISTS tasks")
    cur.execute("CREATE TABLE IF NOT EXISTS daily("
                ")")
    cur.execute("CREATE TABLE IF NOT EXISTS onetime("
                "id BIGINT UNSIGNED AUTO_INCREMENT;"
                ")")
    cur.execute("CREATE TABLE IF NOT EXISTS dependencies("
                ")")


def seed(*args):
    if args is None:
        seed()
    else:
        for i in args:
            for num in range(5, random.randint(5, 20)):
                cur.execute(f"INSERT INTO {i} ")
