from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('560x350')
root.title=("Tic Tac Toe Game")
#ROW ONE
button1=ttk.Button(root,text="",command=lambda:buttonPressed(1))
button1.grid(row=0,column=0,ipadx=50,ipady=50)

button2=ttk.Button(root,text="",command=lambda:buttonPressed(2))
button2.grid(row=0,column=1,ipadx=50,ipady=50)

button3=ttk.Button(root,text="",command=lambda:buttonPressed(3))
button3.grid(row=0,column=3,ipadx=50,ipady=50)

#ROW TWO
button4=ttk.Button(root,text="",command=lambda:buttonPressed(4))
button4.grid(row=2,column=0,ipadx=50,ipady=50)

button5=ttk.Button(root,text="",command=lambda:buttonPressed(5))
button5.grid(row=2,column=1,ipadx=50,ipady=50)

button6=ttk.Button(root,text="",command=lambda:buttonPressed(6))
button6.grid(row=2,column=3,ipadx=50,ipady=50)

#ROW THREE
button7=ttk.Button(root,text="",command=lambda:buttonPressed(7))
button7.grid(row=3,column=0,ipadx=50,ipady=50)

button8 =ttk.Button(root,text="",command=lambda:buttonPressed(8))
button8.grid(row=3,column=1,ipadx=50,ipady=50)

button9=ttk.Button(root,text="",command=lambda:buttonPressed(9))
button9.grid(row=3,column=3,ipady=50,ipadx=50)

def buttonPressed(buttonNumber):
    temp=buttonNumber


root.mainloop()