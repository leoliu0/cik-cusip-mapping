import argparse
import csv
import os

import pandas as pd
import requests
OUT_PATH = '/datadrive'
def main():
    output_cusip_cik = os.path.join(OUT_PATH, 'cusip_cik_output')
    if not os.path.exists(output_cusip_cik):
        os.mkdir(output_cusip_cik)
    idx_file = os.path.join(output_cusip_cik, 'master.idx')

    with open(idx_file, 'wb') as f:
        for year in range(1994, 2023):
            for q in range(1, 5):
                print(year, q)
                content = requests.get(
                    f"https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{q}/master.idx"
                ).content
                f.write(content)
    full_idx_file = os.path.join(output_cusip_cik, 'full_index.csv')
    with open(full_idx_file, 'w', newline='', errors='ignore') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(['cik', 'comnam', 'form', 'date', 'url'])
        with open(idx_file, 'r', encoding='latin1') as f:
            for r in f:
                if '.txt' in r:
                    wr.writerow(r.split('|'))

if __name__=='__main__':
    main()