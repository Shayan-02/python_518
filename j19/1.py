from tkinter import *


def showfull():
    fname = fent.get() + " " + eent.get()
    fnamelbl.configure(text=fname)


root = Tk()

fent = Entry(root, width=50)
fent.pack()

eent = Entry(root, width=50)
eent.pack()

btn = Button(root, text="click", command=showfull).pack()

fnamelbl = Label(root, text="")
fnamelbl.pack()

root.mainloop()
