# -*- coding: utf-8 -*-
"""
import psycopg2

# коннект к бд
conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='2209vvd!'
)

# открытие курсора
cur = conn.cursor()

# запрос к бд
cur.execute("INSERT INTO user_account VALUES (%s, %s)", (3, 'Jon'))
cur.execute("SELECT * FROM user_account")

rows = cur.fetchall()
for row in rows:
    print(row)

# закрытие курсора и изменения базы данных
cur.close()
conn.close()
"""