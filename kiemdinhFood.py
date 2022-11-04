import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.head())
# Lọc dữ liệu gạo bán lẻ (Rice - Retail) ở National Average

df_rice = df[(df["ProductName"]=="Rice - Retail") & (df["Place"]=="National Average")]
print("Kích thước của bộ dữ ",df_rice.shape)
print("Mô tả dữ liệu")
print(df_rice.describe())
# Vẽ mối liên hệ giữa thời gian và giá gạo
df_rice["time"] = pd.to_datetime(df_rice["Year"].astype(str) + "/" +df_rice["Month"].astype(str))
plt.plot(df_rice["time"],df_rice["Price"])
# plt.show()
# Do thời gian nhận giá trị tăng dần nên có thể được coi là một biến định lượng
# Thực hiện kiểm định pearson để tiến hành kiểm định mối liên hệ giữa hai biến thời gian và giá
# Biến đổi thời gian về dạng định lượng như sau: lấy mốc 1/2013 là mốc 1 tương đối, 1 tháng sẽ được tính là một đơn vị thời gian
df_rice["time_processed"] = df_rice["Month"] + (df_rice["Year"]-2013)*12
print(df_rice)
# Giả thuyết không: Giữa thời gian và giá gạo không có mối tương quan
# Giả thuyết đối: Giữa thời gian và giá gạo có mối tương quan
print("Hệ số tương quan và pvalue tương ứng là:")
print(stats.pearsonr(df_rice["time_processed"],df_rice["Price"]))