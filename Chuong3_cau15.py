"""
Yêu cầu: (a) range(5) (b) range(5, 10) (c) range(5, 20, 3) (d) range(20, 5, -1) (e) range(20, 5, -3) (f) range(10, 5) (g) range(0) (h) range(10, 101, 10) (i) range(10, -1, -1) (j) range(-3, 4) (k) range(0, 10, 1)

                    "Bai lam"
                    
| ------------------------ | --------------------------------------------- | ---------------------- |
| (a) `range(5)`           | Bắt đầu từ 0, kết thúc 4                      | 0, 1, 2, 3, 4          |
| (b) `range(5, 10)`       | Bắt đầu 5, kết thúc 9                         | 5, 6, 7, 8, 9          |
| (c) `range(5, 20, 3)`    | Tăng mỗi lần 3                                | 5, 8, 11, 14, 17       |
| (d) `range(20, 5, -1)`   | Giảm dần mỗi lần 1                            | 20, 19, 18, ..., 6     |
| (e) `range(20, 5, -3)`   | Giảm dần mỗi lần 3                            | 20, 17, 14, 11, 8      |
| (f) `range(10, 5)`       | Không chạy (vì tăng dương nhưng start > stop) | *rỗng*                 |
| (g) `range(0)`           | Không chạy                                    | *rỗng*                 |
| (h) `range(10, 101, 10)` | Bắt đầu 10, tăng 10                           | 10, 20, 30, …, 100     |
| (i) `range(10, -1, -1)`  | Giảm dần 1                                    | 10, 9, 8, …, 0         |
| (j) `range(-3, 4)`       | Tăng dần 1                                    | -3, -2, -1, 0, 1, 2, 3 |
| (k) `range(0, 10, 1)`    | Tăng dần 1                                    | 0, 1, 2, …, 9          |
"""