import pandas as pd
import numpy as np
# Tạo dữ liệu
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
# Định nghĩa khoảng giá trị các nhóm
bins = [18,25,35,60,100]
# Thực hiện rời rạc hóa
cats = pd.cut(ages,bins)
print(cats)
# Lấy ra index của nhóm tương ứng với các phần tử
print(cats.codes)
# Lấy ra các nhóm 
print(cats.categories)
# Thống kê số lượng phần tử của mỗi nhóm
df_group = pd.value_counts(cats)
print(df_group)
# Đồng nhất với kí hiệu toán học cho các khoảng, dấu ngoặc đơn có nghĩa là cạnh đó mở,
# trong khi dấu ngoặc vuông tức là cạnh đó đóng(bao gồm).
# Chúng ta có thể thay đổi phía bị đóng băng bằng cách truyền vào tham số right = False
cats1 = pd.cut(ages,[18,26,36,61,100],right=False)
print(cats1)
# Truyền vào danh sách nhãn
group_names = ["Youth","YoungAdult","MiddleAged","Senior"]
cats2 = pd.cut(ages,bins,labels = group_names)
print(cats2)

# Sinh dữ liệu ngẫu nhiên gồm 20 phần tử
data = np.random.rand(20)
# Tùy chọn precision = 2 sẽ giới hạn độ chính xác thập phân ở hai chữ số
cut_data = pd.cut(data,4,precision=2)
print(cut_data)
# Thống kê số lượng phần tử mỗi nhóm
df_group = pd.value_counts(cut_data)
print(df_group)

# sinh ngẫu nhiên dữ liệu gồm 1000 điểm dữ liệu
data = np.random.rand(1000)
# Thực hiện hàm qcut trên dữ liệu vừa sinh ra, qcut giúp chia đều dữ liệu
cats3 = pd.qcut(data,4)
print(cats3)
# Thống kê số lượng phần tử
df_group = pd.value_counts(cats3)
print(df_group)
# Tương tự cut, chúng ta có thể chuyển các lượng tử của riêng mình(các số từ 0 đến 1)
cats4 = pd.qcut(data,[0,0.1,0.5,0.9,1])
print(cats4)