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
left_frame = tk.Frame(root, width = 500, height = 650, bg = "#106d8f")
left_frame.grid(row=0,column=0,padx=10, pady=5)

left_select = tk.Frame(left_frame, width= 500, height = 100, bg= "#626873")
left_select.grid(row=0,column=0,padx=10, pady=5)

left_title = tk.Label(left_select, text = "Class Statistics",font = ("Times New Roman", 24), bg= "#626873")
left_title.grid(row=0, column=0,padx=1, pady=2)

left_selection = ttk.Combobox(left_select, width=35, height = 20,values=[""], font=("Times New Roman", 18))
left_selection.bind("<<ComboboxSelected>>",lambda event:select(event))
left_selection.grid(column=0,row=1, padx=1, pady=2)

left_statistics = tk.Frame(left_frame, width= 600, height = 650)
left_statistics.grid(row=1,column=0,padx=10, pady=5)


#---------------------------------------------------------------Right Window Shit---------------------------------------------------------------#

right_frame = tk.Frame(root, bg = "#106d8f" )
right_frame.grid(row=0,column=1,padx=10, pady=5)

right_selection = tk.Frame(right_frame, width= 500, height = 100, bg= "#626873")
right_selection.grid(row=0,column=0,padx=10, pady=5)

right_title = tk.Label(right_selection, text = "Class Grades",font = ("Times New Roman", 24), bg= "#626873")
right_title.grid(row=0, column=0,padx=1, pady=2)

right_selection = ttk.Combobox(right_selection, width=35, height = 20,values=[""], font=("Times New Roman", 18))
right_selection.grid(row=1,column=0,padx=1, pady=2)
# canvas is the only thing that works with scroll bar
# place notebook inside canvas to get scrolling to wor


#Notebook has control of window sizing
#Notebook allows to create tabs to change page to page
tabController = ttk.Notebook(right_frame,height=625, width= 775)
tabController.grid(row=1,column=0,padx=10, pady=5)

right_canvas = Canvas(tabController, height=647, width=800)
right_canvas.grid(row= 0, column = 0, padx=10,pady=5)

right_grades = ttk.Frame(right_canvas, height=625 , width=500, padding=10)
right_grades.grid(row=0,column=0,padx=10, pady=5)

grade_scroll = ttk.Scrollbar(right_grades, orient=VERTICAL, command=right_canvas.yview)  
grade_scroll.grid(row = 0,column = 0)

#Scroll bar configuration 
right_canvas.configure(yscrollcommand=grade_scroll.set)
right_canvas.bind('<Configure>', lambda e: right_canvas.configure(scrollregion = right_canvas.bbox("all")))
right_canvas.create_window((750,0), window = right_grades, anchor = "nw")

right_graphs = ttk.Frame(tabController, height = 625, width=500, padding=10)
ttk.Label(right_graphs, image= render).grid(row = 0, column = 0)

tabController.add(right_canvas, text = "Grades")
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

#---------------------------------------------------------------Populated frames with dataframes--------------------------------------------------------------------------------------
           
def select(event):
    global DataFrame
    selected_item = event.widget.get()
    print(f"Selected Item: {selected_item}")
    SelectedFrame = dp.leftSelect(DataFrame,selected_item)
    for widget in grade_scroll.winfo_children():
        widget.destroy()
    for index, row in SelectedFrame.iterrows():
       #Order DataFrame so information shows A's first, B's Second, and so on
       #Try to figure out how scrolling works and stop the window from resizing when information is supplied
       f_names = Label(right_grades, text=row["First Name"], font = ("Times New Roman", 15), bg="#a5a8a6", fg="#000000", width = 17)
       f_names.grid(row=index, column=0,columnspan=2, sticky="wens")
       f_names.bind('<Double-1>', _clipboard_copy(f_names))
       f_names.bind('<Enter>', lambda ev, lab=f_names: lab.config(fg='white'))
       f_names.bind('<Leave>', lambda ev, lab=f_names: lab.config(fg='black'))
       l_names = Label(right_grades, text=row["Last Name"], font = ("Times New Roman", 15), bg="#a5a8a6", fg="#000000", width = 17)
       l_names.grid(row=index, column=3,columnspan=2, sticky="wens")
       l_names.bind('<Double-1>', _clipboard_copy(l_names))
       l_names.bind('<Enter>', lambda ev, lab=l_names: lab.config(fg='white'))
       l_names.bind('<Leave>', lambda ev, lab=l_names: lab.config(fg='black'))
       color = dp.gradeColor(row["Grade"])
       stu_grades = Label(right_grades, text=row["Grade"], font = ("Times New Roman", 15), bg = color, fg="#000000", width = 17)
       stu_grades.grid(row=index, column=7,columnspan=2, sticky="wens")
       stu_grades.bind('<Double-1>', _clipboard_copy(stu_grades))
       stu_grades.bind('<Enter>', lambda ev, lab=stu_grades: lab.config(fg='white'))
       stu_grades.bind('<Leave>', lambda ev, lab=stu_grades: lab.config(fg='black'))
       stu_IDs = Label(right_grades, text=row["Student ID"], font = ("Times New Roman", 15), bg="#a5a8a6", fg="#000000", width = 17)
       stu_IDs.grid(row=index, column=5,columnspan=2, sticky="wens")
       stu_IDs.bind('<Double-1>', _clipboard_copy(stu_IDs))
       stu_IDs.bind('<Enter>', lambda ev, lab=stu_IDs: lab.config(fg='white'))
       stu_IDs.bind('<Leave>', lambda ev, lab=stu_IDs: lab.config(fg='black'))

def _clipboard_copy(inst):
    def wrapper(event):
        inst.clipboard_clear()
        inst.clipboard_append(inst['text'])
    return wrapper       
                


root.mainloop()