import sqlite3

def create_db():
    #getting access to the file with sql script, reading it
    with open("sql_script_for_database.sql", "r") as file:
        sql = file.read()
    
    #creating database and tables
    with sqlite3.connect("my_home_task.db") as con:
        cur = con.cursor()
    #running sql-script to create tables
        cur.executescript(sql)

if __name__ == "__main__":
    create_db() 