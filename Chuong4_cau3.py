def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Hơi béo"
    elif bmi <= 34.9:
        return "Béo phì cấp độ 1"
    elif bmi <= 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"

height = float(input("Nhập chiều cao (m): "))
weight = float(input("Nhập cân nặng (kg): "))
bmi = BMI(height, weight)
print(f"BMI = {bmi:.2f}")
print("Phân loại:", PhanLoai(bmi))
print("Nguy cơ bệnh:", NguyCoBenh(bmi))
