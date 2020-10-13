import tkinter
from tkinter import *
base = tkinter.Tk()
base.geometry('300x300')
base.title("calculator")
base.configure(bg="light yellow")
t1 = Entry(base,bg="green",width=60,bd=3,fg="black")
t1.place(x=0,y=30)
Label(base,text="CALCULATOR").pack()
def press(m):#function for key press
    exp =""
    exp=exp.__add__(str(m))
    t1.insert((t1.get().__len__()),exp)
    print(type(exp))
    print(exp)
    print(len(exp))
def clear(): #function for clear
    t1.delete(0, str(t1.get()).__len__())
def equalsto():#function for =
    a = t1.get()
    b = eval(a)
    t1.delete(0, str(t1.get()).__len__())
    t1.insert(0,str(b))
#------------Buttons strat--------------
b1 = Button(base,text="1",bg="grey",fg="black",width=4,bd=4, command=lambda:press(1)).place(x=70,y=60)
b2 = Button(base,text="2",bg="grey",fg="black",width=4,bd=4,command=lambda:press(2)).place(x=120,y=60)
b3 = Button(base,text="3",bg="grey",fg="black",width=4,bd=4,command=lambda:press(3)).place(x=170,y=60)
b4 = Button(base,text="4",bg="grey",fg="black",width=4,bd=4,command=lambda:press(4)).place(x=70,y=90)
b5 = Button(base,text="5",bg="grey",fg="black",width=4,bd=4,command=lambda:press(5)).place(x=120,y=90)
b6 = Button(base,text="6",bg="grey",fg="black",width=4,bd=4,command=lambda:press(6)).place(x=170,y=90)
b7 = Button(base,text="7",bg="grey",fg="black",width=4,bd=4,command=lambda:press(7)).place(x=70,y=120)
b8 = Button(base,text="8",bg="grey",fg="black",width=4,bd=4,command=lambda:press(8)).place(x=120,y=120)
b9 = Button(base,text="9",bg="grey",fg="black",width=4,bd=4,command=lambda:press(9)).place(x=170,y=120)
b0 = Button(base,text="0",bg="grey",fg="black",width=4,bd=4,command=lambda:press(0)).place(x=120,y=150)
b11 = Button(base,text="=",bg="grey",fg="black",width=4,bd=4,command=equalsto).place(x=70,y=150)
b12 = Button(base,text="clear",bg="grey",fg="black",width=4,bd=4,command=clear).place(x=170,y=150)
b13 = Button(base,text="+",bg="grey",fg="black",width=4,bd=4,command=lambda:press("+")).place(x=220,y=60)
b14 = Button(base,text="-",bg="grey",fg="black",width=4,bd=4,command=lambda:press("-")).place(x=220,y=90)
b15 = Button(base,text="*",bg="grey",fg="black",width=4,bd=4,command=lambda:press("*")).place(x=220,y=120)
b16 = Button(base,text="/",bg="grey",fg="black",width=4,bd=4,command=lambda:press("/")).place(x=220,y=150)

#---------buttons end------------



base.mainloop()