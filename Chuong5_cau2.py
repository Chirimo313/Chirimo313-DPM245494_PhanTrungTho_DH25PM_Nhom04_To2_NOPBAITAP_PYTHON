def ToiUuChuoi(s):
    s2 = s.strip()
    arr = s2.split(' ')
    s2 = ""
    for x in arr:
        if len(x.strip()) != 0:
            s2 += x + " "
    return s2.strip()

s = "    Trần     Duy     Thanh   "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))
