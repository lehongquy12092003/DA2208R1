import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("house_price_Dống-Da_Hà-Nội_subdata.csv")
# Vẽ biểu đồ so sánh phân phối giá (triệu đ/m2) giữa nhà phố và nhà ngõ
# sns.kdeplot(data=df,x="price",hue="property_type")
# plt.show()
# Kiểm định giả thuyết giá nhà mặt phố cao hơn giá nhà trong ngõ với mức ý nghĩa 5%
df1 = df[df["property_type"]=="mat pho"]
df2 = df[df["property_type"]=="trong ngo"]
print(stats.ttest_ind(df1["price"].dropna(),df2["price"].dropna(),equal_var=False))
# Giả thuyết không: a1=a2
# Giả thuyết đối: a1-a2>0
# Do pvalue > 5% nên chưa đủ căn cứ để bác bỏ H0
# Kết luận: Với mức ý nghã 5%, thì giá nhà trong ngõ bằng với giá nhà mặt phố

# Giá của những căn nhà không có thông tin về giấy tờ pháp lí thấp hơn giá nhà những căn nhà có thông tin về giấy tờ pháp lí, với mức ý nghĩa 5%
# Giả thuyết không: a1 = a2
# Giả thuyết đối: a1 < a2
df3 = df[df["land_certificate"].isnull()]

df4 = df[df["land_certificate"].notna()]

print(stats.ttest_ind(df3["price"].dropna(),df4["price"].dropna(),equal_var=False))
# Do pvalue