import random
import tkinter as tk
from tkinter.ttk import *
def generate_pass():
    entry.delete(0, tk.END)
    try:
        length = int(entry1.get())
    except ValueError:
        entry.insert(0, "Invalid length")
        return

    if length <= 0:
        entry.insert(0, "Invalid length")
        return

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789!@#$%^&*()"
    alphanumeric= lower+upper+digits


    password = []
    for i in range(length):
        password=random.choice(alphanumeric)

        entry.insert(0,''.join (password))


root = tk.Tk()
root.title("Password Generator")
root.config(bg='black')



lb = Label(root, text="Generate Password")
lb.grid(row=0, column=1)

Random_password = Label(root, text="Password")
Random_password.grid(row=1)

entry = Entry(root)
entry.grid(row=1, column=1)

label = Label(root, text="Length")
label.grid(row=2)

button = Button(root, text="Generate", command=generate_pass)
button.grid(row=6, column=1)

entry1 = Entry(root)
entry1.grid(column=1, row=2)
root.mainloop()

