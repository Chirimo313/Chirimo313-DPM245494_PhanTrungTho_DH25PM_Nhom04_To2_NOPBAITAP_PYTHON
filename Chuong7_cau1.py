# XuLyFile.py
def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.writelines("\n")

def DocFile(path):
    arrProduct = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            arr = data.split(';')
            arrProduct.append(arr)
    return arrProduct

# TestLuuFile.py
from XuLyFile import *

masp = input("Nhập mã SP:")
tensp = input("Nhập tên SP:")
dongia = float(input("Nhập giá:"))
line = masp + ";" + tensp + ";" + str(dongia)

LuuFile("database.txt", line)

# TestDocFile.py
from XuLyFile import *

dssp = DocFile("database.txt")

def XuatSanPham(dssp):
    for row in dssp:
        for element in row:
            print(element, end='\t')
        print()

def SortSp(dssp):
    dssp.sort(key=lambda x: float(x[2]), reverse=True)

# Xuất sản phẩm trước khi sắp xếp
XuatSanPham(dssp)

# Sắp xếp sản phẩm theo đơn giá giảm dần
SortSp(dssp)

print("Sản phẩm sau khi sắp xếp giá:")
XuatSanPham(dssp)
