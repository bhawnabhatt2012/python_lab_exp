import sqlite3

conn =  sqlite3.connect('phonelist.db')

cursor = conn.execute("SELECT * from PHONELIST")
for row in cursor:
   print ("PHONE_NUMBER = ", row[0])
   print ("NAME = ", row[1])


print ("Operation done successfully")

conn.close()