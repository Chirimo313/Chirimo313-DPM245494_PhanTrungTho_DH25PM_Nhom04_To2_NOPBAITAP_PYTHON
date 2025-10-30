s = input("Nhập chuỗi: ")
nguyen_am = "aeiouAEIOU"
phu_am = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

hoa = thuong = so = dacbiet = khoang = nguyenam = phuam = 0

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch.isspace():
        khoang += 1
    else:
        dacbiet += 1

    if ch in nguyen_am:
        nguyenam += 1
    elif ch in phu_am:
        phuam += 1

print("Chữ IN HOA:", hoa)
print("Chữ in thường:", thuong)
print("Chữ số:", so)
print("Ký tự đặc biệt:", dacbiet)
print("Khoảng trắng:", khoang)
print("Nguyên âm:", nguyenam)
print("Phụ âm:", phuam)
