import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Đọc dữ liệu
df = pd.read_csv("GDPlist.csv")
# Thông tin dữ liệu
print(df.info())
# Phân tích sự đồng đều GDP của các quốc gia
print("Trung bình số GDP là {0}".format(df["GDP (millions of US$)"].mean()))
print("Trung vị số GDP là {0}".format(df["GDP (millions of US$)"].median()))
plt.hist(df["GDP (millions of US$)"])
plt.title("Phân bố GDP")
plt.xlabel("Số GDP")
plt.ylabel("Số lượng quốc gia")
plt.show()
# Mỗi châu lục có bao nhiêu quốc gia nằm trong bảng dữ liệu
countries = df.Country.unique()
print("Số lượng quốc gia là {0}".format(countries.size))
# Tổng GDP của các châu lục
df_group = df.groupby(["Continent"])["GDP (millions of US$)"].sum()
print(df_group)
# Top 10 quốc gia có GDP cao nhất
df_group = df.groupby(["Country"])["GDP (millions of US$)"].sum().sort_values(ascending=False)
print(df_group.head(10))