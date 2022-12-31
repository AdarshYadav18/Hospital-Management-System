import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    # e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['ptname'])
    e3.insert(0, select['mobile'])
    var.insert(0, select['gender'])
    e5.insert(0, select['amount'])


def Add():
    ptid = e1.get()
    ptname = e2.get()
    mobile = e3.get()
    gender = var.get()
    amount=e5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Hospital")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  login (id,ptname,mobile,gender,amount) VALUES (%s, %s, %s, %s,%s)"
        val = (ptid, ptname, mobile, gender,amount)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        # e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
def selection():
    e4 = StringVar()
    selection="You selected the option"+str(var.get())
    label.config(text=selection)



def update():
    ptid = e1.get()
    ptname = e2.get()
    mobile = e3.get()
    gender = var.get()
    amount = e5.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Hospital")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  login set ptname=%s,mobile=%s,amount=%s where id=%s"
        val = (ptid, ptname, mobile,amount)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        # e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def search():
    global records
    ptid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Hospital")
    mycursor = mysqldb.cursor()

    try:
        sql = "SELECT *from login where id=%s"
        val = (ptid,)
        mycursor.execute(sql, val)
        records = mycursor.fetchall()
        print(records)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record search successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        # e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()
        for i, (id, ptname, mobile, gender, amount) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, ptname, mobile, gender, amount))
            mysqldb.close()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



def delete():
    ptid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Hospital")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from login where id = %s"
        val = (ptid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        # e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Hospital")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,ptname,mobile,gender,amount FROM login")
    records = mycursor.fetchall()
    print(records)

    # for i, (id, ptname,mobile, gender, amount) in enumerate(records, start=1):
    #     listBox.insert("", "end", values=(id, ptname,mobile, gender, amount))
    #     mysqldb.close()


root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
# global e4
global e5
var=StringVar(root,"1")
tk.Label(root, text="HOSPITAL MANAGEMENT", fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Patient ID").place(x=10, y=10)
Label(root, text=" Name").place(x=10, y=40)
Label(root, text="Mobile").place(x=10, y=70)
Label(root, text="Gender").place(x=10, y=100)

r1=tk.Radiobutton(root,text='Male',value='Male',variable=var,command=selection).place(x=100,y=100)
r2=tk.Radiobutton(root,text='Female',value="Female",variable=var,command=selection).place(x=170,y=100)
r3=tk.Radiobutton(root,text='Other',value="Other",variable=var,command=selection).place(x=250,y=100)
Label(root, text="Amount").place(x=10, y=130)

e1 = Entry(root ,bg='pink')
e1.place(x=100, y=10)

e2 = Entry(root,bg='pink')
e2.place(x=100, y=40)

e3 = Entry(root,bg='pink')
e3.place(x=100, y=70)

e5 = Entry(root,bg='pink')
e5.place(x=100, y=130)

Button(root, text="Add",bg='green' ,command=Add, height=3, width=13).place(x=30, y=155)
Button(root, text="update",bg='sky blue', command=update, height=3, width=13).place(x=140, y=155)
Button(root, text="Delete",bg='red', command=delete, height=3, width=13).place(x=250, y=155)
Button(root, text="Search",bg='yellow', command=search, height=3, width=13).place(x=360, y=155)

cols = ('id', 'ptname', 'mobile', 'gender','amount')
listBox = ttk.Treeview(root, columns=cols, show='headings') #like columns

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=250)

# show()
root.config(bg='orange')
listBox.bind('<Double-Button-1>', GetValue) # double click on blue line highlight for getting value
label=Label(root)
root.mainloop()
