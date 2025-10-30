from math import log

a = float(input("Nhập cơ số a (>0, ≠1): "))
x = float(input("Nhập số x (>0): "))

if a <= 0 or a == 1 or x <= 0:
    print("Giá trị không hợp lệ!")
else:
    kq = log(x) / log(a)
    print(f"log_{a}({x}) = {kq}")
