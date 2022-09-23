import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("OnlineRetail.csv")
# Thông tin dữ liệu
print(df.info())
# Xây dựng bảng pivot_table, với mỗi số hóa đơn, tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia
pivot_table1 = pd.pivot_table(df,values = ["Quantity"],index = ["InvoiceNo","Country"],aggfunc={"Quantity":"mean"})
print(pivot_table1)
# Xây dựng bảng pivot_table, với mỗi khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo kho
pivot_table2 = pd.pivot_table(df,values = ["Quantity"],index = ["CustomerID"],aggfunc={"Quantity":"max"})
print(pivot_table2)
pivot_table3 = pd.pivot_table(df,values = ["Quantity"],index = ["CustomerID"],aggfunc={"Quantity":"min"})
print(pivot_table3)
df = pd.concat([pivot_table2,pivot_table3],axis=1)
print(df)
# Xây dựng bảng pivot_table, với mỗi Mã kho, tính tổng số lượng các mặt hàng và trung bình cộng giá
pivot_table4 = pd.pivot_table(df,values = ["Quantity","UnitPrice"],index = ["StockCode"],aggfunc={"Quantity":"sum","UnitPrice":"mean"})
print(pivot_table4)
# Xây dựng bảng pivot_table, cho biết tổng số lượng hàng bán được của mỗi ngày
pivot_table5 = pd.pivot_table(df,value = ["Quantity"],index = ["InvoiceDate"],aggfunc={"Quantity":"sum"})
print(pivot_table5)