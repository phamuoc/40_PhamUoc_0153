import pandas as pd

DataFrame_stock1 = pd.read_csv('LAB3/data/stocks1.csv')
DataFrame_stock2 = pd.read_csv('LAB3/data/stocks2.csv')

stocks = pd.concat([DataFrame_stock1, DataFrame_stock2], ignore_index=True)

stocks.set_index(['date', 'symbol'], inplace=True)

trung_binh = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',
    'high': 'mean',
    'low': 'mean',
    'close': 'mean',
    'volume': 'mean'
})

# Sắp xếp dữ liệu theo ngày và mã chứng khoán
trung_binh_sap_xep = trung_binh.sort_values(by=['date', 'symbol'])

print("Kết quả 5 ngày đầu tiên:\n", trung_binh_sap_xep.head())