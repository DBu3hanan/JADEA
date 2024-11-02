import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import tkinter


    
root = tkinter.Tk()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')

filemenu.add_command(label='Exit', command=root.quit)


helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label="View Guidelines")


root.title("JADE")
root.config(background="black")
root.geometry("600x400") #W x L
root = Label(root, text='Jamaican Association for Debating and Empowerment', font=("Times New Roman", 16))
root.pack()


root.mainloop()