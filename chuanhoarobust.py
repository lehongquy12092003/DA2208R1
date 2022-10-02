import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler
# tạo các cột theo các phần phối khác nhau
df = pd.DataFrame({ 
    'beta': np.random.beta(5, 1, 1000) * 60,        # beta
    'exponential': np.random.exponential(10, 1000), # exponential
    'normal_p': np.random.normal(10, 2, 1000),      # normal platykurtic
    'normal_l': np.random.normal(10, 10, 1000),     # normal leptokurtic
})
# thêm dữ liệu được tạo theo phân phối nhị thức
first_half = np.random.normal(20, 3, 500) 
second_half = np.random.normal(-20, 3, 500) 
bimodal = np.concatenate([first_half, second_half])

df['bimodal'] = bimodal
print(df.head())
# Trực quan hóa dữ liệu sinh ra
#sns.kdeplot(data=df)
#plt.show()
# Hiển thị thống kê dữ liệu sinh ra
print(df.describe())
# Thêm một đặc trưng với giá trị lớn hơn nhiều
normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values
df['normal_big'] = normal_big
#sns.kdeplot(data=df)
#plt.show()
# Trực quan hóa bằng biểu đồ box plot
#df.boxplot()
#plt.show()
# Chuẩn hóa đối tượng RobustScaler
scaler = RobustScaler()
# Chuẩn hóa dữ liệu trong df với StandardScaler
df_s = scaler.fit_transform(df)
# Lấy danh sách cột
col_names = list(df.columns)
# Chuyển về DataFrame, gán các cột của df cho dữ liệu đã được chuẩn hóa
df_s = pd.DataFrame(df_s,columns=col_names)
print(df_s.head())
# Biểu diễn dữ liệu đã được chuẩn hóa
#sns.kdeplot(data=df_s)
#plt.show()
# Thống kê dữ liệu được sinh ra
print(df_s.describe())
# Trực quan hóa bằng biểu đồ boxplot
#df_s.boxplot()
#plt.show()
# Lấy các giá trị min ở mỗi cột
mins = [df_s[col].min() for col in df_s.columns]
print(mins)
# Lấy giá trị max ở mỗi cột
maxs = [df[col].max() for col in df_s.columns]
print(maxs)
# Giá trị trung vị của các đặc trưng của tập dữ liệu gốc
print(scaler.center_)