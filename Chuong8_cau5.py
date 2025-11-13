from tkinter import *
from tkinter import messagebox

def login():
    user = username.get()
    pw = password.get()
    if user == "admin" and pw == "123":
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

root = Tk()
root.title("Đăng nhập hệ thống")
root.geometry("300x180")

username = StringVar()
password = StringVar()

Label(root, text="Đăng Nhập", fg="blue", font=("Tahoma", 16)).pack(pady=5)
Label(root, text="Tên đăng nhập:").pack()
Entry(root, textvariable=username).pack()
Label(root, text="Mật khẩu:").pack()
Entry(root, textvariable=password, show="*").pack()

Button(root, text="Đăng nhập", command=login).pack(pady=10)
Button(root, text="Thoát", command=root.quit).pack()

root.mainloop()
