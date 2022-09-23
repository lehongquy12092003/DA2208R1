import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("OnlineRetail.csv")
# Thông tin dữ liệu
print(df.info())
# Tạo cột mới có tên quý - "Previous"
df["Month"] = df["InvoiceDate"].str.split("/").str[1]
logic1 = (df["Month"] == "1") | (df["Month"] == "2") | (df["Month"] == "3")
logic2 = (df["Month"] == "4") | (df["Month"] == "5") | (df["Month"] == "6")
logic3 = (df["Month"] == "7") | (df["Month"] == "8") | (df["Month"] == "9")
logic4 = (df["Month"] == "10") | (df["Month"] == "11") | (df["Month"] == "12")

df["Previous"] = np.nan

df["Previous"][logic1] = 1
df["Previous"][logic2] = 2
df["Previous"][logic3] = 3
df["Previous"][logic4] = 4

print(df)
# Tạo cột mới có tên "Amount"
df["Amount"] = df["Quantity"] * df["UnitPrice"]
print(df.head())
# Tạo cột mới "Discount"
conditions = [(df["Country"]=="United Kingdom")&(df["Previous"]==4),(df["Country"]=="France")]
choices = [0.1,0.05]
df["Discount"] = np.select(conditions,choices,default=0)
#print(df)
# Tạo cột mới "Total"
df["Total"] = df["Amount"] - df["Discount"]
print(df)