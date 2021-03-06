from tkinter import *
import tkinter 
import pymysql
from StockManagement import *
def mainMenu():
    t=tkinter.Tk()
    t.geometry('650x650')
    l=Label(t,text='Stock Management System',bg='sky blue',font=('Arial',25))
    l.pack()
    l1=Label(t,text='Item Category',bg='sky blue')
    l1.place(x=30,y=100)
    l2=Label(t,text='Items',bg='sky blue')
    l2.place(x=30,y=150)
    l3=Label(t,text='Customers',bg='sky blue')
    l3.place(x=30,y=200)
    l4=Label(t,text='Orders',bg='sky blue')
    l4.place(x=30,y=250)
    l5=Label(t,text='Bill',bg='sky blue')
    l5.place(x=30,y=300)
    l6=Label(t,text='Stock',bg='sky blue')
    l6.place(x=30,y=350)
    f1=Frame(t,borderwidth=3,bg='grey')
    b1=Button(f1,text='Enter Data',bg='light grey',command=itemcategoryInsert)
    b1.pack()
    f1.place(x=250,y=100)
    f2=Frame(t,borderwidth=3,bg='grey')
    b2=Button(f2,text='Find Data',bg='light grey',command=itemcategoryFind)
    b2.pack()
    f2.place(x=330,y=100)
    f3=Frame(t,borderwidth=3,bg='grey')
    b3=Button(f3,text='Update Data',bg='light grey',command=itemcategoryUpdate)
    b3.pack()
    f3.place(x=407,y=100)
    f4=Frame(t,borderwidth=3,bg='grey')
    b4=Button(f4,text='Delete Data',bg='light grey',command=itemcategoryDelete)
    b4.pack()
    f4.place(x=498,y=100)
    f5=Frame(t,borderwidth=3,bg='grey')
    b5=Button(f5,text='Enter Data',bg='light grey',command=itemsInsert)
    b5.pack()
    f5.place(x=250,y=150)
    f6=Frame(t,borderwidth=3,bg='grey')
    b6=Button(f6,text='Find Data',bg='light grey',command=itemsFind)
    b6.pack()
    f6.place(x=330,y=150)
    f7=Frame(t,borderwidth=3,bg='grey')
    b7=Button(f7,text='Update Data',bg='light grey',command=itemsUpdate)
    b7.pack()
    f7.place(x=407,y=150)
    f8=Frame(t,borderwidth=3,bg='grey')
    b8=Button(f8,text='Delete Data',bg='light grey',command= itemsDelete)
    b8.pack()
    f8.place(x=498,y=150)
    f9=Frame(t,borderwidth=3,bg='grey')
    b9=Button(f9,text='Enter Data',bg='light grey',command=customerInsert)
    b9.pack()
    f9.place(x=250,y=200)
    f10=Frame(t,borderwidth=3,bg='grey')
    b10=Button(f10,text='Find Data',bg='light grey',command= customerFind)
    b10.pack()
    f10.place(x=330,y=200)
    f11=Frame(t,borderwidth=3,bg='grey')
    b11=Button(f11,text='Update Data',bg='light grey',command=customerUpdate)
    b11.pack()
    f11.place(x=407,y=200)
    f12=Frame(t,borderwidth=3,bg='grey')
    b12=Button(f12,text='Delete Data',bg='light grey',command=customerDelete)
    b12.pack()
    f12.place(x=498,y=200)
    f13=Frame(t,borderwidth=3,bg='grey')
    b13=Button(f13,text='Enter Data',bg='light grey',command=ordersInsert)
    b13.pack()
    f13.place(x=250,y=250)
    f14=Frame(t,borderwidth=3,bg='grey')
    b14=Button(f14,text='Find Data',bg='light grey',command=ordersFind)
    b14.pack()
    f14.place(x=330,y=250)
    f15=Frame(t,borderwidth=3,bg='grey')
    b15=Button(f15,text='Update Data',bg='light grey',command= orderUpdate)
    b15.pack()
    f15.place(x=407,y=250)
    f16=Frame(t,borderwidth=3,bg='grey')
    b16=Button(f16,text='Delete Data',bg='light grey',command=ordersDelete)
    b16.pack()
    f16.place(x=498,y=250)
    f17=Frame(t,borderwidth=3,bg='grey')
    b17=Button(f17,text='Enter Data',bg='light grey',command= billsInsert)
    b17.pack()
    f17.place(x=250,y=300)
    f18=Frame(t,borderwidth=3,bg='grey')
    b18=Button(f18,text='Find Data',bg='light grey',command=billsFind)
    b18.pack()
    f18.place(x=330,y=300)
    f19=Frame(t,borderwidth=3,bg='grey')
    b19=Button(f19,text='Update Data',bg='light grey',command=billsUpdate)
    b19.pack()
    f19.place(x=407,y=300)
    f20=Frame(t,borderwidth=3,bg='grey')
    b20=Button(f20,text='Delete Data',bg='light grey',command= billsDelete)
    b20.pack()
    f20.place(x=498,y=300)
    f21=Frame(t,borderwidth=3,bg='grey')
    b21=Button(f21,text='Enter Data',bg='light grey',command=stockInsert)
    b21.pack()
    f21.place(x=250,y=350)
    f22=Frame(t,borderwidth=3,bg='grey')
    b22=Button(f22,text='Find Data',bg='light grey',command=stockFind)
    b22.pack()
    f22.place(x=330,y=350)
    f23=Frame(t,borderwidth=3,bg='grey')
    b23=Button(f23,text='Update Data',bg='light grey',command=stockUpdate)
    b23.pack()
    f23.place(x=407,y=350)
    f24=Frame(t,borderwidth=3,bg='grey')
    b24=Button(f24,text='Delete Data',bg='light grey',command=stockDelete)
    b24.pack()
    f24.place(x=498,y=350)
    t.config(bg='sky blue')    
    t.mainloop()
    