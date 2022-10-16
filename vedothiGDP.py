import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("GDPlist.csv")

# Biểu đồ để hiển thị giá trị cụ thể và so sánh GDP các nước Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.
# Biểu đồ để đánh giá tỉ lệ đóng góp GDP của các nước trên tổng số GDP của 5 nước Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.
data1 = df[(df["Country"]=="Vietnam")]
print(data1)
data2 = df[(df["Country"]=="Indonesia")]
print(data2)
data3 = df[(df["Country"]=="Cambodia")]
print(data3)
data4 = df[(df["Country"]=="Thailand")]
print(data4)
data5 = df[(df["Country"]=="Malaysia")]
print(data5)
x1 = ["Vietnam","Indonesia","Cambodia","Thailand","Malaysia"]
y1 = [122722,845680,12861,345649,287680]
fig, ax = plt.subplots(1, 2)

ax[0].bar(x1, y1)
ax[0].set_title("Biểu đồ so sánh GDP 5 nước")
ax[1].pie(y1, labels = x1,autopct='%1.2f%%')
ax[1].set_title("Biểu đồ tỉ lệ GDP")

plt.show()
