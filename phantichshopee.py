import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")

# Vẽ biểu đồ so sánh số lượng shop gia nhập theo các năm
# y  = df.groupby(["join_year"])["shopid"].count()
# print(y)
# x = ["2015","2016","2017","2018","2019","2020","2021"]
# z = [4,27,156,87,106,247,119]
# plt.bar(x,z)
# plt.show()
# Vẽ biểu đồ thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượng khách hàng đánh giá tốt
# x = df["response_rate"]
# y = df["rating_good"]
# plt.scatter(x,y)
# plt.show()
# Vẽ biểu đồ thể hiện mối quan hệ giữa thời gia phản hồi với số lượt khách hàng đánh giá xấu
# x = df["response_time"]
# y = df["rating_bad"]
# plt.scatter(x,y)
# plt.show()
# Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình
plt.hist(df["rating_star"],bins=80)
plt.show()