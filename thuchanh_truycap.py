import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# Truy cập dòng có chỉ số 3 
tg = df.iloc[3]
print(tg)
# Truy cập các dòng có chỉ số liên tục từ 3 tới 7
tg = df.iloc[3:8]
print(tg)
# Truy cập các phần tử rời rạc của dữ liệu
tg = df.iloc[[2,4,6]]
print(tg)
# Truy cập cột thứ 4 của dữ liệu
tg = df.iloc[:,5]
print(tg)
# Truy cập liên tục từ cột 3 tới cột 7
tg = df.iloc[:,3:8]
print(tg)
# Truy cập tới các phần tử từ dòng 3 đến dòng 4, cột 5 đến cột 6
tg = df.iloc[3:5,5:7]
print(tg)
# Truy cập phần tử dòng 3, cột 7
tg = df.iloc[3,7]
print(tg)
# Truy cập phần tử có year >= 2019
tg = df[df["Year"]>=2019]
print(tg)
# Thay thế số 5 thành số 10 trong toàn bộ dữ liệu
df.replace(5,10,inplace=True)
print(df.head())
# Thay thế giá trị 52 thành RR trong toàn bộ dữ liệu
df.replace(52,"RR",inplace=True)
print(df.head())
# Thay giá trị 10 trong cột Month thành giá trị 5
df["Month"].replace(10,5,inplace=True)
print(df.tail())
