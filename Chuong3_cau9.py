print("Chương trình xác định quý trong năm")
month = int(input("Nhập tháng (1–12): "))

if 1 <= month <= 3:
    print("Tháng", month, "thuộc quý I")
elif 4 <= month <= 6:
    print("Tháng", month, "thuộc quý II")
elif 7 <= month <= 9:
    print("Tháng", month, "thuộc quý III")
elif 10 <= month <= 12:
    print("Tháng", month, "thuộc quý IV")
else:
    print("Tháng không hợp lệ!")
