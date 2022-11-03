import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_csv("GDPlist.csv",encoding='latin1')
print(df.head())
# Với mức ý nghĩa 5%, kiểm định trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm
# Giả thuyết không: H0=500
# Giả thuyết đối: H0!=500
print(stats.ttest_1samp(df["GDP (millions of US$)"],500))
# Do pvalue<<5%, nên ta chấp nhận giả thuyết đối
# Vậy trung bình GDP các quốc gia trên thế giới khác 500 tỉ USD/năm

# Với mức ý nghĩa 5%, hãy kiểm định GDP trung bình ở các quốc gia Châu Âu cao hơn Châu Á
# Giả thuyết không: a1 = a2
# Giả thuyết đối: a1 > a2
df1 = df[df["Continent"]=="Asia"]
df2 = df[df["Continent"]=="Europe"]
print(stats.ttest_ind(df1["GDP (millions of US$)"],df2["GDP (millions of US$)"],equal_var=False))
# Do pvalue > 5% nên không đủ cơ sở để bác bỏ H0
# Không đủ căn cứ để kết luận GDP trung bình ở Châu Âu cao hơn Châu Á

# Với mức ý nghĩa 5%, hãy kiểm định GDP trung bình của các quốc gia ở Châu Âu và Châu Mĩ là bằng nhau
# Giả thuyết không: a1=a2
# Giả thuyết đối: a1!=a2
df3 = df[(df["Continent"]=="South America") | (df["Continent"]=="North America")]
print(df3.head())
print(stats.ttest_ind(df2["GDP (millions of US$)"],df3["GDP (millions of US$)"],equal_var=False))
