import sys

import pandas as pd

df = pd.read_csv(sys.argv[1], names=['f','cik','cusip']).dropna()

df['leng'] = df.cusip.map(len)

df = df[(df.leng==6) | (df.leng==8) | (df.leng==9)]

df['cusip6'] = df.cusip.str[:6]

df['cusip8'] = df.cusip.str[:8]
df.cik = pd.to_numeric(df.cik)

df = df[['cik','cusip6','cusip8']].drop_duplicates(
            ).to_csv('cik-cusip-maps.csv',index=False)
