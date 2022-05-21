from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql
from ALL_Button import *
def login():
    db=pymysql.connect(host='localhost',
                       user='root',
                       password='Vkumar@1234',
                       db='StockManagement'
                       )
    cur=db.cursor()
    p=e1.get()
    q=e2.get()
    st="select * from admin_info where adminid='%s' and passwd='%s'"%(p,q)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        messagebox.showwarning('Login Error','User ID or Password not found')
    else:
        mainMenu()
t=tkinter.Tk()
t.geometry('650x650')
t.title('Login')
c=Canvas(t,bg='light grey',height=150, width=400, borderwidth=3)
c.place(x=125,y=200)
l1=Label(t,text='User ID',bg='light grey')
l1.place(x=200,y=230)
l2=Label(t,text='Password',bg='light grey')
l2.place(x=200,y=260)
e1=Entry(t,width=20, )
e1.place(x=350,y=230)
e2=Entry(t,width=20)
e2.place(x=350,y=260)
f1=Frame(t,borderwidth=3,bg='grey')
b1=Button(f1,text='Login',bg='light grey', command=login)
b1.pack()
f1.place(x=350,y=290) 
f2=Frame(t,borderwidth=3,bg='grey')
bc=Button(f2,text='Cancel',bg='light grey', command=t.destroy)
bc.pack()
f2.place(x=420,y=290)
f3=Frame(t,borderwidth=1,bg='grey', relief=SOLID, pady=3)
lL=Label(f3,text='LOGIN',bg='light grey', font=('Arial',20,'bold'))
lL.pack(padx=100,pady=15)
f3.pack(fill='x',padx=5,pady=5)
t.config(bg=('grey'))
t.mainloop()