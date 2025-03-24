import sqlite3

conn = sqlite3.connect('tennisclub.db')
myCursor = conn.cursor()
SQL = "select * from member"
rows = myCursor.execute(SQL)
for row in rows: # cursors are iterable
    print(row[1],row[2],row[3],row[4])

