import sys

import pandas as pd

files = sys.argv[1:]

df = [pd.read_csv(f, names=['f', 'cik', 'cusip']).dropna() for f in files]
df = pd.concat(df)

df['leng'] = df.cusip.map(len)

df = df[(df.leng == 6) | (df.leng == 8) | (df.leng == 9)]

df['cusip6'] = df.cusip.str[:6]

df = df[df.cusip6 != '000000']
df = df[df.cusip6 != '0001pt']

df['cusip8'] = df.cusip.str[:8]

df.cik = pd.to_numeric(df.cik)

df = df[['cik', 'cusip6',
         'cusip8']].drop_duplicates().to_csv('cik-cusip-maps.csv', index=False)
