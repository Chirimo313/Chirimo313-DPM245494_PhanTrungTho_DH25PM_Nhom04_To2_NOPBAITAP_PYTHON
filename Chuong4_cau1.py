from math import sqrt

def dien_tich_tam_giac(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0) or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Tam giác không hợp lệ"
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s

print("Chương trình tính diện tích Tam Giác")
a = float(input("Nhập cạnh a > 0: "))
b = float(input("Nhập cạnh b > 0: "))
c = float(input("Nhập cạnh c > 0: "))

kq = dien_tich_tam_giac(a, b, c)
print("Diện tích =", kq)
