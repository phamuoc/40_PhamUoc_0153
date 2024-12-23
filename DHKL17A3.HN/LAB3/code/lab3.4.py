import pandas as pd

DataFrame_companies = pd.read_csv('LAB3/data/companies.csv')
DataFrame_stock1 = pd.read_csv('LAB3/data/stocks1.csv')
DataFrame_stock2 = pd.read_csv('LAB3/data/stocks2.csv')

print("Stock1:\n", DataFrame_stock1)
print("Stock2:\n", DataFrame_stock2)

stocks = pd.concat([DataFrame_stock1, DataFrame_stock2], ignore_index=True)

print("5 dòng đầu tiên của DataFrame companies:\n", DataFrame_companies.head())

merged_data = pd.merge(stocks, DataFrame_companies, left_on="symbol", right_on="name")

average_close_per_company = merged_data.groupby('symbol')['close'].mean()

print("Trung bình giá 'close' của 5 công ty đầu tiên:\n", average_close_per_company.head())