from tkinter import *
import tkinter
import sqlite3

base = Tk()
base.title("basic")
base.geometry("300x300")


l = None
m = None
n = None

Label(base,text="student details").pack()
e1 = Entry(base,width=25,fg="black")
e1.place(x=120,y=40)
Label(base,text="roll no").place(x=40,y=40)

e2 = Entry(base,width=25,fg="black")
e2.place(x=120,y=70)
Label(base,text="Name").place(x=40,y=70)

e3 = Entry(base,width=25,fg="black")
e3.place(x=120,y=100)
Label(base,text="City").place(x=40,y=100)
def getdata(event):
    a = e1.get()
    b = e2.get()
    c = e3.get()
    print(a)
    print(b)
    print(c)
    query = "insert into stud123(roll_no,name,city) values("+a+",'"+b+"'"+",'"+c+"')"
    con = sqlite3.connect("stud")
    con.execute(query)
    con.commit()
    con.close()

def show(e):
    query = "select * from stud123"
    con = sqlite3.connect("stud")
    cur = con.cursor()
    cur.execute(query)
    f2 = Toplevel()
    f2.geometry("200x200")
    f2.title("new window")
    f2.configure(bg="white")

    i = 1
    while True:
        data = cur.fetchone()
        if data != None:
            l = data[0]
            print("student roll no is", data[0])
            m = data[1]
            print("student name is ", data[1])
            n = data[2]
            print("studen city is", data[2])
            print("\n")
            T = Text(f2, height=400, width=400)
            T.pack()
            T.insert(tkinter.END, "student roll no is : " + str(l) +"\n")
            T.insert(tkinter.E,"student name is : " + str(m+"\n"))
            T.insert(tkinter.E,"student city is : " + str(n+"\n"))






        # Label(f2,text="-------------------------------------------------------------------------------------").pack()
            #Label(f2, text="student roll no is : " + str(l)+"\n", fg="black").pack()
           # Label(f2, text="student name is : " + str(m+"\n"), fg="black").pack()
          #  Label(f2, text="student city is : " + str(n+"\n"), fg="black").pack()


        else:
            break

        i = i + 1
    print(type(l))
    print(m)
    print(n)



    f2.mainloop()




btn=Button(base,text="submit",width=6,bd=3)
btn.place(x=120,y=140)
btn.bind("<Button>",getdata)
bt1= Button(base,text="show",width=6,bd=3)
bt1.place(x=120,y=170)
bt1.bind("<Button>",show)

base.mainloop()




























