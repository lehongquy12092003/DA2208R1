import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## Đọc dữ liệu
df = pd.read_csv("subset-covid-data.csv")
# Thông tin dữ liệu
print(df.info())
## Liệu các quốc gia có số lượng ca mắc mới trong ngày 12-4-2020 giống nhau hay không
# Lọc dữ liệu nhiễu 
cleaned_data = df[df.date == "2020-04-12"]
print("Trung bình số ca mắc mới là {0}".format(cleaned_data.cases.mean()))
print("Trung vị số ca mắc mới là {0}".format(cleaned_data.cases.median()))
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("Số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
plt.show()
## Tổng số lượng người mắc bệnh của từng châu lục
df_group = df.groupby(["continent"]).agg({"day":lambda x: x.nunique(),"population":"sum"})
print(df_group)
## Top 5 quốc gia có số lượng ca mắc mới lớn nhất
df_group = df.groupby(["country"])["cases"].sum().sort_values(ascending=False)
print(df_group.head(5))
## Tổng số lượng ca tử vong của từng châu lục
df_group = df.groupby(["continent"]).agg({"day":lambda x:x.nunique(),"deaths":"sum"})
print(df_group)
## Top 5 quốc gia có số ca tử vong lớn nhất
df_group = df.groupby(["country"])["deaths"].sum().sort_values(ascending=False)
print(df_group.head(5))