from statistics import variance
import tkinter as tk
from tkinter import BUTT, StringVar, ttk
import ttkbootstrap as ttk


# window setup
window = ttk.Window(themename = 'yeti')
window.title("Buttons")
window.geometry("400x200")
# -------------------------------
# Basic Buttons -----------------
# function
def button_func():
    print("basic button clicked!")

button_string = StringVar(value = "Cklick!")
button = ttk.Button(window, text="A simple button", command=button_func, textvariable=button_string)
button.pack(pady=10)


# Basic Checkbutton -------------
# store value
check_var = ttk.IntVar(value = 10)  # for checked in dafault
check = ttk.Checkbutton(
    window, 
    text="checkbox 1", 
    command=lambda: print(f"checkbutton 1 clicked! Value: {check_var.get()}"),
    variable=check_var,
    onvalue= 10,
    offvalue= -10)
check.pack(pady=10)

# Radio buttons -----------------

radio_var = ttk.StringVar()
radio1 = ttk.Radiobutton(
    window, 
    text = "Radio Button 1", 
    value="radio1", 
    variable=radio_var, 
    command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text = "Radio Button 2", 
    value="radio2", 
    variable=radio_var, 
    command=lambda: print(radio_var.get()))
radio2.pack()


# -------------------------------
# root (update and event tracker)
window.mainloop()
