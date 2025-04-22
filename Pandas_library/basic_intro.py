import pandas as pd
f_t = pd.read_csv(
    "C:/Users/Monalisha/OneDrive/Desktop/mca_prog/python/Pandas_library/market_fact.csv")
print(f_t.head())  # will retrieve first 5 rows
print(f_t.tail())
print(f_t.info())
print(f_t.describe())
f_t.dropna()
print(f_t.max())
