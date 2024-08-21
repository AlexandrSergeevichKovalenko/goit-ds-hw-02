import faker

from random import randint, choice, sample

import sqlite3

NUMBER_OF_USERS = 5
NUMBER_OF_TASKS = 15
STATUSES_NAMES = ['new','in progress','completed']
TASK_TITLE_COMPONENTS = ["Complete", "Do", "Execute", "Start"]

def generate_fake_data(num_users, num_tasks):
    fake_fullname = list()
    fake_tasks_title = list()
    fake_emails = list()
    fake_descr = list()

    fake_data = faker.Faker()
    for _ in range(num_users):
        fake_fullname.append(fake_data.name())
    
    for _ in range(num_tasks):
        fake_tasks_title.append(f"{choice(TASK_TITLE_COMPONENTS)} {fake_data.bs()} tasks")
    
    for _ in range(num_users):
        fake_emails.append(fake_data.email())
    
    for _ in range(num_tasks):
        fake_descr.append(fake_data.text())

    return fake_fullname, fake_tasks_title, fake_emails, fake_descr

def prepare_data(names, titles, emails, descriptions):
    unique_emails = sample(emails, len(names))
    
    for_users = []
    for i, name in enumerate(names):
        for_users.append((name, unique_emails[i]))

    for_tasks = []
    unique_description = sample(descriptions, len(titles))
    for i, title in enumerate(titles):
        for_tasks.append((title, unique_description[i], randint(1, len(STATUSES_NAMES)), randint(1, NUMBER_OF_USERS)))

    for_status = []
    uniq_status_name = sample(STATUSES_NAMES, len(STATUSES_NAMES))
    for status in uniq_status_name:
        for_status.append((status,))
        

    return for_users, for_tasks, for_status

def insert_data_to_db(users, tasks, statuses):

    with sqlite3.connect("my_home_task.db") as con:
        cur = con.cursor()
        
        sql_to_users = """ INSERT INTO users (fullname, email) VALUES(?,?);"""
        cur.executemany(sql_to_users, users)

        sql_to_tasks = """ INSERT INTO tasks (title, description, status_id, user_id) VALUES(?,?,?,?);"""
        cur.executemany(sql_to_tasks, tasks)

        sql_to_status = """ INSERT INTO status (name) VALUES(?);"""
        cur.executemany(sql_to_status, statuses)

        con.commit()

if __name__ == "__main__":
    users, tasks, statuses = prepare_data(*generate_fake_data(NUMBER_OF_USERS, NUMBER_OF_TASKS))
    insert_data_to_db(users, tasks, statuses)




        














    




