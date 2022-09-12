import pandas as pd
# Đọc file csv
df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.head())
# Đọc file excel
df = pd.read_excel("house_price_dống-da.xlsx")
print(df.head())
# Đọc file Json
df = pd.read_json('FoodPrice.json')
print(df.head())
# Đọc file hdf5
df=pd.read_hdf('FoodPrice.h5', 'table')
print(df.head())
# Đọc file html
url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
df = pd.read_html(url)
print(df[0].head())