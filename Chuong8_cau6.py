from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Các loại Button Style")
root.geometry("300x250")

styles = ['default', 'primary', 'danger', 'success', 'info', 'warning']

Label(root, text="Các loại Button Style", fg="blue", font=("Tahoma", 14)).pack(pady=10)

for s in styles:
    ttk.Button(root, text=f"Nút {s}", style=f"{s}.TButton").pack(pady=5, padx=10, fill=X)

root.mainloop()
