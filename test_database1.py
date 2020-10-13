'''from tkinter import *
import tkinter
import sqlite3
a = input()
b = input()
c = input()
print(type(a))
#query = "create table stud123(roll_no number(3),name varchar(20),city varchar(20))"
shr = "insert into stud123(roll_no,name,city) values("+a+",'"+b+"'"+",'"+c+"')"
con = sqlite3.connect("stud")
print(shr)
con.execute(shr)
con.commit()
con.close()'''
from tkinter import *
import tkinter
base1 = Tk()
base1.title("basic")
base1.geometry("300x300")
def show_new_wind(e):
    f2 = Toplevel()
    f2.geometry("200x200")
    f2.title("new window")
    f2.configure(bg="light blue")
    Label(f2,text="this is new window").pack()
base1.configure(bg="light yellow")
b1 = Button(base1, text="sign in", width=4, bd=4, bg="grey", fg="red")
b1.place(x=70, y=80)
b1.bind('<Button>', show_new_wind)
base1.mainloop()
'''import sqlite3
query = "select * from stud123"
con = sqlite3.connect("stud")
cur = con.cursor()
cur.execute(query)
i=1
while i == 1:
    data = cur.fetchone()
    if data != None:
        print("student roll no is",data[0])
        print("student name is ",data[1])
        print("studen city is",data[2])
        print("\n")
    else:
        break
    i=i+1


con.close()'''


