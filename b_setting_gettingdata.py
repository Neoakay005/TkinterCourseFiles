import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
    # get content of the entry
    print(f"{text_area.get()} Halil!")
    # update a label
    """
    header_label.config(text = "Changed Header") / 1st way
    header_label["text"] = "Changed Header" / 2nd way
    """
    header_label["text"] = text_area.get()
    # after an input diable the entry widget
    text_area["state"] = "disabled"

def button_able():
    text_area["state"] = "abled"

# window setup
window = ttk.Window(themename = 'solar')
window.title("Getting and Setting Widgets")
window.geometry("800x600")
# -------------------------------

# header label
header_label = ttk.Label(master=window, text="Hallo There!", font="Calibri 16")
header_label.pack(pady=10)

# text area
text_area = ttk.Entry(master=window)
text_area.pack(pady=10)

# button
my_button = ttk.Button(master=window, text="Click!", command=button_func)
my_button.pack(pady=10)

text_able_button = ttk.Button(master=window, text="Activate Text", command=button_able)
text_able_button.pack(pady=10)


# -------------------------------
# root (update and event tracker)
window.mainloop()
