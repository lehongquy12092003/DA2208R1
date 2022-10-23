import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.info())
print(df.describe())
# Loại bỏ dữ liệu bị khuyết
df = df.dropna()
# Lọc dữ liệu sản phẩm gạo, vẽ biểu đồ xu hướng qua các năm
rice_df = df[df["ProductId"]==52]
# Vẽ biểu đồ xu hướng qua các năm
# sns.lmplot(x="Year",y="Price",data=rice_df)
# plt.show()

# trans_df = df[(df["ProductName"]=="Transport (public) - Retail") | (df["ProductName"]=="Rice - Retail")]
# sns.lmplot(x="Year",y="Price",hue="ProductName",data=trans_df)
# plt.show()
# Vẽ biểu đồ phân bố cho giá sản phẩm
# sns.violinplot(y="Price",data=df)
# plt.show()
# Biểu đồ phân bố năm cho sản phẩm
# sns.violinplot(y="Year",data=df)
# plt.show()
# Vẽ biểu đồ tần số cho các sản phẩm theo năm
# sns.countplot(x="Year",data=df)
# plt.show()
# Thống kê sản phẩm theo địa điểm
# sns.countplot(x="Place",data=df)
# plt.show()
# Hiển thị quan hệ số lượng thoe năm được nhóm theo địa điểm
# sns.countplot(x="Year",hue="Place",data=df)
# plt.show()
# Vẽ biểu đồ boxplot
# sns.boxplot(x=df["Price"])
# plt.show()
# Vẽ biểu đồ boxplot giá sản phẩm phân bố theo năm
sns.boxplot(x="Year",y="Price",data=df)
plt.show()