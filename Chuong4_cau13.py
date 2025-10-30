def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_hoan_thien(n):
    return tong_uoc(n) == n

def la_thinh_vuong(n):
    return tong_uoc(n) > n

n = int(input("Nhập số nguyên dương n: "))
if la_hoan_thien(n):
    print(n, "là số hoàn thiện")
elif la_thinh_vuong(n):
    print(n, "là số thịnh vượng")
else:
    print(n, "không phải số hoàn thiện hoặc thịnh vượng")
