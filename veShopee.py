import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
df = df.dropna()
# Vẽ biểu đồ tần số số lượng shop gia nhập theo các năm
# sns.countplot(x="join_year",data=df)
# plt.show()
# Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt
# sns.lmplot(x="response_rate",y="rating_good",data=df)
# plt.show()
# Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa thời gian phản hồi với số lượt khách hàng đánh giá xấu
# sns.lmplot(x="response_rate",y="rating_bad",data=df)
# plt.show()
# Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình
# sns.violinplot(y="rating_star",data=df)
# plt.show()
# Vẽ biểu đồ tần số của cửa hàng chính thức và không chính thức
# sns.countplot(x="join_year",hue="is_official_shop",data=df)
# plt.show()
# Vẽ biểu đồ tần số của cửa hàng được xác thực với chưa xác thực
sns.countplot(x="join_year",hue="is_shopee_verified",data=df)
plt.show()