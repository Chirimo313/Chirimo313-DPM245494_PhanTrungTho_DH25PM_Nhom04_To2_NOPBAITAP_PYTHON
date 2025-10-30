from math import sqrt

print("Tính độ dài đoạn AB")
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))

AB = sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print(f"Độ dài đoạn AB = {AB:.2f}")
