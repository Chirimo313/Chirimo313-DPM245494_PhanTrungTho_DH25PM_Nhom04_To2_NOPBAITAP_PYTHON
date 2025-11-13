from tkinter import *

def congAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a + b)

def truAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a - b)

def nhanAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a * b)

def chiaAction():
    a = float(stringA.get())
    b = float(stringB.get())
    if b == 0:
        stringKQ.set("Không chia được cho 0")
    else:
        stringKQ.set(a / b)

root = Tk()
root.title("Cộng Trừ Nhân Chia")
root.geometry("300x200")

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

Label(root, text="Cộng Trừ Nhân Chia", fg="blue", font=("Tahoma", 16)).grid(row=0, columnspan=3)
Label(root, text="Số a:").grid(row=1, column=1)
Entry(root, textvariable=stringA).grid(row=1, column=2)
Label(root, text="Số b:").grid(row=2, column=1)
Entry(root, textvariable=stringB).grid(row=2, column=2)
Label(root, text="Kết quả:").grid(row=3, column=1)
Entry(root, textvariable=stringKQ).grid(row=3, column=2)

frame = Frame(root)
Button(frame, text="Cộng", command=congAction).pack(fill=X)
Button(frame, text="Trừ", command=truAction).pack(fill=X)
Button(frame, text="Nhân", command=nhanAction).pack(fill=X)
Button(frame, text="Chia", command=chiaAction).pack(fill=X)
frame.grid(row=1, column=0, rowspan=4, padx=10)

Button(root, text="Thoát", command=root.quit).grid(row=4, column=2, pady=5)

root.mainloop()
