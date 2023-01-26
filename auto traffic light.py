from time import sleep
from tkinter import *

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

count = 30
def start():
    counter(count)

def counter(cou):
    if cou > 0:
        cou = cou - 1
        new(cou)

def new(c):
    if c > 20:
        red()
        e.config(text=c)
        ob.update()
        sleep(1)
        counter(c)
    elif c > 10 and c <= 20:
        yellow()
        e.config(text=c)
        ob.update()
        sleep(1)
        counter(c)
    elif c > 0 and c <=10:
        green()
        e.config(text=c)
        ob.update()
        sleep(1)
        counter(c)
    elif c == 0:
        count = 30
        red()
        e.config(text=c)
        ob.update()
        sleep(1)
        counter(count)


ob = Tk()
ob.geometry('200x600')
ob.title('Traffic Light - Automatic Control')
ob.configure(bg='lightblue')
e = Label(ob, text=('calibri',13))
e.pack()

canvas1 = Canvas(ob, height=150, bg='black')
canvas1.pack()

canvas2 = Canvas(ob, height=150, bg='black')
canvas2.pack()

canvas3 = Canvas(ob, height=150, bg='black')
canvas3.pack()

Button(ob, text='Start',command=start, font=('calibri',15), bg='cyan', fg='black', width='10', height='1').pack()

ob.mainloop()