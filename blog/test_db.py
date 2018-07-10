# -*- coding:utf-8 -*-
import psycopg2

conn = psycopg2.connect(database='study_db', user="postgres", password="Hello@2018", host="localhost", port="5432")
cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()
