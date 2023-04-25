import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import FileReading as fr
import DataProcessing as dp
from tkinter.filedialog import askopenfile
import os, io
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


global DataFrame
DataFrame = pd.DataFrame()
# Create the Tkinter window
root = tk.Tk()
root.title("Testing")
root.config(bg="#3a383d")
#left_frame = tk.Frame(root,width=200, height = 400)
#left_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.figure()
plt.plot([1, 2])

img_buf = io.BytesIO()
plt.savefig(img_buf, format='png')
load = Image.open(img_buf)
render = ImageTk.PhotoImage(load)





    
#------------------------------------------------------------Left Window Shit------------------------------------------------------------------#
left_frame = tk.Frame(root, width = 500, height = 750, bg = "#106d8f")
left_frame.grid(row=0,column=0,padx=10, pady=5)

left_select = tk.Frame(left_frame, width= 500, height = 100, bg= "#626873")
left_select.grid(row=0,column=0,padx=10, pady=5)

left_title = tk.Label(left_select, text = "Class Statistics",font = ("Times New Roman", 24), bg= "#626873")
left_title.grid(row=0, column=0,padx=1, pady=2)

left_selection = ttk.Combobox(left_select, width=35, height = 20,values=[""], font=("Times New Roman", 18))
left_selection.bind("<<ComboboxSelected>>",lambda event:select(event))
left_selection.grid(column=0,row=1, padx=1, pady=2)

left_statistics = tk.Frame(left_frame, width= 500, height = 650)
left_statistics.grid(row=1,column=0,padx=10, pady=5)


#---------------------------------------------------------------Right Window Shit---------------------------------------------------------------#

right_frame = tk.Frame(root, width=500, height = 750, bg = "#106d8f" )
right_frame.grid(row=0,column=1,padx=10, pady=5)

right_selection = tk.Frame(right_frame, width= 500, height = 100, bg= "#626873")
right_selection.grid(row=0,column=0,padx=10, pady=5)

right_title = tk.Label(right_selection, text = "Class Grades",font = ("Times New Roman", 24), bg= "#626873")
right_title.grid(row=0, column=0,padx=1, pady=2)

right_selection = ttk.Combobox(right_selection, width=35, height = 20,values=[""], font=("Times New Roman", 18))
right_selection.grid(row=1,column=0,padx=1, pady=2)

tabController = ttk.Notebook(right_frame)
tabController.grid(row=1,column=0,padx=10, pady=5)

right_grades = ttk.Frame(tabController, width= 500, height = 625)
right_grades.grid(row=1,column=0,padx=10, pady=5)

grade_display = Scrollbar(right_grades, orient="vertical")  
grade_display.grid(row = 0,column = 0)

right_graphs = ttk.Frame(tabController, height = 500)
ttk.Label(right_graphs, image= render).grid(row = 0, column = 0)

tabController.add(right_grades, text = "Grades")
tabController.add(right_graphs, text = "Graphs")

#---------------------------------------------------------------Bottom Window Shit-----------------------------------------------------------------#

bottom_frame = tk.Frame(root, width = 1000, height = 200)
bottom_frame.grid(row = 1, column= 0, columnspan=2, padx=10, pady =5)

bottom_title = tk.Label(bottom_frame, text = "Enter File Path: ", font = ("Times New Roman", 12), bg = "#626873")
bottom_title.grid(row = 0, column=0, columnspan= 3)

bottom_browse = tk.Button(bottom_frame, text = "Browse", command = lambda:browse_click())
bottom_browse.grid(row = 1 , column = 0, padx = 10, pady = 10)

bottom_entry = tk.Entry(bottom_frame, width= 75)
bottom_entry.grid(row = 1, column= 1)

#------------------------------------------------------------Make tables for stats frame-----------------------------------------------------------

#group_tree = ttk.Treeview(left_statistics, column =("Group","GPA Average") , show='headings',height=5)
#group_tree.column("# 1", anchor=CENTER)
#group_tree.heading("# 1", text="Group")
#group_tree.column("# 2", anchor=CENTER)
#group_tree.heading("# 2", text="GPA Average")

#sec_tree = ttk.Treeview(left_statistics, column =("Section","GPA Average") , show='headings',height=5)
#sec_tree.column("# 1", anchor=CENTER)
#sec_tree.heading("# 1", text="Section")
#sec_tree.column("# 2", anchor=CENTER)
#sec_tree.heading("# 2", text="GPA Average")




def browse_click():
    global DataFrame
    file = askopenfile(mode = 'r' , filetypes= [('RUN Files','*.run')])
    bottom_entry.delete(0, END)
    bottom_entry.insert(0,file.name)
    if file is not NONE:
        FileReading = fr.FileReading(file.name)
        DataFrame = FileReading.openFile()
        if isinstance(DataFrame,tuple):
            errorString = ("Error: No such File Found\nMissing File: {file}".format(file = DataFrame[1]))
            error_label = tk.Label(right_grades, text = errorString)
            error_label.grid(row = 0, column = 0)
        #if it's not a tuple. It's a DataFrame
        else:
            DataFrame = dp.letterTogpa(DataFrame)
            left_selection["values"] = dp.listedComboBox(DataFrame)

            
           
def select(event):
    global DataFrame
    selected_item = event.widget.get()
    print(f"Selected Item: {selected_item}")
    SelectedFrame = dp.leftSelect(DataFrame,selected_item)
    for widget in grade_display.winfo_children():
        widget.destroy()
    for index, row in SelectedFrame.iterrows():
       test1 = Label(grade_display, text=row["First Name"], font = ("Times New Roman", 15), bg="#a5a8a6", fg="#000000", width = 15)
       test1.grid(row=index, column=0,columnspan=2, sticky="wens")
       test1.bind('<Double-1>', _clipboard_copy(test1))
       test1.bind('<Enter>', lambda ev, lab=test1: lab.config(fg='white'))
       test1.bind('<Leave>', lambda ev, lab=test1: lab.config(fg='black'))
       test2 = Label(grade_display, text=row["Last Name"], font = ("Times New Roman", 15), bg="#a5a8a6", fg="#000000", width = 15)
       test2.grid(row=index, column=3,columnspan=2, sticky="wens")
       test2.bind('<Double-1>', _clipboard_copy(test2))
       test2.bind('<Enter>', lambda ev, lab=test2: lab.config(fg='white'))
       test2.bind('<Leave>', lambda ev, lab=test2: lab.config(fg='black'))
       color = dp.gradeColor(row["Grade"])
       test3 = Label(grade_display, text=row["Grade"], font = ("Times New Roman", 15), bg = color, fg="#000000", width = 15)
       test3.grid(row=index, column=5,columnspan=2, sticky="wens")
       test3.bind('<Double-1>', _clipboard_copy(test3))
       test3.bind('<Enter>', lambda ev, lab=test3: lab.config(fg='white'))
       test3.bind('<Leave>', lambda ev, lab=test3: lab.config(fg='black'))

def _clipboard_copy(inst):
    def wrapper(event):
        inst.clipboard_clear()
        inst.clipboard_append(inst['text'])
    return wrapper       
                


root.mainloop()