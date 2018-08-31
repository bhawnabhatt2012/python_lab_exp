import sqlite3

conn =  sqlite3.connect('phonelist.db')

conn.execute('''CREATE TABLE PHONELIST(
    PHONE_NUMBER CHAR(10) PRIMARY KEY NOT NULL,
    NAME VARCHAR(100));''')

print('Table created succesfully')

conn.close()
