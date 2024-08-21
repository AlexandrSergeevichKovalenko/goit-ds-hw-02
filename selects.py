#it is not a part of a home task. I just tried to commit some queries using Python(there is a separate file attached with SQL commands according to the home task description.)
import sqlite3

def execute_query(sql):
    with sqlite3.connect("my_home_task.db") as con:
        cur = con.cursor()
        cur.execute(sql)
    return cur.fetchall()

sql_1 = """SELECT u.id as user_personal_id, u.fullname, t.title FROM users as u LEFT JOIN tasks as t ON u.id = t.user_id ORDER BY u.id;"""
sql_2 = """SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = "new");"""

print(execute_query(sql_1))
print(execute_query(sql_2))
