def ROI(doanh_thu, chi_phi):
    return (doanh_thu - chi_phi) / chi_phi

def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

print("Chương trình tính ROI (Return on Investment)")
dt = float(input("Nhập doanh thu: "))
cp = float(input("Nhập chi phí: "))

roi = ROI(dt, cp)
print("Tỉ lệ ROI =", roi)
print("=>", GoiYDauTu(roi))
