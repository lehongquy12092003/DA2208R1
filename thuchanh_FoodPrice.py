import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# Bộ dữ liệu chứa bao nhiêu dòng và bao nhiêu cột
print(df.info)
# Giá trị trung bình của từng loại thực phẩm
df_group = df.groupby(["ProductId","ProductName"])["Price"].mean()
print(df_group)