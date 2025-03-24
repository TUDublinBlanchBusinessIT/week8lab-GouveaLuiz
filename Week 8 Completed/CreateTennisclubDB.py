import sqlite3

conn = sqlite3.connect("tennisclub.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS member (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Firstname TEXT NOT NULL,
        Surname TEXT NOT NULL,
        DateOfBirth DATE NOT NULL,
        MemberType TEXT CHECK(MemberType IN ('Junior', 'Intermediate', 'Senior')) NOT NULL
    )
''')

members = [
    ("Alice", "Smith", "2008-05-14", "Junior"),
    ("Bob", "Johnson", "1995-09-23", "Intermediate"),
    ("Charlie", "Brown", "1980-11-02", "Senior"),
    ("Diana", "White", "2005-07-19", "Junior"),
    ("Edward", "Davis", "1992-03-30", "Intermediate"),
    ("Fiona", "Clark", "1975-12-25", "Senior")
]

cursor.executemany("INSERT INTO member (Firstname, Surname, DateOfBirth, MemberType) VALUES (?, ?, ?, ?)", members)

conn.commit()

conn.close()

print("Database setup complete and test data inserted.")
