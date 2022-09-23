import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_excel("house_price_dống-da.xlsx")
# Thông tin dữ liệu
print(df.info())
# Lọc ra các bản ghi bán nhà riêng tại phường Trung Liệt hoặc phường Khâm Thiên
df["Phường"] = df["address"].str.split(",").str[1]
df["Phường"] = df["Phường"].apply(lambda x: str(x).strip())
#df = df[df["Phường"]=="Phường Trung Liệt"]
#print(df)
#df = df[df["Phường"]=="Phường Khâm Thiên"]
#print(df)
# Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên
#df = df[["address","price","house_direction","balcony_direction","land_certificate","bedroom"]]
#df = df[(df["land_certificate"]=="Sổ đỏ") & (df["bedroom"]>=3)]
#print(df)
# Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất
df1 = df.groupby(["type_of_land"])["price"].mean()
df2 = df.groupby(["type_of_land"])["price"].min()
df3 = df.groupby(["type_of_land"])["price"].max()
df4 = pd.concat([df1,df2,df3],axis=1)
print(df4)
# Tính trung bình số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường
pivot_table = pd.pivot_table(df,values = ["bedroom","toilet","floor"],index = ["ward_name"],aggfunc = {"bedroom":"mean","toilet":"mean","floor":"mean"})
print(pivot_table)