import pandas as pd

DataFrame_stock1 = pd.read_csv('LAB3/data/stocks1.csv')
print(DataFrame_stock1)

print("5 dòng đầu tiên của DataFrame Stock1 là:\n",DataFrame_stock1.head(5))
print("Kiểu dữ liệu của DataFrame Stock1 là:\n",DataFrame_stock1.dtypes)
print("Thông tin tổng quan của Stock1 là:\n",DataFrame_stock1.info())