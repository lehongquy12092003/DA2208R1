import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("house_price_dống-da.xlsx")

# Vẽ biểu đồ phân tích mối liên hệ giữa diện tích với giá nhà, giữa số phòng ngủ với giá nhà, giữa toilet với giá nhà
# x = df["area"]
# y = df["price"]
# plt.scatter(x,y)
# plt.show()
# x = df["bedroom"]
# y = df["price"]
# plt.scatter(x,y)
# plt.show()
# x = df["toilet"]
# y = df["price"]
# plt.scatter(x,y)
# plt.show()
# Vẽ biểu đồ so sánh giá nhà trung bình trên 1 m2 giữa các hình thức nhà
df["average house price"] = df["price"]/df["area"]
# print(df)
# x = df["type_of_land"]
# y = df["average house price"]
# plt.bar(x,y)
# plt.show()
# Vẽ biểu đồ thể hiện phần trăm tỉ lệ bài đăng (bản ghi) giữa các hình thức nhà (type_of_land)
df_group = df.groupby(["type_of_land"])["type_of_land"].value_counts()
print(df_group)
label = ["Bán nhà mặt phố","Bán nhà riêng","Bất động sản khác","Chung cư","Tập thể, cư xá","Đất thổ cư"]
sizes = [65+176,348+254,21,59,69,8]
plt.pie(sizes,labels=label,autopct="%1.2f%%")
plt.show()
# Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ
# x = df["bedroom"]
# y = df["average house price"]
# plt.scatter(x,y)
# plt.show()