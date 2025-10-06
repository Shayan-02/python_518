from random import *
from tkinter import *

def generateRandomNumber():
    start = int(startent.get())
    end = int(endent.get())
    randomNumber = randint(start, end)
    randomNumberlbl.configure(text=f"random number : {randomNumber}")


root = Tk()

root.geometry("300x400")
root.resizable(0, 0)
font = ("arial", 20)


startlbl = Label(root, text="start range", font=font).pack()
startent= Entry(root, width=15, font=font)
startent.pack(pady=30)
endlbl = Label(root, text="end range", font=font).pack()
endent= Entry(root, width=15, font=font)
endent.pack(pady=30)
submitbtn = Button(root, text="random number", font=font, bg="pink", command=generateRandomNumber).pack()
randomNumberlbl = Label(root, text="", font=font)
randomNumberlbl.pack()

root.mainloop()
