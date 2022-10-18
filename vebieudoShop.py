import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")

## Vẽ biểu đồ
# So sánh số lượng shop gia nhập theo các năm.
df_group = df.groupby(["join_year"])["shopid"].count()
print(df_group)
# y = [4,27,156,87,106,247,119]
# x = ["2015","2016","2017","2018","2019","2020","2021"]
# plt.bar(x,y)
# plt.show()

# Xu hướng của số lượng shop gia nhập theo từng tháng trong từng năm
df_group = df.groupby(["join_year","join_month"])["shopid"].count()
print(df_group)
x1 = ["October"]
y1 = [4]
x2 = ["June","May","November","October","September"]
y2 = [2,5,2,13,5]
x3 = ["April","August","December","February","January","July","June","March","May","November","October","September"]
y3 = [8,12,28,2,2,3,7,8,4,14,32,36]
x4 = ["April","August","December","February","January","July","June","March","May","November","October","September"]
y4 = [14,8,4,7,19,4,3,12,7,1,6,2]
x5 = ["April","August","December","February","January","July","June","March","May","November","October","September"]
y5 = [14,5,7,8,2,7,9,17,10,12,10,5]
x6 = ["April","August","December","January","July","June","March","May","November","October","September"]
y6 = [13,32,16,5,32,22,5,29,25,29,39]
x7 = ["Aprial","February","January","June","March","May"]
y7 = [25,13,21,7,33,20]
# fig, ax = plt.subplots(2,2)
# ax[0][0].bar(x1, y1)
# ax[0][0].set_title("Biểu đồ số lượng shop gia nhập năm 2015")

# ax[0][1].bar(x2, y2)
# ax[0][1].set_title("Biểu đồ số lượng shop gia nhập năm 2016")

# ax[1][0].bar(x3, y3)
# ax[1][0].set_title("Biểu đồ số lượng shop gia nhập năm 2017")

# ax[1][1].bar(x4, y4)
# ax[1][1].set_title("Biểu đồ số lượng shop gia nhập năm 2018")
# plt.show()

# fig, ax = plt.subplots(1,3)

# ax[0].bar(x5, y5)
# ax[0].set_title("Biểu đồ số lượng shop gia nhập năm 2019")

# ax[1].bar(x6, y6)
# ax[1].set_title("Biểu đồ số lượng shop gia nhập năm 2020")

# ax[2].bar(x7, y7)
# ax[2].set_title("Biểu đồ số lượng shop gia nhập năm 2021")

# plt.show()

## Vẽ biểu đồ thể hiện mối quan hệ giữa
# Tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt
# Thời gian phản hồi (Đơn vị giây) với số lượt khách hàng đánh giá tôt
# fig, ax = plt.subplots(1,2)
# ax[0].bar(df["response_rate"],df["rating_good"])
# ax[0].set_title("Biểu đồ thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt")
# ax[1].bar(df["response_time"],df["rating_good"])
# ax[1].set_title("Biểu đồ thể hiện mối quan hệ thời gian phản hồi với số lượt khách hàng đánh giá tốt")
# plt.show()
# Vẽ biểu đồ thể hiện phân bố điểm trung bình
plt.scatter(df["rating_star"],df["rating_normal"])
plt.show()