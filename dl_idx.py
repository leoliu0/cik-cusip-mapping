import argparse
import csv
import os

import pandas as pd
import requests

with open(f'master.idx', 'wb') as f:
    for year in range(1994, 2023):
        for q in range(1, 5):
            print(year, q)
            content = requests.get(
                f"https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{q}/master.idx"
            ).content
            f.write(content)

with open('full_index.csv', 'w', newline='', errors='ignore') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(['cik', 'comnam', 'form', 'date', 'url'])
    with open('master.idx', 'r', encoding='latin1') as f:
        for r in f:
            if '.txt' in r:
                wr.writerow(r.split('|'))
