import tkinter as tk
from tkinter import Label,Button

class Heading:
    def __init__(self,top):
        self.top=top
        top.title("RESTAURANT MANAGEMENT SYSTEM")
        #SET GEOMETRY SIZE
        top.geometry("1028x500")
        top.configure(background="#00564")
        

        self.Label=tk.Label(master=top,text='Restaurant management system')
        self.Label.place(relx=0.268,rely=0.02)
root=tk.Tk()
user_gui = Heading(root)
root.mainloop()