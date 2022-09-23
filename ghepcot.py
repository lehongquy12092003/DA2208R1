import pandas as pd
import numpy as np
#Place: Nơi bán
#ProductID: Mã sản phẩm
#ProductName: Tên sản phẩm
#UmId: Mã đơn vị đo lường
#UmName: Tên đơn vị đo lường
#Month: Tháng
#Year: Năm
#Price: Giá
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, giữ chỉ số ban đầu của các dòng
df = df.drop_duplicates(["ProductId"],keep="last")
print(df)
# Xóa các dòng có thuộc tính ProductId trùng nhau, giữ lại bản ghi cuối cùng, thiết lập lại chỉ số
df = df.drop_duplicates(["ProductId"],keep="last").reset_index(drop=True)
print(df)
# Tách file chứa thông tin sản phẩm
df_pro = df.loc[:,['ProductId','ProductName','UmId','UmName']]
print(df_pro)
# Tách file chứa thông tin giá
df_pri = df.loc[:,['ProductId','Place','Month','Year','Price']]
print(df_pri)
# Tách file chứa thông tin giá với số dòng từ bản ghi 10 đến bản ghi 20
df_pri10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]
print(df_pri10)
# Ghép các dữ liệu lại với nhau
df2 = pd.concat([df_pro,df_pri],axis=1)
print(df2)
# Ghép các cột lại với nhau
df3 = pd.concat([df_pri,df_pro,df_pri10],axis=1)
print(df3)