import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")

# Với mức ý nghĩa 5%, hãy kiểm định giữa rating_star và follower_count có tương quan với nhau hay không
df1 = df.filter(["rating_star","follower_count"])
df1 = df1.dropna()
print(stats.pearsonr(df1["rating_star"],df1["follower_count"]))
# Do pvalue > 5% nên không đủ căn cứ để bác bỏ H0
# Kết luận: Giữa rating_star và follower_count không có mối tương quan tuyến tính

# Giữa rating_star và số lượng sản phẩm (item_count) có tương quan với nhau hay không
df2 = df.filter(["rating_star","item_count"])
df2 = df2.dropna()
print(stats.pearsonr(df2["rating_star"],df2["item_count"]))
# Do pvalue > 5% nên không đủ căn cứ để bác bỏ H0
# Kết luận: Giữa rating_star và item_count không có mối tương quan tuyến tính

# Giữa is_shopee_verified và việc có cửa hàng trưng bày (is_official_shop) có tương quan với nhau hay không
df3 = df.filter(["is_shopee_verified","is_official_shop"])
df3 = df3.dropna()
print(stats.pearsonr(df3["is_shopee_verified"],df3["is_official_shop"]))
# Do pvalue 