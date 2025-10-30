print("Chương trình đọc số có tối đa 2 chữ số")
n = int(input("Nhập số n (0 ≤ n ≤ 99): "))

don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
        "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

if n < 0 or n > 99:
    print("Số không hợp lệ")
elif n < 10:
    print(don_vi[n].capitalize())
else:
    hang_chuc = n // 10
    hang_dv = n % 10
    doc = chuc[hang_chuc]
    if hang_dv == 0:
        pass
    elif hang_dv == 1 and hang_chuc > 1:
        doc += " mốt"
    elif hang_dv == 5 and hang_chuc >= 1:
        doc += " lăm"
    else:
        doc += " " + don_vi[hang_dv]
    print(doc.capitalize())