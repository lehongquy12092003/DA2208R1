import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("house_price_dống-da.xlsx")

# Phân tích mối liên hệ giữa diện tích với giá nhà. Đồng thời, giữa số phòng ngủ với giá nhà và giữa số toilet với giá nhà
# fig, ax = plt.subplots(3,1)
# ax[0].scatter(df['area'], df['price'])
# ax[0].set_title('Biểu đồ thể hiện mối liên hệ giữa diện tích, số phòng ngủ, số toilet với giá nhà')


# ax[1].scatter(df['bedroom'], df['price'])


# ax[2].scatter(df['toilet'], df['price'])
# ax[2].set_ylabel('price')

# plt.show()
# Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ, theo số phòng toilet hoặc theo diện tích
df["gia/m2"] = df["price"]/df["area"]
# fig, ax = plt.subplots(3,1)
# ax[0].plot(df['area'], df['gia/m2'],marker="s")
# ax[0].set_title('Biểu đồ thể hiện mối liên hệ giữa diện tích, số phòng ngủ, số toilet với giá nhà')


# ax[1].plot(df['bedroom'], df['gia/m2'],marker="s")


# ax[2].plot(df['toilet'], df['gia/m2'],marker="s")
# ax[2].set_ylabel('price')

# plt.show()

# So sánh giá nhà trung bình trên 1 m2 giữa các hình thức nhà (type_of_land). Đồn thời thể hiện tỉ lệ % bài đăng (bản ghi) giữa các hình thức nhà (type_of_land).
fig, ax = plt.subplots(1, 2)
df1=df["type_of_land"].value_counts()
print(df1)
x = ["Bán nhà riêng","Bán nhà mặt phố","Tập thể, cư xá","Chung cư","Bất động sản khác","Đất thổ cư"]
sizes = [602,241,69,59,21,8]
ax[0].bar(df["type_of_land"], df["gia/m2"])
ax[0].set_title("Biểu đồ gia/m2 giữa các hình thức nhà")
ax[1].pie(sizes, labels = x,autopct='%1.2f%%')
ax[1].set_title("Biểu đồ tỉ lệ bài đăng ")

plt.show()