################################################
#
#Creator: Zayvier Hartman
#Purpose: For COMSC330 GPA calculator project
#Date:4/2/23
#Description: This program is meant to create a GUI to display results from FileReading.py

import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import os
import FileReading as fr
import DataProcessing as dp

DataFrame = None
window = tk.Tk()

window.title("GPA Calculator")

lb = Label(window, text = "Enter filepath")
lb.grid(row = 0, column = 1)

#create entry box

e = Entry(window)
e.grid(row = 1 , column= 1, padx= 10,pady= 10)


#create calculate button

calc = Button(window, text = "Enter")
calc. grid(row = 2, column = 0,columnspan = 2, padx = 10,pady= 10, )

#Create results box

r = st.ScrolledText(window, width = 30, height = 10,font = ("Times New Roman", 12))

r.grid(row = 1 , column = 2, padx = 10, pady= 10)

#Create button definitions
#Process browse ONCLICK funcion, should allow user to browse system files

def browse_click():
    file = askopenfile(mode = 'r' , filetypes= [('RUN Files','*.run')])
    if file is not NONE:
        FileReading = fr.FileReading(file.name)
        DataFrame = FileReading.openFile()
        if isinstance(DataFrame,tuple):
            r.insert(tk.END, "Error: No such File Found\n")
            r.insert(tk.END, "Missing File: {file}".format(file = DataFrame[1]))
        #if it's not a tuple. It's a DataFrame
        else:
            #replace_widget()
            print("n/a")


def button_enter():
    path = e.get()
                    #MUST USE DIRECTORY FUNCTIONS CWD

def text_box():
    r.insert("Data") #CALL DATA PROCESSING FROM FILE READING

#create Browse Button for file browsing

browse = Button(window, text = "Browse", command = lambda:browse_click())
browse.grid(row = 1 , column = 0, padx = 10, pady = 10)

window.mainloop()
