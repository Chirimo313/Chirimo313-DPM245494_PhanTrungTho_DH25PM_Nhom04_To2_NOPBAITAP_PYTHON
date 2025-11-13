'''
| Chiều cao (cm) | Cân nặng (kg) |
| -------------- | ------------- |
| 147            | 49            |
| 150            | 50            |
| 153            | 51            |
| 158            | 54            |
| 163            | 58            |
| 165            | 59            |
| 168            | 60            |
| 170            | 62            |
| 173            | 63            |
| 175            | 64            |
| 178            | 66            |
| 180            | 67            |
| 183            | 68            |

'''
import numpy as np
from sklearn.linear_model import LinearRegression

# Dữ liệu chiều cao (cm) và cân nặng (kg)
X = np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T
y = np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])

# Khởi tạo mô hình hồi quy tuyến tính
regr = LinearRegression()

# Huấn luyện mô hình
regr.fit(X, y)

# In hệ số hồi quy và intercept
print("Slope (w1):", regr.coef_[0])
print("Intercept (w0):", regr.intercept_)

# Nhập chiều cao từ người dùng
yourHeight = int(input("Input your height (cm): "))

# Dự đoán cân nặng
yourWeight = regr.coef_[0] * yourHeight + regr.intercept_
print(f"Your height is {yourHeight} cm, I predict your weight is {yourWeight:.2f} kg")


