import pandas as pd
import numpy as np
# Đọc dữ liệu
df = pd.read_csv("OnlineRetail.csv")
# Thông tin dữ liệu
print(df.info())
# Trích xuất các cột Description và Quantity lưu vào file demoOnline.csv
target = df.iloc[:,2:4]
target.to_csv("demoOnlineRetail.csv")
# Trích xuất 1000 dòng dữ liệu đầu tiên lưu vào file demoOnlineRetail
target = df.loc[0:1000]
target.to_excel("demoOnlineRetail.xlsx")
# Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file demoOnlineRetail.h5
target = df[df["Quantity"]>=10]
target.to_hdf("demoOnlineRetail.h5","table")
# Trích xuất dữ liệu các phần tử dòng 1000 đến dòng 2000, các cột Quantity, InvoiceDate, UnitPrice lưu vào file demoOnlineRetail.json
target = df.iloc[1000:2001,3:6]
target.to_json("demoOnlineRetail.json",orient="columns")
# Trích xuất các bản ghi có số hóa đơn "536365" lưu vào file demoOnlineRetail.html
target = df[df["InvoiceNo"]=="536365"]
target.to_html("demoOnlineRetail.html")
