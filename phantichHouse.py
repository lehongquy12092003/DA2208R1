import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler,RobustScaler
# Đọc dữ liệu
df = pd.read_excel("house_price_dống-da.xlsx")
#Xóa bỏ tất cả những dòng dữ liệu không có thông tin về giá
df["price"].dropna()
# Thực hiện xử lí dữ liệu khuyết thiếu
df1=df["land_certificate"].fillna("Không có thông tin")
print(df1)
# Thay the khuyet thieu bang du lieu xuat hien nhieu nhat

df["house_direction"].fillna(df["house_direction"].mode()[0],inplace=True)
print(df["house_direction"])

df["balcony_direction"].fillna(df["balcony_direction"].mode()[0],inplace=True)
print(df["balcony_direction"])

df["toilet"].fillna(df["toilet"].mode()[0],inplace=True)
print(df["toilet"])

df["bedroom"].fillna(df["bedroom"].mode()[0],inplace=True)
print(df["bedroom"])

df["floor"].fillna(df["floor"].mode()[0],inplace=True)
print(df["floor"])
#Lọc thông tin những bất động sản ở trong phố thành bộ dữ liệu nhà phố
df = df[df["type_of_land"]=="Bán nhà mặt phố"]
# Tính toán giá trên m2
df["gia/m2"] = df["price"]/df["area"]
# Lọc giá trị ngoại lai
Q1 = df["gia/m2"].quantile(0.25)
Q3 = df["gia/m2"].quantile(0.75)
IQR = Q3 - Q1
df = df[["area","gia/m2"]]
df_s = df[~((df<(Q1-1.5*IQR)) | (df>(Q3+1.5*IQR))).any(axis=1)]
# Chuẩn hoá dữ liệu cột gia/m2
scaler = MinMaxScaler()
df_c = scaler.fit_transform(df_s[["gia/m2"]])
print(pd.DataFrame(df_c).describe())

scaler = RobustScaler()
df_c = scaler.fit_transform(df_s[["gia/m2"]])
print(pd.DataFrame(df_c).describe())

scaler = StandardScaler()
df_c = scaler.fit_transform(df_s[["gia/m2"]])
print(pd.DataFrame(df_c).describe())