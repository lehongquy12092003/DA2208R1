import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel("Quality.xlsx")
print(df.head())
print(df.info())
print(df.describe())
### Với mức ý nghĩa 0.01, tiến hành kiểm định chất lượng sản phẩm
# Tiền xử lí dữ liệu
# Gom hết dữ liệu của 4 mẫu thành 1 mảng duy nhất
sample = list()
for i in df.columns:
    sample.extend(df[i].tolist())
# Tiến hành mô tả dữ liệu mẫu
df = pd.DataFrame(columns=["sample"],data=sample)
print(df.describe())
## Dựa vào kết quả phân tích trên: bộ dữ liệu chứa 120 mẫu
# Giá trị trung bình mẫu đúng bằng 12, giống mô tả khách hàng
# Phương sai: = 0.223108 (sai số so với giá trị trung bình của mẫu dữ liệu)>0.21 --> khách hàng nên thay đổi lại tuyên bố về sai số của mình
# Tiến hành kiểm định về giá trị trung bình
# Giả thuyết không: khối lượng trung bình sản phẩm = 12
# Giả thuyết đối: khối lượng trung bình của sản phẩm != 12
# Thực hiện phép kiểm định: One Sample T Test
print(stats.ttest_1samp(sample,12))