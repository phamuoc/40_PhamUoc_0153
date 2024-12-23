import pandas as pd

DataFrame_stock1 = pd.read_csv('data/stocks1.csv')
DataFrame_stock2 = pd.read_csv('data/stocks2.csv')

stocks = pd.concat([DataFrame_stock1, DataFrame_stock2], ignore_index=True)

bang_tong_hop = stocks.pivot_table(
    values='close',
    index='date',
    columns='symbol',
    aggfunc='mean'
)

tong_volume = stocks.groupby('symbol')['volume'].sum()
bang_tong_hop['tong_volume'] = bang_tong_hop.columns.map(tong_volume)

bang_tong_hop_sorted = bang_tong_hop.sort_values(by='tong_volume', axis=1, ascending=False)

print(bang_tong_hop_sorted.head())