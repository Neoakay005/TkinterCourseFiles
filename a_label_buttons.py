import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
    print("Aaaaa")

# window setup
window = ttk.Window(themename = 'darkly')
window.title("Tkinter and Widgets")
window.geometry("800x600")
# -------------------------------

# header label
header_label = ttk.Label(master=window, text="Hallo There!", font="Calibri 16")
header_label.pack(pady=10)

# text area
text_area = tk.Text(master=window)
text_area.pack(pady=10)

# ttk entry
text_entry = ttk.Entry(master=window)
text_entry.pack(pady=10)

# ttk button
my_button = ttk.Button(master=window, text="My Button", command=button_func)
my_button.pack(pady=10)

# -------------------------------
# root (update and event tracker)
window.mainloop()
