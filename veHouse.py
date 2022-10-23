import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("house_price_dống-da.xlsx")
# Vẽ biểu đồ phân tích xu hướng mối quan hệ giữa giá nhà với diện tích, giá nhà với số lượng phòng ngủ
# sns.lmplot(x="area",y="price",data=df)
# plt.show()
# sns.lmplot(x="bedroom",y="price",data=df)
# plt.show()
# Vẽ biểu đồ phân bố thể hiện phân bố của giá nhà theo các hướng, nhận xét
# sns.violinplot(x="house_direction",y="price",data=df)
# plt.show()
# Vẽ biểu đồ tần số đếm số nhà theo các hướng
# sns.countplot(x="price",hue="house_direction",data=df)
# plt.show()
# Vẽ biểu đồ boxplot thể hiện phân bố của giá nhà theo các hướng
sns.boxplot(x="house_direction",y="price",data=df)
plt.show()