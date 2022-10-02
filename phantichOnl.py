import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler,RobustScaler
df = pd.read_csv("OnlineRetail.csv")
# Kiểm tra dữ liệu
print(df.info())
print(df.describe())
# Phát hiện các dòng, các cột chứa giá trị khuyết thiếu
print(df.isna())
# Thay thế giá trị khuyết thiếu của thuộc tính Description bằng giá trị mặc định "Không biết"
df["Description"].fillna("Không biết")
print(df)
# Thực hiện phát hiện giá trị ngoại lai của thuộc tính Quantity và thuộc tính UnitPrice 
# sns.kdeplot(data=df["Quantity"])
# plt.show()
# sns.kdeplot(data=df["UnitPrice"])
# plt.show()
# Lọc dữ liệu ngoại lai
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df2 = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
df2.boxplot()
plt.show()