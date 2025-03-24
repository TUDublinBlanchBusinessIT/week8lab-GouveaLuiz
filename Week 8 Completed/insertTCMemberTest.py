import sqlite3

conn = sqlite3.connect('tennisclub.db')
myCursor = conn.cursor()
SQL = "insert into member(firstname, surname, dateofbirth, membertype) values ('Eoin','OK','01/01/2010','Senior')"
row = myCursor.execute(SQL)
conn.commit()
print("row inserted")

