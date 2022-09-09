import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("OnlineRetail.csv")
# Tìm hiểu cấu trúc
print(df.info())
# Công ty bán hàng do bao nhiêu nước sản xuất
countries = df.Country.unique()
print("Số lượng các quốc gia là {0}".format(countries.size))
# Tổng số lượng đơn hàng bán ra, tổng doanh thu
df["total"] = df["Quantity"] * df["UnitPrice"]
total_invoices = df["total"].sum()
print("Số lượng hóa đơn bán ra là {0}".format(total_invoices.size))
print("Tổng doanh thu là {0}".format(total_invoices))
# Top 10 mặt hàng có số lượng bán ra lớn nhất
df_group = df.groupby(["StockCode","Description"])["Quantity"].sum().sort_values(ascending=False)
print(df_group.head(10))
# Top 10 mặt hàng có doanh thu lớn nhất
df_group = df.groupby(["StockCode","Description"])["total"].sum().sort_values(ascending=False)
print(df_group.head(10))