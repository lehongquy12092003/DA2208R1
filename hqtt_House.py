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

df = pd.read_csv("AmesHousing.csv")
print(df.head())
print(df.shape)
# Vì Hồi quy cần các tính năng số, hãy chuyển đổi các cột phân loại thành các biến giả
df1 = pd.get_dummies(df)
print(df1.head())
# Tìm kiếm các cột có bất kỳ giá trị NaN (thiếu) nào
print(df1.columns[df1.isna().any()].tolist())
# Số lượng giá trị NaN theo cột
print(df1.isna().sum())
# Để xử lí dữ liệu bị khuyết ta thay bằng giá trị trung vị của cột tương ứng. Ta định nghĩa hàm impute_median() để thực hiện việc này
def impute_median(series):
    return series.fillna(series.median())
df1['Lot Frontage']= df1['Lot Frontage'].transform(impute_median)
df1['Mas Vnr Area']=df1['Mas Vnr Area'].transform(impute_median)
df1['BsmtFin SF 1']=df1['BsmtFin SF 1'].transform(impute_median)
df1['BsmtFin SF 2']=df1['BsmtFin SF 2'].transform(impute_median)
df1['Bsmt Unf SF']=df1['Bsmt Unf SF'].transform(impute_median)
df1['Total Bsmt SF']=df1['Total Bsmt SF'].transform(impute_median)
df1['Bsmt Full Bath']=df1['Bsmt Full Bath'].transform(impute_median)
df1['Bsmt Half Bath']=df1['Bsmt Half Bath'].transform(impute_median)
df1['Garage Cars']=df1['Garage Cars'].transform(impute_median)
df1['Garage Area']=df1['Garage Area'].transform(impute_median)
# Kiểm tra cột có bất kì giá trị NaN nào
print(df1.columns[df1.isna().any()].tolist())
# Sau khi thay trung vị vẫn còn trường (cột) ‘Garage Yr Blt’ thiếu dữ liệu. Ta sẽ lọai bỏ – không xét đến cột này, khi xây dựng mô hình đồng thời đưa dữ liệu đã tiền xử lý vào mảng df2 để tính toán trong các bước tiếp theo
df2=df1.drop('Garage Yr Blt',axis=1)
print(df2.head())
#Define target array y
y = df2["SalePrice"].values
#Create feature array X
x = df2.drop("SalePrice",axis=1).values
print(x)
# Hiển thị kích thước hai mảng x và y
print(x.shape)
print(y.shape)
# Dùng lệnh reshape để định dạng y thành vector cột (mảng 1 cột) và kiểm tra
y = y.reshape(-1,1)
print(y.shape)
## Chia dữ liệu
# Ta dùng hàm train_test_split() trong thư viện scikit-learn để chia bộ dữ liệu ta có thành 2 phần: dữ liệu huẩn luyện (train data) và dữ liệu kiểm tra (test data). Tham số test_size=0.3 cho biết, 30% dữ liệu được lấy để kiểm tra, 70% được dùng để huấn luyện mô hình
#Split the arrays into training and testing data sets
X_train, X_test,y_train, y_test= train_test_split(x,y,test_size=0.3,random_state=42)
## Huấn luyện mô hình
#Create a regressor object
LR= LinearRegression()

#Fit training set to the regressor
LR.fit(X_train,y_train)

#print("Mô hình hồi quy tuyến tính đã được huấn luyện, có các tham số:")
#print("Intercept =", LR.intercept_)
#print("Coefficients:", LR.coef_)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
## Sử dụng mô hình
#Make predictions with the regressor
y_prediction = LR.predict(X_test)
## Đánh giá mô hình
# Calculate R2-score
score=r2_score(y_test,y_prediction)
print('R2-score is ',score)
print('Mean_sqrd_error is==',mean_squared_error(y_test,y_prediction))
print('Root_mean_squared error of is==',np.sqrt(mean_squared_error(y_test,y_prediction)))
