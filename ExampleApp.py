import tkinter as tk
from tkinter import filedialog
import pandas as pd
import FileReading as fr
import DataProcessing as dp

# Create the Tkinter window
window = tk.Tk()
window.title("Select a .run file")
window.geometry("1500x1500")


# Function to browse for a file and display its directory path
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a .run file", filetypes=[("RUN Files", "*.run")])
    txt_directory.delete(1.0, tk.END)
    txt_directory.insert(tk.END, file_path)
    FileReader = fr.FileReading(file_path)
    DataFrame = FileReader.openFile()
    DataFrame = dp.letterTogpa(DataFrame)

    # Create a Pandas DataFrame from the selected file
    df = DataFrame

    # Display the DataFrame in a grid
    for index, row in df.iterrows():
        tk.Label(window, text=row["Group"]).grid(row=index+3, column=0)
        tk.Label(window, text=row["Section"]).grid(row=index+3, column=1)
        tk.Label(window, text=row["First Name"]).grid(row=index+3, column=2)
        tk.Label(window, text=row["Last Name"]).grid(row=index+3, column=3)
        tk.Label(window, text=row["Student ID"]).grid(row=index+3, column=4)

# Create a label and a text box to display the selected file directory path
lbl_directory = tk.Label(window, text="Selected file directory:")
lbl_directory.grid(row=0, column=0)
txt_directory = tk.Text(window, height=1, width=100)
txt_directory.grid(row=0, column=1)

# Create a button to browse for a file
btn_browse = tk.Button(window, text="Browse", command=browse_file)
btn_browse.grid(row=1, column=0)

# Create labels for the DataFrame grid
tk.Label(window, text="Group", width= 10).grid(row=2, column=0)
tk.Label(window, text="Section", width= 10).grid(row=2, column=1)
tk.Label(window, text="First Name", width= 10).grid(row=2, column=2)
tk.Label(window, text="Last Name", width= 10).grid(row=2, column=3)
tk.Label(window, text="Student ID", width= 10).grid(row=2, column=4)

# Start the Tkinter event loop
window.mainloop()