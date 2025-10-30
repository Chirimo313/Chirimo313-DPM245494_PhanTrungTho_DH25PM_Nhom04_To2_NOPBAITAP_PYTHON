print("Chương trình tính S(x, n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!")

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

s = 0  
for i in range(n + 1):
    mu = 2 * i + 1  
    tu = x ** mu
    mau = 1
    for j in range(1, mu + 1):
        mau *= j
    s += tu / mau

print(f"S({x}, {n}) = {s}")