import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency

df = pd.read_csv("house_price_Dống-Da_Hà-Nội_subdata.csv")
print(df.head())

## Với mức ý nghĩa 5% hãy kiểm định
# Giữa giá nhà và diện tích có tương quan với nhau hay không
df1 = df.filter(["price","area"])
df1 = df1.dropna()
print(stats.pearsonr(df1["price"],df1["area"]))
# Do pvalue < 5% và r = 0.22 giữa giá nhà và diện tích có tương quan tuyến tính yếu

# Giữa giá nhà và tọa độ địa lý (lat, long) có tương quan với nhau
df2 = df.filter(["price","lat","long"])
df2 = df2.dropna()
print(stats.pearsonr(df2["price"],df2["lat"]))
# Do pvalue > 5% nên giữa giá nhà và lat không có tương quan tuyến tính với nhau
print(stats.pearsonr(df2["price"],df2["long"]))
# Do pvalue > 5% nên giữa giá nhà và tọa độ địa lí không tương quan tuyến tính với nhau

# Giữa thuộc tính land_certificate và property_type có tương quan với nhau
df3 = df.filter(["property_type","land_certificate"])
contigency = pd.crosstab(df3["land_certificate"],df3["property_type"])
print(contigency)
c,p,dof,expected = chi2_contingency(contigency)
print(p)
# Do pvalue > 5% nên chưa đủ cơ sở để kết luận land_certificate và property_type có tương quan tuyến tính với nhau

# Hãy  mã hóa lại thuộc tính giá nhà theo đơn vị (nghìn đồng/m2) và sắp xếp giá nhà thành 4 mức tương ứng với các khoảng tứ phân vị. Tiến hành kiểm định tương quan giữa biến giá nhà này với các biến tọa độ vị trí (lat, long)
q1 = df["price"].quantile(0.25)
q2 = df["price"].quantile(0.5)
q3 = df["price"].quantile(0.75)
def price_order(price):
    if price < q1:
        return 1
    elif price >= q1 and price < q2:
        return 2
    elif price >= q2 and price < q3:
        return 3
    else:
        return 4
df["price_ordinal"] = df["price"].apply(price_order)
print(df.head())
df = df.dropna()
r,pvalue = stats.spearmanr(df["price"],df["lat"])
print("r = {0} và pvalue = {1}".format(r,pvalue))
# Do pvalue > 5% nên giữa price và lat không có mối tương quan tuyến tính với nhau
r,pvalue = stats.spearmanr(df["price"],df["long"])
print("r = {0} và pvalue = {1}".format(r,pvalue))
# Do pvalue 