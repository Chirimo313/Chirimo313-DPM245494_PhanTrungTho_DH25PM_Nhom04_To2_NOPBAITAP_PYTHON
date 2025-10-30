'''
Yêu cầu: Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression (a) x == 3 (b) x < y (c) x >= y (d) x <= y (e) x != y - 2 (f) x < 10 (g) x >= 0 and x < 10 (h) x < 0 and x < 10 (i) x >= 0 and x < 2 (j) x < 0 or x < 10 (k) x > 0 or x < 10 (l) x < 0 or x > 10
                                                                      "Bai lam"
                                                                      | Biểu thức             | Kết quả | Giải thích         |
    | --------------------- | ------- | ------------------ |
    | (a) x == 3            | ✅ True  | 3 == 3             |
    | (b) x < y             | ✅ True  | 3 < 5              |
    | (c) x >= y            | ❌ False | 3 < 5              |
    | (d) x <= y            | ✅ True  | 3 ≤ 5              |
    | (e) x != y - 2        | ❌ False | y - 2 = 3 → 3 != 3 |
    |   (f) x < 10            | ✅ True  | 3 < 10           |
    | (g) x >= 0 and x < 10 | ✅ True  | cả hai điều đúng   |
    | (h) x < 0 and x < 10  | ❌ False | x < 0 sai          |
    | (i) x >= 0 and x < 2  | ❌ False | 3 < 2 sai          |
    | (j) x < 0 or x < 10   | ✅ True  | 3 < 10 đúng        |
    | (k) x > 0 or x < 10   | ✅ True  | 3 > 0 đúng         |
    | (l) x < 0 or x > 10   | ❌ False | cả hai điều sai    |

'''
