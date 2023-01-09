import sklearn.metrics as metrics
from sklearn.metrics import r2_score
import pickle
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd 
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_percentage_error
from scipy import stats
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model

# Xây dựng mô hình dự báo giá đất trên/m2 của bài toán mua bán đất huyện Đông Anh
df = pd.read_csv("LandTrading.csv")
print(df.head())
# Lọc dữ liệu
df["ten_quan"] = df["ten_quan"].apply(lambda x: str(x).strip()) # Loại bỏ khoảng trắng
df1= df[df["ten_quan"]=="Huyện Đông Anh"]
# Mô tả dữ liệu
# print("Dữ liệu có {0} dòng và {1} cột".format(df1.shape[0],df1.shape[1]))
# print("Thông tin chi tiết dữ liệu:")
# print(df1.describe())
# Biểu đồ phân bố giá_m2 nhà trước khi tiền xử lí dữ liệu
# sns.violinplot(y="gia_m2", data=df1)
# plt.show()
# sns.boxplot(y="gia_m2",data=df1)
# plt.show()
# #print(df1.head())
df1["so_do"] = df1["so_do"].isna()

df1["so_do"] = df1["so_do"].apply({True:0, False:1}.get)
print(df1["so_do"])

# # # Check Hệ số tương quan giữa các biến( vẽ thêm heatmap để dễ trực quan)
# # # print(df1.corr())
# # # sns.heatmap(df1.corr(), vmin=0, vmax=1, annot=True, cmap=plt.cm.Reds)
# # # plt.show()
# # # Chọn các cột cần thiết để xây dựng mô hình
df2=df1[["so_do","lat","long","mat_tien","dien_tich","do_rong_duong","gia_m2","id_duong", "id_phuong","gia"]]
# print(df2.columns[df2.isna().any()].tolist())
print(df2.describe())
print(df2.info())
print(df2.shape)
#so_do          678 non-null    object
#  1   lat            1584 non-null   float64
#  2   long           1584 non-null   float64
#  3   mat_tien       941 non-null    float64
#  4   dien_tich      1561 non-null   float64
#  5   do_rong_duong  178 non-null    float64
#  6   gia_m2         1271 non-null   float64
#  7   id_duong       1273 non-null   object
#  8   id_phuong      1500 non-null   object
#  9   gia            1270 non-null   float64
# Dữ liệu có tổng cộng 1585 dòng

# # # Xử lí dữ liệu khuyết
df2["dien_tich"] = df2["dien_tich"].fillna(df2['dien_tich'].median())

df2 = df2[(df2["gia_m2"]>=40) & (df2["gia_m2"]<=55)]

df2["mat_tien"] = df2["mat_tien"].fillna(df2['mat_tien'].median())
df2['gia_m2'] = df2['gia_m2'].fillna(df2['gia_m2'].median())

df2["lat"].fillna(df2["lat"].mode()[0],inplace=True)
df2["long"].fillna(df2["long"].mode()[0],inplace=True)

df2['id_duong'] = df2['id_duong'].fillna('NULL').astype('category').cat.codes
df2['id_phuong'] = df2['id_phuong'].fillna('NULL').astype('category').cat.codes

df2['do_rong_duong']=df2['do_rong_duong'].fillna(value=2.5) # Độ rộng đường trong khoảng 2.5 đến 4.5

df2["gia"] = df2["gia"].fillna(df2['gia'].median()) 

## Xử lí ngoại lai
Q1 = df2['gia_m2'].quantile(0.25)
Q3 = df2['gia_m2'].quantile(0.75)
IQR = Q3 - Q1
df2 = df2[~((df2['gia_m2'] < (Q1 - 1.5 * IQR) ) | (df2['gia_m2'] > (Q3 + 1.5*IQR)))]

Q1 = df2['dien_tich'].quantile(0.25)
Q3 = df2['dien_tich'].quantile(0.75)
IQR = Q3 - Q1
df2 = df2[~((df2['dien_tich'] < (Q1- 1.5 * IQR) ) | (df2['dien_tich'] > (Q3 + 1.5*IQR)))]

Q1 = df2['mat_tien'].quantile(0.25)
Q3 = df2['mat_tien'].quantile(0.75)
IQR = Q3 - Q1
df2 = df2[~((df2['mat_tien'] < (Q1 - 1.5*IQR) ) | (df2['mat_tien'] > (Q3 + 1.5*IQR)))]

Q1 = df2['gia'].quantile(0.25)
Q3 = df2['gia'].quantile(0.75)
IQR = Q3 - Q1
df2 = df2[~((df2['gia'] < (Q1- 1.5 * IQR) ) | (df2['gia'] > (Q3 + 1.5*IQR)))]

# Điểm ngoại lai sẽ là những điểm mà nằm dưới Q1 ít nhất là 1.5*IQR, hoặc nằm trên Q3 ít nhất là 1.5*IQR.

# #  Xuất ra file csv
# df2.to_excel("du_bao_gia_dat.xlsx")

# # Split dữ liệu
x = df2[["so_do","lat","long","mat_tien","dien_tich","do_rong_duong","id_duong", "id_phuong","gia"]] 
y = df2["gia_m2"]
# Chuẩn hóa dữ liệu 
# Công thức của nó là: z = (x – u) / s
# Trong đó: u là mean của dữ liệu huấn luyện, s là độ lệch chuẩn,
#  x là điểm dữ liệu cần chuẩn hóa, z là dữ liệu được chuẩn hóa
scaler = StandardScaler()
x_sc = scaler.fit_transform(x)
################################################################

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold

# Chia dữ liệu để làm chuẩn và để test (test=20%, train=80%)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_sc, y, test_size=0.2, random_state=42)

from sklearn.metrics import explained_variance_score,mean_absolute_error,r2_score

from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
# Danh sách các mô hình hồi quy tuyến tính
regressors = [
    KNeighborsRegressor(),
    GradientBoostingRegressor(),
    ExtraTreesRegressor(),
    RandomForestRegressor(),
    DecisionTreeRegressor(),
    LinearRegression(),
    Lasso(),
    Ridge()
]
for model in regressors:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(model)
    print("\tMAPE:", mean_absolute_percentage_error(y_test, y_pred)) # % trị tuyệt đối Trung bình phương sai số
    print("\tR2 score:", r2_score(y_test, y_pred))
    print()

# Huấn luyện mô hình RandomForestRegressor()
x_train, x_test,y_train, y_test= train_test_split(x_sc,y,test_size=0.2,random_state=42)
model = LinearRegression()

model.fit(x_train,y_train)

#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
## Sử dụng mô hình
# Đưa ra dự đoán với biến hồi quy
y_prediction = model.predict(x_test) 

## Đánh giá mô hình
# Calculate R2-score
score = r2_score(y_test,y_prediction)
print("Lấy mô hình RandomForestRegressor() để infer dữ liệu:")
print('R2-score is ',score) 
print('MAPE',mean_absolute_percentage_error(y_test,y_prediction))

# infer 
# "so_do","lat","long","mat_tien","dien_tich","do_rong_duong","id_duong", "id_phuong","gia" 
# theo dung thu tu
input = [0, 21.12, 105.83, 5, 67, 2.5, 40, 11, 2914.5]
input = np.array(input).reshape(1,-1)
estimate = model.predict(input)
print(x.columns.tolist())
print("Giá_m2 theo dự đoán là: ")
print(estimate)
