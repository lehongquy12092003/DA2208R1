import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler,RobustScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder
# Đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# In ra kích thước dữ liệu
print(df.shape)
# In ra 5 dòng đầu tiên
print(df.head())
# Mô tả dữ liệu
print(df.describe())
# Thông tin dữ liệu
print(df.info())
# Kiểm tra dữ liệu bị khuyết
print(df.isna())
# Kiểm tra dữ liệu không bị khuyết
print(df.notna())
# Xóa những dòng chứa ít nhất 1 giá trị bị khuyết 
df1 = df.dropna()
print(df1.shape)
### Xử lí dữ liệu ngoại lai cho đặc trưng Price
sns.boxplot(x=df1["Price"])
plt.show()
# Xử lí dữ liệu ngoại lai bằng IQR
Q1= df1["Price"].quantile(0.25)
Q3 = df1["Price"].quantile(0.75)
IQR = Q3 - Q1
# Xác định phần tử không phải ngoại lai
df2 = df1
df2["logic"] = ~((df1["Price"]<(Q1<-1.5*IQR)) | (df1["Price"]>(Q3+1.5*IQR)))
df2 = df2[df2["logic"]==True]
# sns.boxplot(x=df2["Price"])
# Mô tả dữ liệu
print(df2["Price"].describe())
# Biểu đồ phân bố dữ liệu
# sns.kdeplot(data=df2["Price"])
# plt.show()
### Chuẩn hóa dữ liệu với MinMaxScaler
scaler = MinMaxScaler()
# Chuẩn hóa dữ liệu trong df với MinMaxScaler ở 2 cột Price
df_s = scaler.fit_transform(df2[["Price"]])
# Mô tả dữ liệu chuẩn hóa
print(pd.DataFrame(df_s).describe())
# Vẽ lại biểu đồ hộp
# sns.boxplot(x=df_s)
# plt.show()
### Chuẩn hóa dữ liệu với RobustScaler
scaler = RobustScaler()
# Chuẩn hóa dữ liệu trong df với RobustScaler ở 2 cột Price
df_s  = scaler.fit_transform(df2[["Price"]])
#Mô tả dữ liệu sau chuẩn hóa
print(pd.DataFrame(df_s).describe())
# Vẽ lại biểu đồ hộp
# sns.boxplot(x=df_s)
# plt.show()
# Biểu đồ phân bố dữ liệu
# sns.kdeplot(data=df_s)
# plt.show()
### Chuẩn hóa dữ liệu với z-score scaling
scaler = StandardScaler()
# Chuẩn hóa dữ liệu trong df với StandardScaler ở 2 cột Price
df_s = scaler.fit_transform(df2[["Price"]])
# Mô tả dữ liệu sau chuẩn hóa
print(pd.DataFrame(df_s).describe())
## Vẽ boxplot cho dữ liệu đã được chuẩn hóa
# sns.boxplot(x=df_s)
# plt.show()
# Vẽ biểu đồ kdep lot
# sns.kdeplot(data=df_s)
# plt.show()
#### Mã hóa dữ liệu
# Các giá trị ở cột ProductName
print(df2["ProductName"].unique())
# Mã hóa cột ProductName với One-hot encoder sử dụng scikit learn
encoder = OneHotEncoder()
encoder_data = encoder.fit_transform(np.asarray(df2["ProductName"]).reshape(-1,1))
print(encoder_data.todense())
# Mã hóa cột ProductName với One-hot encoder sử dụng pandas
print(pd.get_dummies(df2["ProductName"]))
# Mã hóa cột ProductName với Label encoder sử dụng scikit learn
encoder = LabelEncoder()
encoder_data = encoder.fit_transform(np.asarray(df2["ProductName"]))
print(encoder_data)
# Mã hóa cột ProductName với Label encoder bằng pandas
print(df2["ProductName"].astype("category").cat.codes)
### Rời rạc hóa dữ liệu
print(df2.head())
# Rời rạc hóa dữ liệu ở cột Price
# Chia thành 5 khoảng có giá trị độ dài bằng nhau
cats = pd.cut(df2["Price"],5)
print(cats)
# Số lượng phân tử ở mỗi phần
print(pd.value_counts(cats))
# Chia thành 5 phần tử tương đuwong nhau
cats = pd.qcut(df2["Price"],5)
print(cats)
# Số lượng phần tử ở mỗi phần
print(pd.value_counts(cats))