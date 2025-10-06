from tkinter import *


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

flbl = Label(root, text="first name", font=font, bg=bg, fg="white").grid(row=0, column=0, padx=20)
fent = Entry(root, font=font)
fent.grid(row=0, column=1, pady=20)
llbl = Label(root, text="last name", font=font, bg=bg, fg="white").grid(row=1, column=0, padx=20)
lent = Entry(root, font=font)
lent.grid(row=1, column=1, pady=20)
fnbtn = Button(
    root, text="show fullname", bg="lightgreen", font=font, command=showFullName
).grid(row=2, column=1, pady=30)

fullNamelbl = Label(root, text="", font=font, bg=bg, fg="white", border=2)
fullNamelbl.grid(row=3, column=1)


root.mainloop()
