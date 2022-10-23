import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("GDPlist.csv")
print(df.info())
print(df.describe())
# Loại bỏ dữ liệu khuyết
df = df.dropna()
# Vẽ biểu đồ phân bố
# sns.violinplot(y="GDP (millions of US$)",data=df)
# plt.show()
# Biểu đồ phân bố giá trị GDP Châu Á
# df1 = df[df["Continent"]=="Asia"]
# sns.violinplot(y="GDP (millions of US$)",data=df1)
# plt.show()
# Vẽ biểu đồ boxplot nhóm theo châu lục
sns.boxplot(x="Continent",y="GDP (millions of US$)",data=df)
plt.show()