def LayTenFile(duongdan):
    return duongdan.split("\\")[-1]

def LayTenBaiHat(duongdan):
    tenfile = LayTenFile(duongdan)
    return tenfile.split(".")[0]

path = r"d:\music\muabui.mp3"
print("Tên file:", LayTenFile(path))
print("Tên bài hát:", LayTenBaiHat(path))
