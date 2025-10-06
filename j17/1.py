from tkinter import *
from random import *

def showFullName():
    fullName = fent.get() + " " + lent.get()
    fullNamelbl.configure(text=fullName)

bg = "#123456"
font = ("vazir", 20, "bold")

root = Tk()
root.geometry("450x500")
root.configure(bg=bg)
root.title("fullname app")
root.resizable(0, 0)

flbl = Label(root, text="نام", font=font, bg=bg, fg="white").pack()
fent = Entry(root, font=font)
fent.pack(pady=20)
llbl = Label(root, text="نام خانوادگی", font=font, bg=bg, fg="white").pack()
lent = Entry(root, font=font)
lent.pack(pady=20)
fnbtn = Button(root, text="نمایش نام", bg="lightgreen", font=font, command=showFullName).pack(pady=20)

fullNamelbl = Label(root, text="", font=font, bg=bg, fg="white", border=2)
fullNamelbl.pack()


root.mainloop()
