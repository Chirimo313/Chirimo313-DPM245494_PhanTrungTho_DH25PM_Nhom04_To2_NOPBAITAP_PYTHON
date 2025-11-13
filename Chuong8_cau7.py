from tkinter import *
import datetime
import lunardate  # cần cài: pip install lunardate

def convert():
    year = int(year_dl.get())
    lunar = lunardate.LunarDate.fromSolarDate(year, 1, 1)
    result.set(f"Năm âm lịch: {lunar.year}")

root = Tk()
root.title("Chuyển Dương lịch sang Âm lịch")
root.geometry("320x160")

year_dl = StringVar()
result = StringVar()

Label(root, text="Nhập năm Dương lịch:", font=("Arial", 12)).pack()
Entry(root, textvariable=year_dl, width=20).pack(pady=5)
Button(root, text="Chuyển đổi", command=convert).pack(pady=5)
Label(root, textvariable=result, fg="blue", font=("Arial", 12)).pack()

root.mainloop()
