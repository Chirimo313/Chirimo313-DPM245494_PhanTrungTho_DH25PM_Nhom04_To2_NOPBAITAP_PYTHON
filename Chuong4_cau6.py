
from random import randrange
randrange(0, 100)

"""
| Giá trị | Có thể xuất hiện? | Giải thích                                               |
| ------- | ----------------- | -------------------------------------------------------- |
| **4.5** | ❌ Không           | `randrange()` chỉ sinh **số nguyên**, không sinh số thực |
| **34**  | ✅ Có              | Là số nguyên trong khoảng [0, 99]                        |
| **-1**  | ❌ Không           | Nhỏ hơn 0 (ngoài phạm vi)                                |
| **100** | ❌ Không           | `stop=100` là **giới hạn trên**, không bao gồm           |
| **0**   | ✅ Có              | Bắt đầu từ 0                                             |
| **99**  | ✅ Có              | Là giá trị nguyên lớn nhất có thể được sinh ra           |

"""