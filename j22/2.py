from tkinter import messagebox

def withdraw(balance, amount):
    if balance < amount:
        messagebox.showerror("عدم موجودی","موجودی کافی نیست")
    else:
        messagebox.showinfo("برداشت موفق", f"برداشت با موفقیت انجام شد موجودی جدید {balance - amount} است")

withdraw(500, 100) # انجام شد 
withdraw(100, 500)