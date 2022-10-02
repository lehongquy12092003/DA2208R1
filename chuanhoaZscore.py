import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
# Tạo các cột theo các phần khối khác nhau
df = pd.DataFrame({"beta":np.random.beta(5,1,1000)*60,
"exponential":np.random.exponential(10,1000),
"normal_p":np.random.normal(10,2,1000),
"normal_l":np.random.normal(10,10,1000),})
# Thêm dữ liệu được tạo theo phân phối nhị thức
first_half = np.random.normal(20,3,500)
second_half = np.random.normal(-20,3,500)
bimodal = np.concatenate([first_half,second_half])
df["bimodal"] = bimodal
print(df.head())
# Trực quan hóa dữ liệu sinh ra
#sns.kdeplot(data=df)
#plt.show()
# Hiển thị thống kê về dữ liệu sinh ra
print(df.describe())
# Thêm một đặc trưng với giá trị lớn hơn nhiều
normal_big = np.random.normal(1000000,10000,(1000,1))
df["normal_big"] = normal_big
#sns.kdeplot(data=df)
#plt.show()
# Trực quan hóa bằng biểu đồ box plot
#df.boxplot()
#plt.show()
# Chuẩn hóa với StandardScaler (Z-Score scaling)
# Khai báo đối tượng StandarScaler
s_scaler = StandardScaler()
# Chuẩn hóa dữ liệu trong df với StandarScaler 
df_s = s_scaler.fit_transform(df)
# Lấy danh sách cột
col_names = list(df.columns)
# Chuyển về DataFrame, gắn các cột của df cho dữ liệu đã được chuẩn hóa
df_s = pd.DataFrame(df_s,columns=col_names)
print(df_s.head())
#sns.kdeplot(data=df_s)
#plt.show()
# Thống kê về dữ liệu được sinh ra
print(df_s.describe())
# Trực quan hóa dữ liệu bằng box plot
df_s.boxplot()
plt.show()