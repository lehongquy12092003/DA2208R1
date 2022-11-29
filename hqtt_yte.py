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

# age: tuổi của người được bảo hiểm
# sex: giới tính (male, female)
# bmi: chỉ số trọng lượng cơ thể (body mass index)
# children: số con
# smoker: cho biết có phải người hút thuốc hay không (yes/no)
# region: vùng sinh sống (northeast, northwest, southeast, southwest)
# charges: chi phí y tế trong năm

# Đọc dữ liệu
df = pd.read_csv("insurance.csv")
print(df.head())
print(df.info())
print(df.shape)
# Vẽ biểu đồ để trực quan hóa mối quan hệ giữa tuổi của người được bảo hiểm (age) với chi phí y tế (charges); 
# plt.scatter(df["age"],df["charges"])
# plt.xlabel("age")
# plt.ylabel("charges")
# plt.show()
# và mối quan hệ giữa chỉ số trọng lượng cơ thể (bmi) với chi phí y tế (charges).
# plt.scatter(df["bmi"],df["charges"])
# plt.xlabel("age")
# plt.ylabel("charges")
# plt.show()
# Chuyển các biến có kiểu categorical: sex, smoker, region thành các biến “Dummy”: sex_female , sex_male, smoker_no, smoker_yes, region_northeast  region_northwest region_southeast, region_southwest. Sau đó loại bớt 2 trường không cần thiết:  sex_male, smoker_no.
df1 = pd.get_dummies(df)
print(df1.head())
# Chia ngẫu nhiên dữ liệu quan sát được thành hai phần dữ liệu huấn luyện và dữ liệu kiểm tra.
y = df1["age"].values
print(y)
x = df1.drop("age",axis=1).values
print(x)
y = y.reshape(-1,1)

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
