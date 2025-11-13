# quanlythietbi.py
from xml.dom.minidom import parse

def doc_nhom():
    DOMTree = parse("nhomthietbi.xml")
    root = DOMTree.documentElement
    nhoms = root.getElementsByTagName("nhom")
    ds = []
    for n in nhoms:
        ma = n.getElementsByTagName("ma")[0].childNodes[0].data
        ten = n.getElementsByTagName("ten")[0].childNodes[0].data
        ds.append({"ma": ma, "ten": ten})
    return ds

def doc_thietbi():
    DOMTree = parse("ThietBi.xml")
    root = DOMTree.documentElement
    tbs = root.getElementsByTagName("thietbi")
    ds = []
    for tb in tbs:
        manhom = tb.getAttribute("manhom")
        ma = tb.getElementsByTagName("ma")[0].childNodes[0].data
        ten = tb.getElementsByTagName("ten")[0].childNodes[0].data
        ds.append({"ma": ma, "ten": ten, "manhom": manhom})
    return ds

def loc_theo_nhom(ma_nhom):
    ds = doc_thietbi()
    for tb in ds:
        if tb["manhom"] == ma_nhom:
            print(tb)

def nhom_nhieu_tb():
    ds_tb = doc_thietbi()
    thongke = {}
    for tb in ds_tb:
        thongke[tb["manhom"]] = thongke.get(tb["manhom"], 0) + 1
    max_ma = max(thongke, key=thongke.get)
    print("✅ Nhóm có nhiều thiết bị nhất:", max_ma, "-", thongke[max_ma], "thiết bị")

print("Danh sách nhóm:", doc_nhom())
print("Danh sách thiết bị:", doc_thietbi())
loc_theo_nhom("n3")
nhom_nhieu_tb()
