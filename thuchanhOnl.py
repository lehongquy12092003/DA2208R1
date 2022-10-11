import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler,RobustScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder
# Doc du lieu
df = pd.read_csv("OnlineRetail.csv")
# In ra kich thuoc du lieu
print(df.shape)
print(df.head())
print(df.info())
# Kiem tra du lieu khuyet
print(df.isna())
# Kiem tra du lieu khong bi khuyet
print(df["CustomerID"].notna())
# In nhung dong ngoai lai Quantity < 0
print(df[df["Quantity"]<0])
# Xoa bo dong ngoai lai cua Quantity
df = df[df["Quantity"]>=0]
# Xoa nhung dong chua gia tri bi khuyet
df1 = df.dropna()
print(df1.shape)
# Xoa nhung dong chua toan gia tri bi khuyet
df2 = df.dropna(how="all")
print(df2.shape)
# Giu nhung dong co it nhat 7 gia tri khong bi khuyet
df3 = df.dropna(thresh=7)
print(df3.shape)
# Xoá những dòng mà có giá trị bị khuyết trên cột Customer
df4 = df.dropna(subset=["CustomerID"])
print(df4.shape)
# Thay thế nhuững giá trị bị khuyết trên cột CustomerID bằng giá trị -1
df5 = df
df5["CustomerID"] = df["CustomerID"].fillna(-1)
# Hiển thị những dòng có CustomerID = -1 vừa được thay thế
print(df5[df5["CustomerID"]==-1])
# Thay thế giá trị bị khuyết ở cột Country bằng giá trị trước đó
df5["Country"] = df["Country"].fillna(method="ffill")
print(df5)
### Xử lí dữ liệu ngoại lai
# sns.boxplot(x=df1["Quantity"])
# plt.show()
# Xoá dữ liệu ngoại lai bằng IQR score
Q1 = df1["Quantity"].quantile(0.25)
Q3 = df1["Quantity"].quantile(0.75)
IQR = Q3 - Q1
# Xác định phần tử không phải ngoại lai
df6 = df1
df6['outlier'] = ~((df1['Quantity'] < (Q1 - 1.5*IQR)) | (df1['Quantity'] > (Q3 + 1.5*IQR)))

# xóa phần tử ngoại lai
df6 = df6[df6['outlier'] == True]


# sns.boxplot(x=df6['Quantity'])  # vẽ box plot cho dữ liệu ở cột Quantity
# plt.show()
# Mô tả dữ liệu
print(df1["Quantity"].describe())
# Chuẩn hoá dữ liệu với MinMaxScaler
scaler = MinMaxScaler()
# Chuẩn hoá dữ liệu trong df với MinMaxScaler ở cột Quantity
df_s = scaler.fit_transform(df1[["Quantity"]])
print(pd.DataFrame(df_s).describe())
# Vẽ lại biểu đồ hộp
# sns.boxplot(x=df_s)
# plt.show()
# Chuẩn hoá dữ liệu với z-score scaling
scaler = StandardScaler()
# Chuẩn hoá dữ liệu trong df với Standardscaler ở cột Quantity
df_s = scaler.fit_transform(df1[["Quantity"]])
# Mô tả dữ liệu sau khi chuẩn hoá
print(pd.DataFrame(df_s).describe())
# Vẽ lại biểu đồ
# sns.boxplot(x=df_s)
# plt.show()
# sns.kdeplot(data=df_s)
# plt.show()
# Chuẩn hoá dữ liệu với Robust scaling
scaler = RobustScaler()
# Chuẩn hoá dữ liệu trong df với RobustScaler ở cột Quantity
df_s = scaler.fit_transform(df1[["Quantity"]])
# Mô tả dữ liệu sau khi chuẩn hoá
print(pd.DataFrame(df_s).describe())
# Vẽ lại biểu đồ hộp
# sns.boxplot(x=df_s)
# plt.show()
### Mã hoá dữ liệu
# Các giá trị ở cột Country
print(df1["Country"].unique())
# Mã hoá cột Country với One-hot encoder sử dụng scikit learn
encoder = OneHotEncoder()
encoder_data = encoder.fit_transform(np.asarray(df1["Country"]).reshape(-1,1))
print(encoder_data.todense())
# Mã hoá cột Country với One-hot encoder sử dụng pandas
print(pd.get_dummies(df1["Country"]))
# Mã hoá cột Country với Label encoder sử dụng scikit learn
encoder = LabelEncoder()
encoder_data = encoder.fit_transform(np.asarray(df1["Country"]))
print(encoder_data)
# Mã hoá cột Country với Label Encoder sử dụng pandas
print(df1["Country"].astype("category").cat.codes)
### Rời rạc hoá dữ liệu
# Rời rạc hoá dữ liệu ở cột UnitPrice
# Chia thành 4 khoảng giá trị có độ dài bằng nhau
cats = pd.cut(df1["UnitPrice"],4)
print(cats)
# Số lượng phần tử ở mỗi phần
print(pd.value_counts(cats))
# Chia thành 4 phần có số lượng phần tử tương đương nhau
cats = pd.qcut(df1["UnitPrice"],4)
print(cats)
# Số lượng phần tử ở mỗi phần 
print(pd.value_counts(cats))