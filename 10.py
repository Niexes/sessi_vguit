import tkinter as tk
from tkinter import ttk

def addition():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Неверный ввод")

def subtraction():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Неверный ввод")

def multiplication():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Неверный ввод")

def division():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 == 0:
            result_label.config(text="Не могу выполнять действия с 0")
        else:
            result = num1 / num2
            result_label.config(text=result)
    except ValueError:
        result_label.config(text="Неверный ввод")

def checkbox_selection():
    selected = []
    if checkbox1.get():
        selected.append("Option 1")
    if checkbox2.get():
        selected.append("Option 2")
    if checkbox3.get():
        selected.append("Option 3")
    selection_label.config(text=selected)

def load_text():
    file = open(file_path_entry.get(), "r")
    content = file.read()
    text_label.config(text=content)
    file.close()


root = tk.Tk()
root.title("Жилякова Анна")


notebook = ttk.Notebook(root)
notebook.pack()


calculator_tab = ttk.Frame(notebook)
notebook.add(calculator_tab, text="Calculator")


checkbox_tab = ttk.Frame(notebook)
notebook.add(checkbox_tab, text="Checkboxes")


text_tab = ttk.Frame(notebook)
notebook.add(text_tab, text="Text")

num1_label = ttk.Label(calculator_tab, text="Number 1:")
num1_label.grid(row=0, column=0, padx=10, pady=10)

num1_entry = ttk.Entry(calculator_tab)
num1_entry.grid(row=0, column=1, padx=10, pady=10)

num2_label = ttk.Label(calculator_tab, text="Number 2:")
num2_label.grid(row=0, column=0, padx=10, pady=10)

num2_entry = ttk.Entry(calculator_tab)
num2_entry.grid(row=0, column=1, padx=10, pady=10)








#-------------------------------------------------------------------