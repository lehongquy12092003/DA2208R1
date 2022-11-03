import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# SeriousDlqin2yrs: Khách hàng gặp khó khăn tài chính trong vòng 2 năm trở lại đây
# Age: Tuổi
# Total_money: Tổng số dư trong tài khoản – tổng các khoản vay
# NumberOfTime30-59DaysPastDueNotWorse: Số lần nợ thành toán thẻ từ 30-59 ngày.
# DebtRatio: Số tiền chi tiêu thẻ tín dụng/tổng thu nhập.
# MonthlyIncome: Thu nhập hàng tháng.
# NumberOfOpenCreditLinesAndLoans: Số lượng khoản vay Mở (trả góp như khoản vay mua ô tô hoặc thế chấp) và Dòng tín dụng (ví dụ: thẻ tín dụng).
# NumberOfTimes90DaysLate: Số lần người vay đã quá hạn 90 ngày trở lên.
# NumberRealEstateLoansOrLines: Số lượng các khoản vay thế chấp và bất động sản bao gồm hạn mức tín dụng sở hữu nhà.
# NumberOfTime60-89DaysPastDueNotWorse: Số lần người vay đã quá hạn 60-89 ngày nhưng không tệ hơn trong 2 năm qua.
# NumberOfDependents: Số người phụ thuộc trong gia đình không bao gồm bản thân
df = pd.read_csv("Credit_Scoring.csv")
print(df.head())

# Có phải những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) nhỏ hơn những khách hàng có người phụ thuộc, với mức ý nghĩa là 10%
df1 = df[df["NumberOfDependents"]==0]
print(df1.head())
df2 = df[df["NumberOfDependents"]>0]
print(df2.head())
print(stats.ttest_ind(df1["MonthlyIncome"].dropna(),df2["MonthlyIncome"].dropna(),equal_var=False))
# Giả thuyết không: a1=a2
# Giả thuyết đối: a1<a2
# Do pvalue << 10% nên ta bác bỏ H0 và chấp nhận H1
# Kết luận: Vậy khách hàng không có người phụ thuộc thì thu nhập theo tháng sẽ thấp hơn so với những khách hàng có người phụ thuộc

# Có phải trung bình số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) những khách hàng gặp khó khăn trong vòng 2 năm trở lại đây (SeriousDlqin2yrs =1) thì sẽ cao hơn những khách hàng không gặp khó khăn không, với mức ý nghĩa 10%
df3 = df[df["SeriousDlqin2yrs"]==1]
df4 = df[df["SeriousDlqin2yrs"]==0]
print(df3.head())
print(df4.head())
print(stats.ttest_ind(df3["NumberOfOpenCreditLinesAndLoans"],df4["NumberOfOpenCreditLinesAndLoans"],equal_var=False))
# Giả thuyết không: a1=a2
# Giả thuyết đối: a1>a2
# 