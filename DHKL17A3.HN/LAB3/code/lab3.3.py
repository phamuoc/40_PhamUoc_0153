import pandas as pd

DataFrame_stock1 = pd.read_csv('LAB3/data/stocks1.csv')
DataFrame_stock2 = pd.read_csv('LAB3/data/stocks2.csv')

print("Stock1:\n",DataFrame_stock1)
print("Stock2:\n",DataFrame_stock2)

stock = pd.concat([DataFrame_stock1, DataFrame_stock2], ignore_index = True)
print("Stock sau khi gộp là:\n",stock)

stock['mean'] = stock[['open', 'high', 'low', 'close']].mean(axis=1)
print(stock.head())