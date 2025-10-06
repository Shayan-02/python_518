from tkinter import *
from random import *


def showFullName():
    fullName = fent.get() + " " + lent.get()
    fullNamelbl.configure(text=fullName)


bg = "#123456"
font = ("vazir", 20, "bold")

root = Tk()
root.geometry("500x500")
root.configure(bg=bg)
root.title("fullname app")
root.resizable(0, 0)

flbl = Label(root, text="نام", font=font, bg=bg, fg="white").place(x=440, y=10)
fent = Entry(root, width=15)
fent.place(x=100, y=10)
llbl = Label(root, text="نام خانوادگی", font=font, bg=bg, fg="white").place(x=335, y=100)
lent = Entry(root, width=15)
lent.place(x=100, y=100)
fnbtn = Button(
    root, text="نمایش نام", bg="lightgreen", font=font, command=showFullName
).place(x=150, y=150)

fullNamelbl = Label(root, text="", font=font, bg=bg, fg="white", border=2)
fullNamelbl.place(x=10, y=10)


root.mainloop()
