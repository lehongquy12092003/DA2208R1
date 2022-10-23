import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("OnlineRetail.csv")
print(df.info())
print(df.describe())
# Loại bỏ dữ liệu bị khuyết
df = df.dropna()
# Tính giá của mỗi sản phẩm ở các đơn hàng 
df["Price"] = df["Quantity"] * df["UnitPrice"]
print(df.head())
# Biểu đồ phân bố giá sản phẩm
# sns.violinplot(y="UnitPrice",data=df)
# plt.show()
# Biểu đồ phân bố tổng giá sản phẩm
# sns.violinplot(y="Price",data=df)
# plt.show()
# Tính tổng số lượng sản phẩm mỗi đơn hàng
df2 = df.groupby(["InvoiceNo"])["Quantity"].sum().reset_index()
print(df2.head())
# Biểu đồ phân bố lượng sản phẩm trên mỗi đơn hàng
# sns.violinplot(y="Quantity",data=df2)
# plt.show()
# Vẽ biểu đồ tần số
df3 = df.groupby(["Country"])["Quantity"].sum().reset_index()
print(df3.head())
# Loại bỏ dữ liệu trùng lặp
df1 = df.drop_duplicates(subset = 'InvoiceNo')
print(df1.head())
# Vẽ biểu đồ tần số cho hoá đơn theo quốc gia
# sns.countplot(x="Country",data=df1)
# plt.show()
# Vẽ biểu đồ boxplot cho thuộc tính giá sản phẩm
# sns.boxplot(x=df["UnitPrice"])
# plt.show()
# Vẽ biểu đồ boxplot cho số lượng sản phẩm mỗi đơn hàng
sns.boxplot(x=df2["Quantity"])
plt.show()
