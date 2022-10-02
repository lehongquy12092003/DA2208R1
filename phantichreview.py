import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
df = pd.read_csv("Credit_Scoring.csv")
print(df.head())
## Thông tin dữ liệu
print(df.info())
## Mô tả dữ liệu
print(df.describe())
## Xử lí dữ liệu khiếm khuyết
# Kiểm tra dữ liệu khiếm khuyết
print(df.isna())
# # Loại bỏ dữ liệu khiếm khuyết
df1 = df.dropna()
# print(df1) 
# # % số lượng bản ghi còn lại
target =df1.shape[0]/df.shape[0]*100
print(target)
# ## Vẽ biểu đồ phân bố
# #sns.kdeplot(data=df1["MonthlyIncome"])
# #plt.show()
# ## Thay thế dữ liệu khuyết thiếu bởi giá trị nội suy theo cột
df2 = df.interpolate(axis=1) #############################
print(df2)
print(df2.isna())
# ## Xử lí dữ liệu ngoại lai
# # Vẽ biểu đồ boxplot cho các đặc trưng
# #df2.boxplot()
# #plt.show()
# # Vẽ biểu đồ boxplot cho MonthlyIncome
# sns.boxplot(x=df2["MonthlyIncome"])
# plt.show()
# # Tính giá trị Q1 và Q3
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR = Q3 - Q1
# # Lọc dữ liệu ngoại lai
df3 = df2[~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df3)
# df3.boxplot()
# plt.show()
# sns.boxplot(x=df3["MonthlyIncome"])#############################
# plt.show()
## Mô tả dữ liệu
# print(df3.describe())
# # Phân bố dữ liệu trên cột MonthlyIncome
sns.kdeplot(data=df3["MonthlyIncome"])
plt.show()
# ## Chuẩn hóa với MinMaxScaler
# scaler = MinMaxScaler()
# mms = scaler.fit_transform(pd.DataFrame(df3["MonthlyIncome"]))
# #sns.kdeplot(data=mms)
# #plt.show()
# ## Chuẩn hóa với RobustScaler
# scaler = RobustScaler()
# rbs = scaler.fit_transform(pd.DataFrame(df3["MonthlyIncome"]))
# #sns.kdeplot(data=rbs)
# #plt.show()
# ## Chuẩn hóa với standardScaler
# scaler = StandardScaler()
# scs = scaler.fit_transform(pd.DataFrame(df3["MonthlyIncome"]))
# sns.kdeplot(data=scs)
# plt.show()