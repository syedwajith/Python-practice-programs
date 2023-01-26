from textwrap import fill
from tkinter import *
from turtle import width

def red():
    canvas1.create_oval(120, 120, 50, 50, fill='red', outline='white', width=3)
    canvas2.create_oval(120, 120, 50, 50, fill='white', outline='white', width=3)
    canvas3.create_oval(120, 120, 50, 50, fill='white', outline='white', width=3)

def yellow():
    canvas1.create_oval(120, 120, 50, 50, fill='white', outline='white', width=3)
    canvas2.create_oval(120, 120, 50, 50, fill='yellow', outline='white', width=3)
    canvas3.create_oval(120, 120, 50, 50, fill='white', outline='white', width=3)

def green():
    canvas1.create_oval(120, 120, 50, 50, fill='white', outline='white', width=3)
    canvas2.create_oval(120, 120, 50, 50, fill='white', outline='white', width=3)
    canvas3.create_oval(120, 120, 50, 50, fill='green', outline='white', width=3)

ob = Tk()
ob.geometry('300x400')
ob.title('Traffic Light - Mannual Control')
ob.configure(bg='lightblue')

Button(ob, text='RED',command=red, font=('calibri',15), bg='red', fg='black', width='10', height='1').grid(row=1,column=0)
Button(ob, text='YELLOW',command=yellow, font=('calibri',15), bg='yellow', fg='black', width='10', height='1').grid(row=2,column=0)
Button(ob, text='GREEN',command=green, font=('calibri',15), bg='green', fg='black', width='10', height='1').grid(row=3,column=0)

canvas1 = Canvas(ob, height=130, bg='black')
canvas1.grid(row=1, column=2)

canvas2 = Canvas(ob, height=130, bg='black')
canvas2.grid(row=2, column=2)

canvas3 = Canvas(ob, height=130, bg='black')
canvas3.grid(row=3, column=2)

ob.mainloop()