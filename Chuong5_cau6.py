def NegativeNumberInStrings(s):
    kq = []
    i = 0
    while i < len(s):
        if s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            kq.append(int(s[i:j]))
            i = j
        else:
            i += 1
    return kq

chuoi = input("Nhập chuỗi: ")
print("Các số nguyên âm trong chuỗi là:", NegativeNumberInStrings(chuoi))
