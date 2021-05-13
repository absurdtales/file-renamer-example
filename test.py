from zipfile import ZipFile
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def unzip(file, destination):
    try:
        with ZipFile(root.zip_file, 'r') as zipped:
            zipped.extractall(root.destination)
    except:
        print("Error with zip file")

def rename(destination):
    for entry in os.listdir(root.destination):
        new_name = entry[9:]
        os.rename(f'{root.destination}/{entry}', f'{root.destination}/{new_name}')

def add_file(file, destination):
    for entry in os.listdir(root.destination):
        dash_index = entry.find("-")
        new_name = entry[:dash_index]
        shutil.copyfile(root.criteria, f'{root.destination}/{new_name} - criteria.docx')

def zipped_btn():
    root.zip_file = tk.filedialog.askopenfile(initialdir = ".").name
    print(root.zip_file)

def destination_btn():
    root.destination = tk.filedialog.askdirectory(initialdir= ".")
    print(root.destination)

def criteria_btn():
    root.criteria = tk.filedialog.askopenfilename(initialdir = ".")
    print(root.criteria)

def go_btn():
    unzip(root.zip_file, root.destination)
    rename(root.destination)
    add_file(root.criteria, root.destination)


# ------ Main Program ------
# Create Window
root = tk.Tk()
root.title("MBBC File Extracter")
root.geometry("640x480")

# Create elements
tk.Label(root, text="MBBC File Extracter").grid(row=0, column=0, columnspan=2)
# zipped folder picker
tk.Label(root, text="Zipped File Location").grid(row=1, column=0)
tk.Button(root, text="Select Folder", command=zipped_btn).grid(row=1, column=1)
# destination folder picker
tk.Label(root, text="Destination Folder").grid(row=2, column=0)
tk.Button(root, text="Select Folder", command=destination_btn).grid(row=2, column=1)
# criteria file picker
tk.Label(root, text="Criteria File").grid(row=3, column=0)
tk.Button(root, text="Select File", command=criteria_btn).grid(row=3, column=1)
# go button
tk.Button(root, text="Go!", padx=40, pady=20, command=go_btn).grid(row=4, column=0, columnspan=2)

# Global Variables

root.zip_file = ""
root.destination = ""
root.criteria = ""

# Main loop when the uh
root.mainloop()