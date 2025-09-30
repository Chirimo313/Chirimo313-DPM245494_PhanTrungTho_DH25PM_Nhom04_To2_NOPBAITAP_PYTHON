#Câu 9: Giải thích kết quả tính toán của các biểu thức
'''
Yêu cầu:
Cho các biến với giá trị
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

'''
# Khai báo biến
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

# Danh sách biểu thức và kết quả
expressions = [
    ("(a) i1 + (i2 * i3)",       i1 + (i2 * i3)),
    ("(b) i1 * (i2 + i3)",       i1 * (i2 + i3)),
    ("(c) i1 / (i2 + i3)",       i1 / (i2 + i3)),
    ("(d) i1 // (i2 + i3)",      i1 // (i2 + i3)),
    ("(e) i1 / i2 + i3",         i1 / i2 + i3),
    ("(f) i1 // i2 + i3",        i1 // i2 + i3),
    ("(g) 3 + 4 + 5 / 3",        3 + 4 + 5 / 3),
    ("(h) 3 + 4 + 5 // 3",       3 + 4 + 5 // 3),
    ("(i) (3 + 4 + 5) / 3",      (3 + 4 + 5) / 3),
    ("(j) (3 + 4 + 5) // 3",     (3 + 4 + 5) // 3),
    ("(k) d1 + (d2 * d3)",       d1 + (d2 * d3)),
    ("(l) d1 + d2 * d3",         d1 + d2 * d3),
    ("(m) d1 / d2 - d3",         d1 / d2 - d3),
    ("(n) d1 / (d2 - d3)",       d1 / (d2 - d3)),
    ("(o) d1 + d2 + d3 / 3",     d1 + d2 + d3 / 3),
    ("(p) (d1 + d2 + d3) / 3",   (d1 + d2 + d3) / 3),
    ("(q) d1 + d2 + (d3 / 3)",   d1 + d2 + (d3 / 3)),
    ("(r) 3 * (d1 + d2) * (d1 - d3)", 3 * (d1 + d2) * (d1 - d3)),
]

# In bảng kết quả
print(f"{'Biểu thức':<35} {'Kết quả':<15} {'Kiểu dữ liệu'}")
print("-" * 65)
for label, result in expressions:
    print(f"{label:<35} {result:<15} {type(result).__name__}")
