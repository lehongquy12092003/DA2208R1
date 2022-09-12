import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv")
#print(df.head())
# Đổi tên cột thuộc tính
df.rename(columns={"Place":"Địa điểm", "ProductName":"Tên sản phẩm"}, inplace = True)
#print(df.head())
# Thêm cột mới mang giá trị rỗng
df["New_column"]=np.nan
#print(df.head())
# Thêm cột giảm giá 10% cho tất cả các bản ghi
df["giảm giá"] = "10%"
#print(df.head())
# Thêm một dòng cuối vào DataFrame
df=df.append({'Địa điểm':'NA','ProductId':'RR','Tên SP':'Rice','UmId':10,'UmName':'KG','Month':6,'Year':2021,'Price':84.3785,'Giảm giá':'10%'},ignore_index=True)
print(df.tail()) # Hiển thị 5 bản ghi cuối
# Xóa một cột trong DataFrame
df.drop("Tên sản phẩm",axis=1,inplace=True)
#print(df.head())
# Xóa nhiều cột
df.drop(["New_column","Giảm giá"],axis=1,inplace=True)
#print(df.head())
# Xóa các dòng trong DataFrame
df.drop([7377,7379],inplace=True)
print(df)