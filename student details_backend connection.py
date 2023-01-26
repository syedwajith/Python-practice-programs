from tkinter import *
import tkinter.messagebox
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='studentdetails')
cursor = db.cursor()

def add():
    regno = std_regno.get()
    name = std_name.get()
    dob = std_dob.get()
    phno = std_phno.get()
    mail = std_mailid.get()
    deg = std_deg.get()
    dept = std_dept.get()
    yr = std_yrstud.get()
    sem = std_sem.get()
    cgpa =std_cgpa.get()
    cursor.execute('insert into studentinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[regno,name,dob,phno,mail,deg,dept,yr,sem,cgpa])
    db.commit()
    tkinter.messagebox.showinfo('Access','Datas are Added Successfully')


def view():
    regno = std_regno.get()
    cursor.execute('select * from studentinfo where reg_no=%s',[regno])
    data = cursor.fetchone()
    std_name.set(data[1])
    std_dob.set(data[2])
    std_phno.set(data[3])
    std_mailid.set(data[4])
    std_deg.set(data[5])
    std_dept.set(data[6])
    std_yrstud.set(data[7])
    std_sem.set(data[8])
    std_cgpa.set(data[9])

def update():
    regno = std_regno.get()
    dob = std_dob.get()
    phno = std_phno.get()
    mail = std_mailid.get()
    yr = std_yrstud.get()
    sem = std_sem.get()
    cgpa =std_cgpa.get()
    cursor.execute('update studentinfo set dob=%s,phone_no=%s,email_id=%s,year_of_study=%s,semester=%s,cgpa=%s where reg_no=%s',[dob,phno,mail,yr,sem,cgpa,regno])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Datas are Updated Successfully')

ob=Tk()
ob.geometry('900x700')
ob.title('Student portal')
ob.configure(bg='pink')

Label(ob, text='Welcome to Student Portal', font=('calibri',20), bg='pink', fg='blue').place(x=200,y=10)

std_regno_label = Label(ob, text='Student RegNo ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=100)
std_regno = StringVar()
std_regno_entry = Entry(ob, textvariable=std_regno, font=('calibri',15), bg='white').place(x=400,y=100)

std_name_label = Label(ob, text='Student Name ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=150)
std_name = StringVar()
std_name_entry = Entry(ob, textvariable=std_name, font=('calibri',15), bg='white').place(x=400,y=150)

std_dob_label = Label(ob, text='Student DOB ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=200)
std_dob = StringVar()
std_dob_entry = Entry(ob, textvariable=std_dob, font=('calibri',15), bg='white').place(x=400,y=200)

std_phno_label = Label(ob, text='Student PhoneNo ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=250)
std_phno = StringVar()
std_phno_entry = Entry(ob, textvariable=std_phno, font=('calibri',15), bg='white').place(x=400,y=250)

std_mailid_label = Label(ob, text='Student E-Mailid ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=300)
std_mailid = StringVar()
std_mailid_entry = Entry(ob, textvariable=std_mailid, font=('calibri',15), bg='white').place(x=400,y=300)

std_deg_label = Label(ob, text='Degree ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=350)
std_deg = StringVar()
std_deg_entry = Entry(ob, textvariable=std_deg, font=('calibri',15), bg='white').place(x=400,y=350)

std_dept_label = Label(ob, text='Department', font=('calibri',15), bg='pink', fg='red').place(x=150,y=400)
std_dept = StringVar()
std_dept_entry = Entry(ob, textvariable=std_dept, font=('calibri',15), bg='white').place(x=400,y=400)

std_yrstud_label = Label(ob, text='Year of Study ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=450)
std_yrstud = StringVar()
std_yrstud_entry = Entry(ob, textvariable=std_yrstud, font=('calibri',15), bg='white').place(x=400,y=450)

std_sem_label = Label(ob, text='Semester ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=500)
std_sem = StringVar()
std_sem_entry = Entry(ob, textvariable=std_sem, font=('calibri',15), bg='white').place(x=400,y=500)

std_cgpa_label = Label(ob, text='OverAll CGPA ', font=('calibri',15), bg='pink', fg='red').place(x=150,y=550)
std_cgpa = StringVar()
std_cgpa_entry = Entry(ob, textvariable=std_cgpa, font=('calibri',15), bg='white').place(x=400,y=550)

button_add = Button(ob, text='ADD', command=add, fg='black', bg='lightgray', width='10', height='1').place(x=700,y=300)

button_view = Button(ob, text='VIEW', command=view, fg='black', bg='lightgray', width='10', height='1').place(x=800,y=300)

button_upd = Button(ob, text='UPDATE', command=update, fg='black', bg='lightgray', width='10', height='1').place(x=750,y=400)

ob.mainloop()