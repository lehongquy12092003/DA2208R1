import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler,RobustScaler,StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder

df = pd.read_csv("Credit_Scoring.csv")
print(df.info())
print(df.describe())
# Kiểm tra dữ liệu khuyết thiếu
print(df.isna())
# Thay thế giá trị bị khuyết bằng giá trị nội suy theo các cột
df = df.interpolate(axis=1)
# Thay thế giá trị khuyết thiếu bằng giá trị 0
df = df.fillna(0)
# Vẽ biểu đồ boxplot, biểu đồ phân bố dữ liệu cho các cột
# sns.boxplot(x=df["age"])
# plt.show()
# sns.boxplot(x=df["SeriousDlqin2yrs"])
# plt.show()
# sns.boxplot(x=df["age"])
# plt.show()
# sns.boxplot(x=df["NumberOfTime30-59DaysPastDueNotWorse"])
# plt.show()
# sns.boxplot(x=df["DebtRatio"])
# plt.show()
# sns.boxplot(x=df["MonthlyIncome"])
# plt.show()
# sns.boxplot(x=df["NumberOfOpenCreditLinesAndLoans"])
# plt.show()
# sns.boxplot(x=df["NumberOfTimes90DaysLate"])
# plt.show()
# sns.boxplot(x=df["NumberRealEstateLoansOrLines"])
# plt.show()
# sns.boxplot(x=df["NumberOfTime60-89DaysPastDueNotWorse"])
# plt.show()
# sns.boxplot(x=df["NumberOfDependents"])
# plt.show()
# Loại bỏ giá trị ngoại lai
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 -Q1
df = df[~((df<(Q1-1.5*IQR)) | (df>(Q3+1.5*IQR))).any(axis=1)]
print(df)
# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng dữ liệu của mỗi nhóm
cats = pd.qcut(df["age"],4)
# Đếm số lượng phần tử
print(pd.value_counts(cats))
# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng dữ liệu của mỗi nhóm
cats = pd.qcut(df["MonthlyIncome"],4)
# Đếm số lượng phần tử
print(pd.value_counts(cats))

# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng dữ liệu của mỗi nhóm
cats = pd.qcut(df["age"],5)
# Đếm số lượng phần tử
print(pd.value_counts(cats))
# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng dữ liệu của mỗi nhóm
cats = pd.qcut(df["MonthlyIncome"],5)
# Đếm số lượng phần tử
print(pd.value_counts(cats))

# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng dữ liệu của mỗi nhóm
cats = pd.qcut(df["age"],6)
# Đếm số lượng phần tử
print(pd.value_counts(cats))
# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng dữ liệu của mỗi nhóm
cats = pd.qcut(df["MonthlyIncome"],6)
# Đếm số lượng phần tử
print(pd.value_counts(cats))

# Chia dữ liệu ở các cột age và MonthlyIncome thành 5 nhóm theo các khoảng: 0,30,40,50,80,150 và đếm số lượng phần tử ở mỗi nhóm
bins = [0,30,40,50,80,150]
cats = pd.cut(df["age"],bins)
print(cats)
# Đếm số lượng phần tử
print(pd.value_counts(cats))

bins = [0,30,40,50,80,150]
cats = pd.cut(df["MonthlyIncome"],bins)
print(cats)
#Đếm số lượng phần tử
print(pd.value_counts(cats))