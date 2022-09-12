import pandas as pd
import numpy as np
df = pd.read_csv("GDPlist.csv")
print(df.info())
# Đổi tên cột thuộc tính
df.rename(columns={"Country":"Nước","Continent":"Châu lục","GDP (millions of US$)":"GDP (triệu $)"},inplace=True)
print(df.head())
# Thêm cột mới
df.insert(1,"Thành phố",pd.Series(df.loc[:,"Nước"],index=df.index))
print(df.head())
# Trong cột Thành phố thì thay Vietnam thành Ha Noi
df["Thành phố"].replace("Vietnam","Ha Noi",inplace=True)
print(df)
# Xóa các bản ghi có Châu lục là Asia
df.drop(df[df["Châu lục"] == "Asia"].index,inplace=True)
print(df)
# Xóa các bản ghi có GDP < 300000
df.drop(df[df["GDP (triệu $)"]<300000].index,inplace=True)
print(df)