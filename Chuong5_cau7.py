def ToiUuDanhTu(s):
    s = s.strip().lower()
    arr = s.split()
    s2 = ""
    for word in arr:
        s2 += word.capitalize() + " "
    return s2.strip()

s = "    TRần     duY    thAnH   "
print("Chuỗi tối ưu:", ToiUuDanhTu(s))
