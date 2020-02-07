import os
import sqlite3 as sql

ROOT = os.path.dirname(os.path.relpath(__file__))

def create_post(name, post):
    connection = sql.connect(os.path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('INSERT INTO POSTS (USERNAME, CONTENT) VALUES (?, ?);', (name, post))
    connection.commit()
    connection.close()

def get_posts():
    connection = sql.connect(os.path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM POSTS;')
    posts = cursor.fetchall()
    return posts[::-1]

def add_task(task):
    connection = sql.connect(os.path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('INSERT INTO TODO (TASK) VALUES (?);', (task,))
    connection.commit()
    connection.close()

def alter_task(id, task=None):
    connection = sql.connect(os.path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    if task:
        cursor.execute("UPDATE TODO SET TASK = ? WHERE ID = ?;", (task, id))
    else:
        cursor.execute('DELETE FROM TODO WHERE ID = {};'.format(id))
    connection.commit()
    connection.close()

def get_tasks(id=None):
    connection = sql.connect(os.path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    if id is None:
        cursor.execute('SELECT * FROM TODO;')
    else:
        cursor.execute('SELECT * FROM TODO WHERE ID = {};'.format(id))
    tasks = cursor.fetchall()
    return tasks


