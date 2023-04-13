################################################
#
#Creator: Zayvier Hartman
#Purpose: For COMSC330 GPA calculator project
#Date:4/2/23
#Description: This program is meant to create a GUI to display results from FileReading.py

import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st
import os
#import FileReading as fr

window = tk.Tk()

window.title("GPA Calculator")

lb = Label(window, text = "Enter filepath")
lb.grid(row = 0, column = 1)

#create entry box

e = Entry(window)
e.grid(row = 1 , column= 1, padx= 10,pady= 10)

#create browse file button

browse = Button(window, text = "Browse")
browse.grid(row = 1 , column = 0, padx = 10, pady = 10)

#create calculate button

calc = Button(window, text = "Enter")
calc. grid(row = 2, column = 0,columnspan = 2, padx = 10,pady= 10, )

#Create results box

r = st.ScrolledText(window, width = 30, height = 10,font = ("Times New Roman", 12))

r.grid(row = 1 , column = 2, padx = 10, pady= 10)

#Create button definitions
#Process browse ONCLICK funcion, should allow user to browse system files

def button_browse():
    r.insert("browse") #THIS IS NOT DONE 
                        #USE OS MODULE TO DO

def button_enter():
    path = e.get()
                    #MUST USE DIRECTORY FUNCTIONS CWD

def text_box():
    r.insert("Data") #CALL DATA PROCESSING FROM FILE READING



window.mainloop()
