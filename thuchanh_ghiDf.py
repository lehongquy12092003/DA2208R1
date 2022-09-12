import pandas as pd
df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.head())
# Ghi dữ liệu từ DataFrame vào file csv
df.to_csv("demo_foodPrice.csv")
# Ghi dữ liệu từ DataFrame vào file excel
df.to_excel("demo_FoodPrice.xlsx")
# Ghi dữ liệu từ DataFrame vào file Json
df.to_json("demo_FoodPrice.json",orient="columns")
# Ghi dữ liệu từ DataFrame vào file HDF5
df.to_hdf("demo_FoodPrice.h5","table")
# Ghi dữ liệu từ DataFrame vào file HTML
df.to_html("demo_FoodPrice.html")