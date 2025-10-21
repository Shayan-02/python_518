from tkinter import *

class Todo(Tk):
    def __init__(self):
        super().__init__()
        self.title("Todo app")
        self.geometry("300x350")
        
        # gettin task
        self.task_entry=Entry(self, width=18 )
        self.task_entry.place(x=20, y=10)
        # button for add your task in the listbox
        self.btn_add=Button(self, text="add", command= self.add_task, width=20, bg="blue", fg="white")
        self.btn_add.place(x=150, y=5)
        # button for delete that option that you select it
        self.btn_delete_task=Button(self, text="delete", command= self.clear, width=10, bg="crimson", fg="white")
        self.btn_delete_task.place(x=50, y=40)
        # button for delete all tasks
        self.btn_delete_all=Button(self, text="delete all", command= self.clear_all , width=10, bg="crimson", fg="white")
        self.btn_delete_all.place(x=150, y=40)
        
        self.lstbox=Listbox(self , font=("Arial",12), width=30, height=10)
        self.lstbox.place(x=10, y=80)
        
    def add_task(self):
        """it is a function that takes task 
        of entry and put it in the list box
        """
        current=self.task_entry.get()
        self.task_entry.delete(0 ,END)
        self.lstbox.insert(0, current)
    def clear(self):
        """this function delete 
        that option you select it 
        """
        self.index=self.lstbox.curselection()
        if self.index !=():
            self.lstbox.delete(self.index)
    def clear_all(self):
        """it is a function that 
        delete all things in list box
        """
        self.lstbox.delete(0,END)

todo=Todo()
todo.mainloop()