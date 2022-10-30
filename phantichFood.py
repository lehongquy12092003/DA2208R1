from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.info())

### Với mức ý nghĩa 5%, kiểm định giả thuyết giá bán gạo trung bình năm 2019 là 9.5 Lira/kg
# Liệt kê tên sản phẩm
product_names = list(df["ProductName"].unique())
print(product_names)
# Lọc những bản ghi liên quan tới giá gạo năm 2019
df_rice = df[(df["ProductName"]=="Rice - Retail") & (df["Year"]==2019)]
print("Số bản ghi của gạo năm 2019 là: {0}".format(df_rice.shape[0]))
# vẽ biểu đồ hist để xem xét
# df_rice["Price"].hist()
# plt.show()
# Giả thuyết không: Giá bán gạo trung bình = 9.5
# Giả thuyết đối: Giá bán gạo trung bình != 9.5
print(stats.ttest_1samp(df_rice["Price"],9.5))
# Giá trị pvalue > 5% nên không đủ cơ sở để bác bỏ giả thuyết 0
# Kết luận: Với mức ý nghĩa 5% có thể nhận định giá bán gạo trung bình bằng 9.5
### Với mức ý nghĩa 5%, hãy kiểm định giả thuyết: Giá bột mì và giá gạo ở Turkey năm 2019 là bằng nhau
df_wheat = df[(df["ProductName"]=="Wheat flour - Retail") & (df["Year"]==2019)]
print("Số lượng bản ghi bột mì năm 2019 là {0}".format(df_wheat.shape[0]))
# Tạo boxplot so sánh phân bố giá bột mì và gạo
price = {'rice': list(df_rice["Price"]), 'wheat': list(df_wheat['Price'])}
df_price = pd.DataFrame(price)
print(df_price)
# sns.boxplot(data=df_price)
# plt.show()
print(stats.ttest_ind(price["rice"],price["wheat"],equal_var=False))
# Chúng ta có thể thấy Pvalue = 7.110465285860583e-55 << 5%, bác bỏ giả thuyết 0, chấp nhận giả thuyết đối
# Kết luận: Giá bột mì và giá gạo là khác nhau
### Vẽ biểu đồ sự biến đổi giá gạo trung bình từ năm 1/2014 đến năm 1/2019 và tìm mối liên hệ giữa giá trà và giá cà phê
# Xóa những biến không cần thiết
del(df_rice,df_price,df_wheat,price)
# Tạo cột gồm có tháng và năm
df["time"] = pd.to_datetime(df["Year"].astype(str)+"/"+df["Month"].astype(str))
# Thực hiện tính toán và vẽ giá trà, coffe theo tháng
df_Tea_all = df[df["ProductName"]=="Tea - Retail"]
df_Tea_all_mean_by_month = df_Tea_all.groupby(["time"])["Price"].mean()
plt.plot_date(df_Tea_all_mean_by_month.index,df_Tea_all_mean_by_month.values,label="Tea_mean")
df_coffee_all = df[df["ProductName"]=="Coffee - Retail"]
df_coffee_all_by_month = df_coffee_all.groupby(["time"])["Price"].mean()
plt.plot_date(df_coffee_all_by_month.index, df_coffee_all_by_month.values,label="coffee_mean")
plt.legend()
# plt.show()
df_tea_and_coffee = df[(df["ProductName"]=="Tea - Retail") | (df["ProductName"]=="Coffee - Retail")]

df_tea_and_coffee["time-place"] = df_tea_and_coffee["time"].astype(str)+"-"+df_tea_and_coffee["Place"]
df1 = df_tea_and_coffee[df_tea_and_coffee["ProductName"]=="Tea - Retail"].filter(["time-place","Price"])
df1 = df1.rename(columns={"Price":"Tea - Retail"})
print(df1.head())
df2 = df_tea_and_coffee[df_tea_and_coffee["ProductName"]=="Coffee - Retail"].filter(["time-place","Price"])
df2 = df2.rename(columns={"Price":"Coffee - Retail"})
print(df2.head())

Processed_data = pd.merge(df1,df2,on="time-place")
print(Processed_data.head())
# Tiến hành kiểm định: Thực hiện kiểm định wilicoxon 1 phía với giả thuyết như sau:
# Giả thuyết không: Giá cà phê bằng giá trà cộng thêm 15 Lira ở mọi thời điểm
# giả thuyết đối: Giá cà phê luôn lớn hơn giá trà 15 Lira 
d = Processed_data['Coffee - Retail']-(Processed_data['Tea - Retail'] + 15)
print(d.head())
print(stats.wilcoxon(d,alternative="greater"))