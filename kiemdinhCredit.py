import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency

df = pd.read_csv("Credit_Scoring.csv")
print(df.head())
## Với mức ý nghĩa 5% hãy kiểm định
# Giữa độ tuổi (age) và thu nhập trung bình theo tháng (MonthlyIncome) có tương quan với nhau hay không?
df1 = df.filter(["age","MonthlyIncome"])
df1 = df1.dropna()
print(stats.pearsonr(df1["age"],df1["MonthlyIncome"]))
# Do pvalue < 5% và r = 0.03 nên giữa age và MonthlyIncome gần như không có mối tương quan tuyến tính với nhau

# Giữa số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) và độ tuổi có tương quan với nhau không
df2 = df.filter(["NumberOfOpenCreditLinesAndLoans","age"])
df2 = df2.dropna()
print(stats.pearsonr(df2["NumberOfOpenCreditLinesAndLoans"],df2["age"]))
# Do pvalue < 5% và r = 0.14 nên giữa hai thuộc tính không có tương quan tuyến tính với nhau

# Giữa (số lượng người phụ thuộc) NumberOfDependents và thu nhập theo tháng (MonthlyIncome) có tương quan với nhau hay không
df3 = df.filter(["NumberOfDependents","MonthlyIncome"])
df3 = df3.dropna()
print(stats.pearsonr(df3["NumberOfDependents"],df3["MonthlyIncome"]))
# Do pvalue < 5% và r = 0.06 nên giữa NumberOfDependents và MonthlyIncome hầu như không có mối tương quan tuyến tính với nhau

# Mã hóa lại thuộc tính MonthlyIncome thành thuộc tính MonthlyIncome_order theo các khoảng tứ phân vị, giữa thuộc tính mới này và tình trạng nợ xấu trong 2 năm trở lại đây (SeriousDlqin2yrs) có liên quan tới nhau không
q1 = df["MonthlyIncome"].quantile(0.25)
q2 = df["MonthlyIncome"].quantile(0.5)
q3 = df["MonthlyIncome"].quantile(0.75)
def MonthlyIncome_order(MonthlyIncome):
    if MonthlyIncome < q1:
        return 1
    elif MonthlyIncome >= q1 and MonthlyIncome < q2:
        return 2
    elif MonthlyIncome >= q2 and MonthlyIncome < q3:
        return 3
    else:
        return 4
df["MonthlyIncome_order"] = df["MonthlyIncome"].apply(MonthlyIncome_order)
print(df.head())
df = df.dropna()
r, pvalue = stats.spearmanr(df["MonthlyIncome"],df["SeriousDlqin2yrs"])
print("r = {0} và pvalue = {1}".format(r,pvalue))
# Do pvalue < 5% và r = -0.06 nên giữa MonthlyIncome và SeriousDlqin2yrs hầu như không có mối tương quan tuyến tính với nhau
# Giữa thuộc tính MonthlyIncome_order với thuộc tính tỉ lệ số dư tài khoản (RevolvingUtilizationOfUnsecuredLines) có mối liên hệ với nhau không
df4 = df.filter(["MonthlyIncome_order","RevolvingUtilizationOfUnsecuredLines"])
contigency = pd.crosstab(df4["MonthlyIncome_order"],df4["RevolvingUtilizationOfUnsecuredLines"])
print(contigency)
c,p,dof,expected = chi2_contingency(contigency)
print(p)