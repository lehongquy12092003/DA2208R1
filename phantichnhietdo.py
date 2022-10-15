import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("daily-min-temperatures.csv")
# Hien thi cac gia tri thong ke cua du lieu nhiet do
print(df["Temp"].describe())
# Ve bieu do Histogram
# plt.hist(df["Temp"],bins=45)
# plt.show()
# Tinh chinh bieu do
# plt.hist(df['Temp'], bins = 45, range = (1, 23), histtype = 'step')
# plt.title('Temperature Histogram', fontsize = 16)
# plt.show()
# Ve bieu do xu huong nhiet do
# plt.plot(df['Date'], df['Temp'])
# plt.title('Daily Temperature', fontsize = 16)
# plt.xlabel('Date', fontsize = 14)
# plt.ylabel('Temp', fontsize = 14)
# plt.show()

## Co the thay xu huong, thay doi nhiet do co tinh chu ki
df['Date'] = pd.to_datetime(df['Date'])
bounds = ['1/1/1990', '12/31/1990']
bounds = pd.to_datetime(bounds)
d1 = df[(df['Date'] >= bounds[0]) & (df['Date'] <= bounds[1])]
plt.plot(d1['Date'], d1['Temp'])
plt.title('Daily Temperature in 1990', fontsize = 16)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('Temp', fontsize = 14)
plt.show()