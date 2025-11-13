# XuLyFile.py
def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data + "\n")

def DocFile(path):
    ds = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            arr = line.strip().split(';')
            ds.append(arr)
    return ds

def GhiDeFile(path, ds):
    with open(path, 'w', encoding='utf-8') as f:
        for item in ds:
            f.write(';'.join(item) + "\n")


from XuLyFile import *

path = "sanpham.txt"

def them():
    ma = input("Nhập mã SP: ")
    ten = input("Nhập tên SP: ")
    gia = input("Nhập đơn giá: ")
    madm = input("Nhập mã danh mục: ")
    line = f"{ma};{ten};{gia};{madm}"
    LuuFile(path, line)
    print("Đã thêm sản phẩm.")

def xem():
    ds = DocFile(path)
    print("Mã\tTên\tĐơn giá\tDanh mục")
    for sp in ds:
        print('\t'.join(sp))

def timkiem():
    tu = input("Nhập từ khóa tìm: ")
    ds = DocFile(path)
    for sp in ds:
        if tu.lower() in sp[1].lower():
            print('\t'.join(sp))

def xoa():
    ma = input("Nhập mã SP cần xóa: ")
    ds = DocFile(path)
    ds = [sp for sp in ds if sp[0] != ma]
    GhiDeFile(path, ds)
    print(" Đã xóa sản phẩm.")

def sapxep():
    ds = DocFile(path)
    ds.sort(key=lambda x: float(x[2]))
    GhiDeFile(path, ds)
    print(" Đã sắp xếp theo đơn giá tăng dần.")

while True:
    print("\n----- MENU -----")
    print("1. Thêm SP")
    print("2. Xem DS")
    print("3. Tìm kiếm")
    print("4. Xóa SP")
    print("5. Sắp xếp theo giá")
    print("0. Thoát")
    chon = input("Chọn: ")

    if chon == '1': them()
    elif chon == '2': xem()
    elif chon == '3': timkiem()
    elif chon == '4': xoa()
    elif chon == '5': sapxep()
    elif chon == '0': break

