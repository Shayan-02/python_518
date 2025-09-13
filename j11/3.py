from tkinter import *
from turtle import color

root = Tk()

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
# lst1 = [1, 2, ,3, 4, 5, 6, 7, 8, 9, 10]

# lst1 += lst2
# lst1.append(lst2)
# for i in lst2:
#     lst1.append(i)
# lst1.extend(lst2)

for i in lst2[::-1]:
    lst1.insert(5, i)

l1 = Label(root, text=lst1, fg="red", font=("vazir", 20, "bold"), bg="lightblue").pack()
root.mainloop()
