import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import FileReading as fr
import DataProcessing as dp

# Create the Tkinter window
root = tk.Tk()
root.title("Testing")
root.config(bg="#3a383d")
#left_frame = tk.Frame(root,width=200, height = 400)
#left_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

left_frame = tk.Frame(root, width = 500, height = 750, bg = "#106d8f")
left_frame.grid(row=0,column=0,padx=10, pady=5)

left_select = tk.Frame(left_frame, width= 500, height = 100)
left_select.grid(row=0,column=0,padx=10, pady=5)

left_title = tk.Label(left_select, text = "Class Statistics",font = ("Times New Roman", 24), bg= "#626873")
left_title.grid(row=0, column=0,padx=1, pady=2)

n = tk.StringVar()
left_selection = ttk.Combobox(left_select,width=27,values=["This","Is","Just","A","Test"])
left_selection.grid(column=0,row=1)


left_statistics = tk.Frame(left_frame, width= 500, height = 650)
left_statistics.grid(row=1,column=0,padx=10, pady=5)


#------------------------------------------------------------------------------------------------------------------------------#

right_frame = tk.Frame(root, width=500, height = 750, bg = "#106d8f" )
right_frame.grid(row=0,column=1,padx=10, pady=5)

right_button = tk.Frame(right_frame, width= 500, height = 100, bg= "#626873")
right_button.grid(row=0,column=0,padx=10, pady=5)

right_title = tk.Label(right_button, text = "Class Statistics",font = ("Times New Roman", 24), bg= "#626873")
right_title.grid(row=0, column=0,padx=1, pady=2)

calc = tk.Button(right_button,text = "Change View",font = ("Times New Roman", 18), width = 35)
calc.grid(row=1,column=0,padx=1, pady=2)

right_grades = tk.Frame(right_frame, width= 500, height = 650)
right_grades.grid(row=1,column=0,padx=10, pady=5)




root.mainloop()