# XuLyFile.py
def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.writelines("\n")

def DocFile(path):
    arrSo = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            arr = data.split(',')
            arrSo.append(arr)
    return arrSo

# TestLuuFile.py
from XuLyFile import *

LuuFile("csdl_so.txt", "-5,4,7,9,3,20")
LuuFile("csdl_so.txt", "5,-4,37,-19,24,-21")
LuuFile("csdl_so.txt", "15,9,0,-38,-3,15")
LuuFile("csdl_so.txt", "5,-4,77,-9,3,-7")
LuuFile("csdl_so.txt", "55,44,27")
LuuFile("csdl_so.txt", "-50,26")

# TestDocFile.py
from XuLyFile import *

arrSo = DocFile("csdl_so.txt")
print(arrSo)

def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for element in row:
            number = int(element)
            if number < 0:
                print(number, end='\t')
        print()

print("Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)
