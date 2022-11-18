import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv("salary_data.csv")
print(df.tail(10))
# Mô tả dữ liệu
print(df.describe())
print(df.shape)
## Tiến hành trực quan hóa
# df.plot(x="SoNamKinhNghiem", y="Luong", style="o")
# plt.title("Số năm kinh nghiệm - lương")
# plt.xlabel("Số năm kinh nghiệm")
# plt.ylabel("Lương")
# plt.show()
# Vẽ biểu đồ histogram
# plt.hist(df["Luong"],20)
# plt.show()

df_ketoan = df[df["NganhNghe"]=="KeToan"]
df_hcnh = df[df["NganhNghe"]=="HCNS"]
df_sale = df[df["NganhNghe"]=="Sale"]

print("Kết cấu bộ dữ liệu là:")
print("Số lượng mẫu nhân viên kế toán: {0}".format(df_ketoan.shape[0]))
print("Số lượng mẫu nhân viên HCNH là: {0}".format(df_hcnh.shape[0]))
print("Số lượng mẫu nhân viên sale: {0}".format(df_sale.shape[0]))

n_by_nganhnghe = df.groupby(["NganhNghe"])["Luong"].mean()
print(n_by_nganhnghe)

# Biểu đồ phân bố lương của kế toán
# plt.boxplot(df_ketoan["Luong"])
# plt.show()
# plt.boxplot(df_hcnh["Luong"])
# plt.show()
# plt.boxplot(df_sale["Luong"])
# plt.show()

#### Xây dựng mô hình model dự đoán tiền lương theo số năm kinh nghiệm
x = df["SoNamKinhNghiem"].values.reshape(-1,1)
y = df["Luong"].values.reshape(-1,1)
# Chia bộ dữ liệu làm 2 tập train và test theo tỉ lệ 80% train, 20% test
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
regressor = LinearRegression() # Khai báo mô hình hồi quy tuyến tính
regressor.fit(x_train, y_train) # Huấn luyện mô hình
print("Mô hình hồi quy sẽ có dạng: Lương = a + b * số năm kinh nghiệm  \nVới các hệ số a và b lần lượt là")
print(regressor.intercept_)
print(regressor.coef_)

#### Đánh giá mô hình
y_pred = regressor.predict(x_test) # Dự đoán trên số năm kinh nghiệm của bộ dữ liệu test
# Tính toán R2 của model
r2_train = r2_score(y_train, regressor.predict(x_train))
print("R2 trên tập huấn luyện của model là: {0}".format(r2_train))
r2_test = r2_score(y_test, y_pred)
print("R2 trên tập kiểm tra của model là: {0}".format(r2_test))

df1 = pd.DataFrame({"Số năm kinh nghiệm": x_test.flatten(), "Lương thực tế": y_test.flatten(),"Lương dự báo": y_pred.flatten()})
print("\n") # xuống dòng
print("Đánh giá năng lực dự báo trung bình trên tập test")
print('Sai số dự báo trung bình:', metrics.mean_absolute_error(y_test, y_pred))

# Trực quan hóa
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color = "red")
plt.show()
# Lưu trữ và sử dụng mô hình sau đã huấn luyện
filename = "model.sav"
pickle.dump(regressor, open(filename, "wb"))
# Sử dụng mô hình sau đã lưu
loaded_model = pickle.load(open(filename, "rb"))
x = [[1],[2],[4]]
y_pred = loaded_model.predict(x)
print(y_pred)