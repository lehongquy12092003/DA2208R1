import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_excel("Coca_cola_use.xlsx")
print("5 bản ghi đầu tiên là: ")
print(df.head())
print("Thông tin của bộ dữ liệu:")
print(df.info())
print("Mô tả dữ liệu:")
print(df.describe())
# Vẽ biểu đồ boxplot
# sns.boxplot(data=df)
# plt.show()
### Với mức ý nghĩa 5%, hãy kiểm định giả thuyết xem có đúng lượng tiêu thụ Coca bình quân ở Ohio lớn hơn Atlanta hay không
## Tiến hành kiểm định
# Giả thuyết không: a1-a2=0
# Giả thuyết đối: a1-a2>0
# Loại kiểm định Independent T test
print(stats.ttest_ind(df["Ohio"],df["Atlanta"],equal_var=False))

