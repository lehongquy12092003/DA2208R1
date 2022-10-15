import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("GDPlist.csv")
# So sánh GDP các nước ở  South America
# data1 = df[df["Continent"]=="South America"]
# plt.bar(data1["Country"],data1["GDP (millions of US$)"], width=0.5)
# plt.title("So sánh GDP các nước ở South America.",fontsize=16,color="red")
# plt.xlabel("Countries",fontsize=14)
# plt.ylabel("GDP",fontsize=14)
# plt.show()
# Đánh giá tỉ lệ đóng góp GDP của Việt Nam với 5 nước Đông Nam Á VietNam, Indonesia, Cambodia, Thailand và Malaysia

labels = ['VietNam', 'Indonesia', 'Cambodia', 'Thailand', 'Malaysia']
sizes = [122722,845680,12861,345649,278680]
plt.pie(sizes, labels = labels,autopct="%1.2f%%")
plt.title('Tỉ lệ đóng góp GDP của Việt Nam so với các nước Đông Nam Á', fontsize = 14)
plt.show()
