################################################
#
#Creator: Zayvier Hartman
#Purpose: For COMSC330 GPA calculator project
#Date:4/2/23
#Description: This program is meant to create a GUI to display results from FileReading.py

import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st
#import FileReading as fr

window = tk.Tk()

#create entry box

e = Entry(window)
e.insert(0,"Enter filepath")
e.grid(row = 0 , column= 1, padx= 10,pady= 10)

#create browse file button

browse = Button(window, text = "Browse")
browse.grid(row = 0 , column = 0, padx = 10, pady = 10)

#create calculate button

calc = Button(window, text = "Enter")
calc. grid(row = 1, column = 0,columnspan = 2, padx = 10,pady= 10, )

#Create results box

r = st.ScrolledText(window, width = 30, height = 10,font = ("Times New Roman", 12))
r.grid(row = 0 , column = 2, columnspan = 2, rowspan = 2, padx = 10, pady= 10)

window.mainloop()
