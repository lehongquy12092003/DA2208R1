from __future__ import division, print_function, unicode_literals
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn import linear_model

# TV: chi phí quảng cáo qua truyền hình (đơn vị nghìn USD)
# Radio: chi phí quảng cáo qua radio (đơn vị nghìn USD)
# Newspaper: chi phí quảng cáo qua báo chí (đơn vị nghìn USD)
# Sales: số sản phẩm bán được (đơn vị nghìn)
# Sử dụng pandas để đọc dữ liệu
df = pd.read_csv("advertising.csv")
print(df.head())
# Sử dụng dụng biểu đồ scatter để trực quan hóa mối quan hệ giữa lượng sản phẩm bán ra và chi phí quảng cáo từng loại hình.
# plt.scatter(df["Sales"],df["Newspaper"])
# plt.xlabel("Sales")
# plt.ylabel("Newspaper")
# plt.show()

# plt.scatter(df["Sales"],df["Radio"])
# plt.xlabel("Sales")
# plt.ylabel("Radio")
# plt.show()

# plt.scatter(df["Sales"],df["TV"])
# plt.xlabel("Sales")
# plt.ylabel("TV")
# plt.show()
# Sử dụng train_test_split() để chia dữ liệu thành dữ liệu huấn luyện và dữ liệu kiểm tra.
print(df.info())
print(df.shape)
x = df[["Newspaper","Radio","Sales"]]
y = df["Sales"]
X_train, X_test,y_train, y_test= train_test_split(x,y,test_size=0.3,random_state=42)
## Huấn luyện mô hình
#Create a regressor object
LR= LinearRegression()

#Fit training set to the regressor
LR.fit(X_train,y_train)

print("Mô hình hồi quy tuyến tính đã được huấn luyện, có các tham số:")
print("Intercept =", LR.intercept_) # Độ chặn 
print("Coefficients:", LR.coef_) # Độ dốc
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
## Sử dụng mô hình
# Đưa ra dự đoán với biến hồi quy
y_prediction = LR.predict(X_test)
## Đánh giá mô hình
# Calculate R2-score
score=r2_score(y_test,y_prediction)
print('R2-score is ',score) # Độ ảnh hưởng
print('Mean_sqrd_error is==',mean_squared_error(y_test,y_prediction)) # Trung bình phương sai số
print('Root_mean_squared error of is==',np.sqrt(mean_squared_error(y_test,y_prediction))) # Căn bậc hai của trung bình phương sai số
