from tkinter import *

def convert():
    f = float(f_value.get())
    c = (f - 32) * 5/9
    result.set(f"{round(c,2)} °C")

root = Tk()
root.title("Đổi độ F sang độ C")
root.geometry("280x150")

f_value = StringVar()
result = StringVar()

Label(root, text="Nhập độ F:").pack()
Entry(root, textvariable=f_value).pack()
Button(root, text="Chuyển đổi", command=convert).pack(pady=5)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
