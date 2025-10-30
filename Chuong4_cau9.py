from math import sqrt

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

s = 0
for i in range(n):
    s = sqrt(x + s)

print(f"Kết quả S = {s}")
