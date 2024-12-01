import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# window setup
window = ttk.Window(themename = 'darkly')
window.title("Buttons, Functions an Arguments")
window.geometry("400x200")
# -------------------------------
# Basic Buttons -----------------
# function
def button_func(entry_string):
    print("basic button clicked!")
    print(entry_string.get())

""" usable if you dont want to use the lambda expression
def outher_func(parameter):
    def inner_func():
        print("a button was pressed")
        print(parameter.get())
    return inner_func
"""

entry_string = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(
    window, 
    text="Button", 
    command=lambda: button_func(entry_string))
button.pack()

# -------------------------------
# root (update and event tracker)
window.mainloop()
