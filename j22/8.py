import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# Functions
def c_to_f():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        result_label.configure(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")


def f_to_c():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        result_label.configure(text=f"{celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")


# Main window
root = ctk.CTk()
root.title("Temperature Converter")
root.geometry("300x200")

# Entry
entry = ctk.CTkEntry(root, width=200, placeholder_text="Enter temperature")
entry.pack(pady=20)

# Buttons (circular style)
btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=10)

c_to_f_btn = ctk.CTkButton(
    btn_frame, text="C → F", width=80, height=80, corner_radius=40, command=c_to_f
)
c_to_f_btn.grid(row=0, column=0, padx=10)

f_to_c_btn = ctk.CTkButton(
    btn_frame, text="F → C", width=80, height=80, corner_radius=40, command=f_to_c
)
f_to_c_btn.grid(row=0, column=1, padx=10)

# Result label
result_label = ctk.CTkLabel(root, text="Result:", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
