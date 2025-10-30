done = False
while not done:
    n = int(input("Nhập số nguyên dương: "))
    if n < 0:
        done = True
    else:
        print("Bạn vừa nhập:", n)
print("Kết thúc chương trình")
