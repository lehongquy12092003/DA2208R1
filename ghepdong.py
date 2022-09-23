import pandas as pd
import numpy as np
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# Tách dữ liệu 5000 dòng đầu tiên
df1 = df.loc[0:4999]
#print(df1)
# Tách các bản ghi còn lại
df2 = df.loc[5000:7380]
#print(df2)
# Tách file 3 chứa thông tin giá với số dòng từ bản ghi 1000 đến 2000
df3 = df.loc[1000:2000,['ProductId','Place','Month','Year','Price']]
#print(df3)
# Ghép các dòng từ df1 và df2
df4 = pd.concat([df1,df2],axis=0)
#print(df4)
# Ghép các dòng từ các file
df5 = pd.concat([df1,df2,df3],axis=0)
#print(df5)
## append
df6 = df1.append(df2)
print(df6)