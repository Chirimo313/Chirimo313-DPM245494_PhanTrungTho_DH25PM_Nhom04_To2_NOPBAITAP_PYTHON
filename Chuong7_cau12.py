# quanly_csv.py
import csv, random

path = "dulieu.csv"

def luu_csv():
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):
            row = [random.randint(0, 100) for _ in range(10)]
            writer.writerow(row)
    print("✅ Đã tạo file CSV.")

def doc_csv():
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            nums = [int(x) for x in row]
            print(row, "→ Tổng =", sum(nums))

luu_csv()
doc_csv()
