import pandas as pd

DataFrame_stock1 = pd.read_csv('LAB3/data/stocks1.csv')
print("Dữ liệu Stock1 ban đầu là:\n",DataFrame_stock1)

trung_binh_low = DataFrame_stock1['low'].mean()
trung_binh_high = DataFrame_stock1['high'].mean()

DataFrame_stock1['low'].fillna(trung_binh_low, inplace = True)
DataFrame_stock1['high'].fillna(trung_binh_high, inplace = True)

print("Dữ liệu stock1 sau khi thay thế là:\n",DataFrame_stock1)
print("Số lượng dữ liệu Null sau khi thay thế:\n", DataFrame_stock1.isnull().sum())
print("Thông tin tổng quan:\n",DataFrame_stock1.info())