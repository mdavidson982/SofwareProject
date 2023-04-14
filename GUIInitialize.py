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

class Window():
    
    def __init__(self,master):
            frame0 = Frame(master)
            label= Label(frame0, text="test").pack()
            frame0.pack(side=LEFT)

            frame1 = Frame(master)
            r = st.ScrolledText(frame1, width = 30, height = 10,font = ("Times New Roman", 12)).pack()
            frame1.pack(padx=10,pady=10, side= RIGHT)
            
            frame2 = Frame(master)
            lb= Label(frame2, text = "Enter filepath").pack(side=LEFT)
            e =Entry(frame2).pack(side=LEFT)
            calc = Button(frame2, text = "Enter").pack(side=RIGHT)
            browse = Button(frame2, text = "Browse", command = lambda:browse_click()).pack(side=LEFT)
            frame2.pack(padx=10,pady=10, side=BOTTOM)

            def browse_click():
                file = askopenfile(mode = 'r' , filetypes= [('RUN Files','*.RUN')]) #opens file browser system
                if file is not NONE: 
                    filepath = os.getcwd()
                    e.insert(0,filepath)  #gets current working directory and pastes in to the input box

            def button_enter():
                e.get()
            
                            #MUST USE DIRECTORY FUNCTIONS CWD

            def text_box():
                r.insert("Data") #CALL DATA PROCESSING FROM FILE READING



window = tk.Tk()
root = Window(window)
window.title("GPA Calculator")

window.mainloop()
