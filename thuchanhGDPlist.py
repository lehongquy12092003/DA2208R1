import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("GDPlist.csv")
# Cho biết số dòng, số cột và kiểu dữ liệu
#print(df.info())
# Tính giá trị lớn nhất và nhỏ nhất của GDP
max_GDP = df["GDP (millions of US$)"].max()
#print(max_GDP)
min_GDP = df["GDP (millions of US$)"].min()
#print(min_GDP)
# Hãy cho biết xu hướng phân bố dữ liệu của GDP
print ("trung bình GDP: " , df["GDP (millions of US$)"].mean())
print ("trung vị GDP: ", df["GDP (millions of US$)"].median())
import matplotlib.pyplot as plt
plt.hist(df["GDP (millions of US$)"])
plt.title("Phân bố GDP")
plt.xlabel("số GDP")
plt.ylabel("Số lượng quốc gia")
#plt.show()
# Hãy cho biết châu lục nào xuất hiện nhiều nhất
df_group = df.groupby(["Continent"])["Continent"].value_counts().max()
print(df_group)
# Tính tổng GDP
pivot_table1 = pd.pivot_table(df,values=["GDP (millions of US$)"],index=["Continent"],aggfunc={"GDP (millions of US$)":"sum"})
# Tính trung bình cộng GDP
pivot_table2 = pd.pivot_table(df,values=["GDP (millions of US$)"],index=["Continent"],aggfunc={"GDP (millions of US$)":"mean"})
# Hợp nhất 2 cột 
target = pd.concat([pivot_table1,pivot_table2],axis=1)
#print(target)