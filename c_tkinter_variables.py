import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
    string_var.set("You've clicked the button man!")

# window setup
window = ttk.Window(themename = 'simplex')
window.title("Tkinter Variables")
window.geometry("400x200")
# -------------------------------
# Tkinter variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master=window, text="Hello!", textvariable=string_var)
label.pack(pady=10)

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack(pady=10)

button = ttk.Button(master=window, text="Click!", command = button_func)
button.pack()

# -------------------------------
# root (update and event tracker)
window.mainloop()
