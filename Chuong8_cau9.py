from tkinter import *
from tkinter import messagebox

def tinhBMI():
    try:
        h = float(height.get())
        w = float(weight.get())
        bmi = w / (h * h)
        if bmi < 18.5:
            status = "Gầy"
        elif bmi < 25:
            status = "Bình thường"
        elif bmi < 30:
            status = "Mập"
        else:
            status = "Béo phì"
        result.set(f"BMI = {round(bmi, 2)} ({status})")
    except:
        messagebox.showerror("Lỗi", "Nhập sai dữ liệu!")

root = Tk()
root.title("Tính chỉ số BMI")
root.geometry("300x220")

height = StringVar()
weight = StringVar()
result = StringVar()

Label(root, text="Tính BMI", fg="green", font=("Tahoma", 16)).pack(pady=5)
Label(root, text="Chiều cao (m):").pack()
Entry(root, textvariable=height).pack()
Label(root, text="Cân nặng (kg):").pack()
Entry(root, textvariable=weight).pack()
Button(root, text="Tính", command=tinhBMI).pack(pady=5)
Label(root, textvariable=result, fg="blue", font=("Arial", 12)).pack()

root.mainloop()
