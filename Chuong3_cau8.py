print("Chương trình tính toán đơn giản")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == '+':
    print("Kết quả:", a + b)
elif op == '-':
    print("Kết quả:", a - b)
elif op == '*':
    print("Kết quả:", a * b)
elif op == '/':
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ!")
