import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
# khởi tạo dữ liệu
df = pd.DataFrame({ 
    'beta': np.random.beta(5, 1, 1000) * 60,        # beta
    'exponential': np.random.exponential(10, 1000), # exponential
    'normal_p': np.random.normal(10, 2, 1000),      # normal platykurtic
    'normal_l': np.random.normal(10, 10, 1000),     # normal leptokurtic
})
print(df.head())
# Thêm dữ liệu được tạo theo phân phối nhị thức
first_half = np.random.normal(20, 3, 500) 
second_half = np.random.normal(-20, 3, 500) 
bimodal = np.concatenate([first_half, second_half])

df['bimodal'] = bimodal
print(df.head())
# Trực quan hóa dữ liệu sinh ra
#sns.kdeplot(data=df)
#plt.show()
# Hiển thị thống kê về dữ liệu sinh ra
print(df.describe())
normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values
df['normal_big'] = normal_big
#sns.kdeplot(data=df)
#df.boxplot()
#plt.show()
# Chuẩn hóa với MinMaxScaler
# Khai báo đối tượng MinMaxScaler
scaler = MinMaxScaler()
# Chuẩn hóa dữ liệu trong df với StandardScaler
df_s = scaler.fit_transform(df)
# Lấy danh sách cột
col_names = list(df.columns)
# Chuyển về DataFrame, gán các cột của df cho dữ liệu đã được chuẩn hóa
df_s = pd.DataFrame(df_s,columns=col_names)
print(df.head())
# Biểu diễn dữ liệu đã được chuẩn hóa
#sns.kdeplot(data=df_s)
#plt.show()
# Chuẩn hóa dữ liệu bằng biểu đồ boxplot
#df_s.boxplot()
#plt.show()
# Thống kê dữ liệu được sinh ra
print(df_s.describe())
# Lấy giá trị min của cột beta
print(df_s["beta"].min())
# Lấy giá trị max của cột beta
print(df_s['beta'].max())
# In các giá trị min của từng cột trong dữ liệu khi chưa chuẩn hóa
mins = [df[col].min() for col in df.columns]
print(mins)
# In các giá trị min của từng cột trong dữ liệu đã chuẩn hóa
mins = [df_s[col].min() for col in df_s.columns]
print(mins)
# In các giá trị của max của từng cột trong dữ liệu khi chưa chuẩn hóa
maxs = [df[col].max() for col in df.columns]
print(maxs)
# In các giá trị max của từng cột dữ liệu đã chuẩn hóa
maxs = [df_s[col].max() for col in df_s.columns]
print(maxs)