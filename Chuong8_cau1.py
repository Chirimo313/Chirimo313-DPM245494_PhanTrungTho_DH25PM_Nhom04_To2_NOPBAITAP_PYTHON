from tkinter import *

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    if a == 0 and b == 0:
        stringKQ.set("Vô số nghiệm")
    elif a == 0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x = " + str(-b / a))

root = Tk()
root.title("Giải phương trình bậc 1")
root.geometry("300x180")

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

Label(root, text="Phương trình bậc 1", fg="red", font=("Tahoma", 14)).grid(row=0, columnspan=2)
Label(root, text="Hệ số a:").grid(row=1, column=0)
Entry(root, textvariable=stringHSA).grid(row=1, column=1)
Label(root, text="Hệ số b:").grid(row=2, column=0)
Entry(root, textvariable=stringHSB).grid(row=2, column=1)

frame = Frame(root)
Button(frame, text="Giải", command=giaiAction).pack(side=LEFT, padx=5)
Button(frame, text="Tiếp", command=tiepAction).pack(side=LEFT, padx=5)
Button(frame, text="Thoát", command=root.quit).pack(side=LEFT, padx=5)
frame.grid(row=3, columnspan=2, pady=5)

Label(root, text="Kết quả:").grid(row=4, column=0)
Entry(root, textvariable=stringKQ).grid(row=4, column=1)

root.mainloop()
