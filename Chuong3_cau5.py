i = int(input("Nhập i: "))
j = int(input("Nhập j: "))
k = int(input("Nhập k: "))

if i < j:
    if j < k:
        print("i < j < k")
    else:
        print("i < j and j >= k")
else:
    print("i >= j")
