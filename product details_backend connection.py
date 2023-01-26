from tkinter import *
import tkinter.messagebox
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',db='product_details')
cursor = db.cursor()

def calculate():
    product_tot.set(int(product_price.get())*int(product_qty.get()))

def add():
    id = product_id.get()
    name = product_name.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()
    cursor.execute('insert into products values(%s,%s,%s,%s,%s)',[id,name,price,qty,tot])
    db.commit()
    tkinter.messagebox.showinfo('Access','Values are Added Successfully')

def update():
    id = product_id.get()
    price = product_price.get()
    qty = product_qty.get()
    tot = product_tot.get()
    cursor.execute('update products set price=%s,quantity=%s,total=%s where id=%s',[price,qty,tot,id])
    db.commit()
    tkinter.messagebox.showinfo('Access','Values are Updated Successfully')

def delete():
    id = product_id.get()
    cursor.execute('delete from products where id=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Access','Values are Deleted Successfully')

def clear():
    id = product_id.set('')
    name = product_name.set('')
    price = product_price.set('')
    qty = product_qty.set('')
    tot = product_tot.set('')

def view():
    id = product_id.get()
    cursor.execute('select * from products where id=%s',[id])
    data = cursor.fetchone()
    product_name.set(data[1])
    product_price.set(data[2])
    product_qty.set(data[3])
    product_tot.set(data[4])

def overall():
    global viewdetails
    viewdetails = Toplevel()
    viewdetails.geometry('800x400')
    viewdetails.title('Product List')
    viewdetails.configure(bg='aqua')
    cursor.execute('select * from products')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(viewdetails, text='Product id', font=('calibri',12), bg='aqua').grid(row=0,column=0)
    Label(viewdetails, text='Product name', font=('calibri',12), bg='aqua').grid(row=0,column=1)
    Label(viewdetails, text='Product price', font=('calibri',12), bg='aqua').grid(row=0,column=2)
    Label(viewdetails, text='Product quantity', font=('calibri',12), bg='aqua').grid(row=0,column=3)
    Label(viewdetails, text='Product total', font=('calibri',12), bg='aqua').grid(row=0,column=4)

    for i in range(rows):
        for j in range(cols):
            e = Entry(viewdetails, font=('calibri',9))
            e.grid(row=i+1,column=j)
            e.insert(END, data[i][j])

ob =Tk()
ob.geometry('700x600')
ob.configure(bg='gray')
ob.title('Product Entry')

Label(ob, text='Welcome to Product Entry', font=('calibri',25), fg='darkred', bg='gray').place(x=200,y=20)

product_id_label = Label(ob, text='Product id ', font=('calibri',20), fg='black', bg='gray').place(x=100,y=100)
product_id = StringVar()
product_id_entry = Entry(ob, textvariable=product_id, font=('calibri',20), bg='white').place(x=300,y=100)

product_name_label = Label(ob, text='Product Name ', font=('calibri',20), fg='black', bg='gray').place(x=100,y=150)
product_name = StringVar()
product_name_entry = Entry(ob, textvariable=product_name, font=('calibri',20), bg='white').place(x=300,y=150)

product_price_label = Label(ob, text='Product Price ', font=('calibri',20), fg='black', bg='gray').place(x=100,y=200)
product_price = StringVar()
product_id_price = Entry(ob, textvariable=product_price, font=('calibri',20), bg='white').place(x=300,y=200)

product_qty_label = Label(ob, text='Product Qty ', font=('calibri',20), fg='black', bg='gray').place(x=100,y=250)
product_qty = StringVar()
product_id_qty = Entry(ob, textvariable=product_qty, font=('calibri',20), bg='white').place(x=300,y=250)

product_tot_label = Label(ob, text='Total Price ', font=('calibri',20), fg='black', bg='gray').place(x=100,y=300)
product_tot = StringVar()
product_tot_entry = Entry(ob, textvariable=product_tot, font=('calibri',20), bg='white').place(x=300,y=300)

button_tot = Button(ob, text='Calculate',command=calculate, fg='white', bg='lightpink', width='10', height='1').place(x=610,y=300)

button_add = Button(ob, text='ADD', fg='white', command=add, bg='lightpink', width='10', height='1').place(x=200,y=400)

button_view = Button(ob, text='VIEW', command=view, fg='white', bg='lightpink', width='10', height='1').place(x=400,y=400)

button_upd = Button(ob, text='UPDATE', command=update, fg='white', bg='lightpink', width='10', height='1').place(x=200,y=450)

button_del = Button(ob, text='DELETE', command=delete, fg='white', bg='lightpink', width='10', height='1').place(x=400,y=450)

button_ovr = Button(ob, text='OVERALL', command=overall, fg='white', bg='lightpink', width='10', height='1').place(x=200,y=500)

button_clr = Button(ob, text='CLEAR', command=clear, fg='white', bg='lightpink', width='10', height='1').place(x=400,y=500)

ob.mainloop()