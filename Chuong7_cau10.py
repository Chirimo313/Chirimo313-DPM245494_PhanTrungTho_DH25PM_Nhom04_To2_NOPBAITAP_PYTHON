# quanlysinhvien.py
import json

path = "sinhvien.json"

def doc():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def luu(data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def them():
    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    ns = int(input("Năm sinh: "))
    lop = input("Mã lớp: ")
    ds = doc()
    ds.append({"ma": ma, "ten": ten, "namsinh": ns, "malop": lop})
    luu(ds)
    print(" Đã thêm SV")

def xem():
    for sv in doc():
        print(sv)

def tim():
    tu = input("Từ khóa: ")
    for sv in doc():
        if tu.lower() in sv["ten"].lower():
            print(sv)

def sapxep():
    ds = sorted(doc(), key=lambda x: x["namsinh"])
    luu(ds)
    print("Đã sắp xếp theo năm sinh")

while True:
    print("\n1.Thêm  2.Xem  3.Tìm  4.Sắp xếp  0.Thoát")
    c = input("Chọn: ")
    if c == '1': them()
    elif c == '2': xem()
    elif c == '3': tim()
    elif c == '4': sapxep()
    elif c == '0': break
