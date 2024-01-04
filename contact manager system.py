import tkinter
import tkinter.ttk as ttk
from tkinter import *
import sqlite3
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title('CONTACT MANAGEMENT SYSTEM')
root.geometry('780x400+0+0')
root.config(bg="green")

#define the variable required for storing the value

f_name =StringVar()
m_name = StringVar()
l_name = StringVar()
email = StringVar()
home_address= StringVar()
phone_number = StringVar()

#create the function for resetting the value

def Reset():
    f_name.set("")
    m_name.set("")
    l_name.set("")
    email.set("")
    home_address.set("")
    phone_number.set("")

#creating the database and table
def Database():
    connection =sqlite3.connect("contactdata.db")
    cursor =connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXIST'contactinformation'(id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,first_name TEXT,middle_name TEXT,last_name TEXT,email TEXT,home_address TEXT,phone_number TEXT)")
    cursor.execute("SELECT * FROM 'contactinformation'ORDER BY 'last_name' ASC")
    fetchinfo = cursor.fetchall()
    for data in fetchinfo:
       tree.insert('', 'end', values=(data))
    cursor.close()
    connection.close()

#function for existing the system
def Exit():
    off = tkinter.messagebox.askyes_or_no('contact management system',"Do you want to exit the system?")
    if off >0:
        root.destroy()
    return

#insert query inserting the value in database table

def Submit():
    if f_name.get()=="" or m_name.get()=="" or l_name.get()=="" or email.get()=="" or phone_number.get()=="" or home_address.get()=="":
        message=tkMessageBox.showwarning('','Please complete All the fields',icon='warning')
    else:
        tree.delete(*tree.get_children())
    connection = sqlite3.connect('contactdata.db')
    cursor = connection.cursor()
    
root.mainloop()