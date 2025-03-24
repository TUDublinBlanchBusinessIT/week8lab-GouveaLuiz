from tkinter import *
import sqlite3

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Tennis Club Membership")

        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry(master)
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()
        self.entry2 = Entry(master)
        self.entry2.pack()

        self.label3 = Label(master, text="Enter your Date of Birth (YYYY-MM-DD)")
        self.label3.pack()
        self.entry3 = Entry(master)
        self.entry3.pack()

        self.label4 = Label(master, text="Enter your Member Type (Junior, Intermediate, Senior)")
        self.label4.pack()
        self.entry4 = Entry(master)
        self.entry4.pack()

        self.insertButton = Button(master, text="Insert Into DB", command=self.insert_member)
        self.insertButton.pack()

        self.printButton = Button(master, text="Print All Members", command=self.print_members)
        self.printButton.pack()

        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

    def insert_member(self):
        firstname = self.entry1.get()
        surname = self.entry2.get()
        dob = self.entry3.get()
        member_type = self.entry4.get()

        conn = sqlite3.connect("tennisclub.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO member (Firstname, Surname, DateOfBirth, MemberType) VALUES (?, ?, ?, ?)", 
                       (firstname, surname, dob, member_type))
        conn.commit()
        conn.close()

        print(f"Inserted: {firstname} {surname}, DOB: {dob}, Type: {member_type}")

    def print_members(self):
        conn = sqlite3.connect("tennisclub.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM member")
        records = cursor.fetchall()
        conn.close()

        
        for record in records:
            print(record)

    def close(self):
        self.master.destroy()

root = Tk()
my_gui = MyFirstGUI(root)

root.mainloop()
