from random import choice
from tkinter import messagebox
f = open("./1.txt", encoding="utf-8")
valid = f.readlines()
for i in range(20):
    messagebox.showinfo("برنده", choice(valid))