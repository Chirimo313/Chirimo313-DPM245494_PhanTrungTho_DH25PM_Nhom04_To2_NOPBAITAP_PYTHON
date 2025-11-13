from tkinter import *
from math import sqrt

def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())
    if a == 0:
        if b == 0 and c == 0:
            stringKQ.set("Vô số nghiệm")
        elif b == 0:
            stringKQ.set("Vô nghiệm")
        else:
            stringKQ.set("x = " + str(-c / b))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            stringKQ.set("Vô nghiệm")
        elif delta == 0:
            stringKQ.set("x1 = x2 = " + str(-b / (2*a)))
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            stringKQ.set("x1 = %.2f; x2 = %.2f" % (x1, x2))

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

root = Tk()
root.title("Giải phương trình bậc 2")
root.geometry("320x220")

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

Label(root, text="Phương trình bậc 2", fg="red", font=("Tahoma", 14)).grid(row=0, columnspan=2)
Label(root, text="Hệ số a:").grid(row=1, column=0)
Entry(root, textvariable=stringHSA).grid(row=1, column=1)
Label(root, text="Hệ số b:").grid(row=2, column=0)
Entry(root, textvariable=stringHSB).grid(row=2, column=1)
Label(root, text="Hệ số c:").grid(row=3, column=0)
Entry(root, textvariable=stringHSC).grid(row=3, column=1)

frame = Frame(root)
Button(frame, text="Giải", command=giaiAction).pack(side=LEFT, padx=5)
Button(frame, text="Tiếp", command=tiepAction).pack(side=LEFT, padx=5)
Button(frame, text="Thoát", command=root.quit).pack(side=LEFT, padx=5)
frame.grid(row=4, columnspan=2, pady=5)

Label(root, text="Kết quả:").grid(row=5, column=0)
Entry(root, textvariable=stringKQ).grid(row=5, column=1)

root.mainloop()
