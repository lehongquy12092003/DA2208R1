import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("subset-covid-data.csv")
print(df.head())
## Với mức ý nghĩa 5%, hãy kiểm định
# Có mối tương quan nào giữa dân số và số ca nhiễm bệnh hay không
df1 = df.filter(["population","cases"])
df1 = df1.dropna()
print(stats.pearsonr(df1["population"],df1["cases"]))
# Do pvalue < 5% nên ta bác bỏ giả thuyết không, chấp nhận giả thuyết đối
# Vì r = 0.17 nên dân số và số ca nhiễm bệnh có tương quan tuyến tính yếu với nhau

# Có mối tương quan nào giữa số ca mắc và số ca tử vong ở các quốc gia hay không
df2 = df.filter(["cases","deaths"])
df2 = df2.dropna()
print(stats.pearsonr(df2["cases"],df2["deaths"]))
# Do pvalue < 5% nên ta bác bỏ giả thuyết không, chấp nhận giả thuyết đối
# Kết luận: r = 0.94, giữa số ca mắc và số ca tử vong có tương quan tuyến tính mạnh với nhau

# Hãy tiến hành rời rạc hóa thuộc tính population thành các nhóm theo thứ tự tăng dần đặt tên là biến population_ordinal
# 1: nếu population < phân vị thứ nhất
# 2: population nằm trong khoảng từ phân vị thứ nhất tới phân vị thứ hai
# 3: population nằm trong khoảng phân vị thứ 2 tới thứ 3
# 4: population lớn hơn phân vị thứ 3
# Tiến hành tính các khoảng tứ phân vị của population
# Tiến hành kiểm định. Do population_ordinal là dữ liệu kiểu thứ bậc nên sử dụng kiểm định spearman để kiểm định tương quan giữa population_ordinal và cases
q1 = df["population"].quantile(0.25)
q2 = df["population"].quantile(0.5)
q3 = df["population"].quantile(0.75)
def population_order(population):
    if population < q1:
        return 1
    elif population >=q1 and population < q2:
        return 2
    elif population >= q2 and population < q3:
        return 3
    else:
        return 4
df["population_ordinal"] = df["population"].apply(population_order)
print(df.head())

r, pvalue = stats.spearmanr(df["cases"],df["population_ordinal"])
print("r = {0} và pvalue = {1}".format(r,pvalue))
#