from tkinter import *

root = Tk()
root.title("Máy tính bỏ túi")
root.geometry("320x400")

expression = StringVar()

# Hàm xử lý khi nhấn nút
def press(num):
    expression.set(expression.get() + str(num))

def clear():
    expression.set("")

def equal():
    try:
        result = eval(expression.get())
        expression.set(result)
    except:
        expression.set("Lỗi")

Entry(root, textvariable=expression, font=("Arial", 20), justify='right', bd=10).pack(fill=X, padx=5, pady=5)

frame = Frame(root)
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    rowFrame = Frame(frame)
    rowFrame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            Button(rowFrame, text=btn, font=("Arial", 18), command=equal).pack(side=LEFT, expand=True, fill="both")
        else:
            Button(rowFrame, text=btn, font=("Arial", 18), command=lambda x=btn: press(x)).pack(side=LEFT, expand=True, fill="both")

Button(root, text="C", font=("Arial", 18), bg="red", fg="white", command=clear).pack(fill=X, padx=5, pady=5)

root.mainloop()
