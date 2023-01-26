from tkinter import *
import tkinter.messagebox
from unicodedata import name
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',db='employee_details')
cursor = db.cursor()

def calculate():
    emp_annualsal.set(int(emp_sal.get())*12)

def add():
    id = emp_id.get()
    name = emp_name.get()
    cno = emp_contactno.get()
    email = emp_emailid.get()
    sal = emp_sal.get()
    asal = emp_annualsal.get()
    cursor.execute('insert into employeesdata values(%s,%s,%s,%s,%s,%s)',[id,name,cno,email,sal,asal])
    db.commit()
    tkinter.messagebox.showinfo('Access','Datas are Added Successfully')

def view():
    id = emp_id.get()
    cursor.execute('select * from employeesdata where emp_id=%s',[id])
    data = cursor.fetchone()
    emp_name.set(data[1])
    emp_contactno.set(data[2])
    emp_emailid.set(data[3])
    emp_sal.set(data[4])
    emp_annualsal.set(data[5])

def update():
    id = emp_id.get()
    cno = emp_contactno.get()
    email = emp_emailid.get()
    sal = emp_sal.get()
    asal = emp_annualsal.get()
    cursor.execute('update employeesdata set contact_no=%s,email_id=%s,salary=%s,annual_salary=%s where emp_id=%s',[cno,email,sal,asal,id])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Datas are Updated Successfully')

def delete():
    id = emp_id.get()
    cursor.execute('delete from employeesdata where emp_id=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Datas are deleted Successfully')

def overall():
    global empdetails
    empdetails = Toplevel()
    empdetails.geometry('900x300')
    empdetails.config(bg='lightgreen')
    empdetails.title('Employee Details')
    cursor.execute('select * from employeesdata')
    data = cursor.fetchall()
    row = len(data)
    col = len(data[0])
    Label(empdetails, text='Emp id', font=('calibri',12), fg='blue', bg='lightgreen').grid(row=0,column=0)
    Label(empdetails, text='Emp Nmae', font=('calibri',12), fg='blue', bg='lightgreen').grid(row=0,column=1)
    Label(empdetails, text='Contact No', font=('calibri',12), fg='blue', bg='lightgreen').grid(row=0,column=2)
    Label(empdetails, text='Email id', font=('calibri',12), fg='blue', bg='lightgreen').grid(row=0,column=3)
    Label(empdetails, text='Salary', font=('calibri',12), fg='blue', bg='lightgreen').grid(row=0,column=4)
    Label(empdetails, text='Annual Salary', font=('calibri',12), fg='blue', bg='lightgreen').grid(row=0,column=5)

    for i in range(row):
        for j in range(col):
            e = Entry(empdetails, font=('calibri',10), bg='lightgreen')
            e.grid(row=i+1,column=j)
            e.insert(END,data[i][j])

def clear():
    id = emp_id.set('')
    name = emp_name.set('')
    cno = emp_contactno.set('')
    email = emp_emailid.set('')
    sal = emp_sal.set('')
    asal = emp_annualsal.set('')


ob = Tk()
ob.geometry('800x700')
ob.configure(bg='aqua')
ob.title('Employee Details Entry')

Label(ob, text='Welcome to Employee Details Entry', font=('calibri',21), fg='darkgreen', bg='aqua').place(x=200,y=10)

emp_id_lable = Label(ob, text='Emp id', font=('calibri',20),fg='brown', bg='aqua').place(x=150,y=100)
emp_id = StringVar()
emp_id_entry = Entry(ob, textvariable=emp_id, font=('calibri',20), bg='white').place(x=400,y=100)

emp_name_lable = Label(ob, text='Emp name', font=('calibri',20),fg='brown', bg='aqua').place(x=150,y=150)
emp_name = StringVar()
emp_name_entry = Entry(ob, textvariable=emp_name, font=('calibri',20), bg='white').place(x=400,y=150)

emp_contactno_lable = Label(ob, text='Contact No', font=('calibri',20),fg='brown', bg='aqua').place(x=150,y=200)
emp_contactno = StringVar()
emp_contactno_entry = Entry(ob, textvariable=emp_contactno, font=('calibri',20), bg='white').place(x=400,y=200)

emp_emailid_lable = Label(ob, text='Email id', font=('calibri',20),fg='brown', bg='aqua').place(x=150,y=250)
emp_emailid = StringVar()
emp_emailid_entry = Entry(ob, textvariable=emp_emailid, font=('calibri',20), bg='white').place(x=400,y=250)

emp_sal_lable = Label(ob, text='Salary', font=('calibri',20),fg='brown', bg='aqua').place(x=150,y=300)
emp_sal = StringVar()
emp_sal_entry = Entry(ob, textvariable=emp_sal, font=('calibri',20), bg='white').place(x=400,y=300)

emp_annualsal_lable = Label(ob, text='Annual Salary', font=('calibri',20),fg='brown', bg='aqua').place(x=150,y=350)
emp_annualsal = StringVar()
emp_annualsal_entry = Entry(ob, textvariable=emp_annualsal, font=('calibri',20), bg='white').place(x=400,y=350)

button_cal = Button(ob, text='Calculate', command=calculate, fg='black', bg='lightgray', width='10', height='1').place(x=700,y=350)

button_add = Button(ob, text='ADD', command=add, fg='black', bg='lightgray', width='10', height='1').place(x=250,y=450)

button_view = Button(ob, text='VIEW', command=view, fg='black', bg='lightgray', width='10', height='1').place(x=500,y=450)

button_upd = Button(ob, text='UPDATE', command=update, fg='black', bg='lightgray', width='10', height='1').place(x=250,y=500)

button_del = Button(ob, text='DELETE', command=delete, fg='black', bg='lightgray', width='10', height='1').place(x=500,y=500)

button_ovr = Button(ob, text='OVERALL', command=overall, fg='black', bg='lightgray', width='10', height='1').place(x=250,y=550)

button_clr = Button(ob, text='CLEAR', command=clear, fg='black', bg='lightgray', width='10', height='1').place(x=500,y=550)

ob.mainloop()