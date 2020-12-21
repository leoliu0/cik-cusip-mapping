#!/usr/bin/python
import argparse
import csv
import os

import pandas as pd
import requests
OUT_PATH = '/datadrive'

parser = argparse.ArgumentParser()
parser.add_argument('filing', type=str)
parser.add_argument('folder', type=str)

args = parser.parse_args()

def main():
    filing = args.filing
    output_cusip_cik = os.path.join(OUT_PATH, 'cusip_cik_output')
    if not os.path.exists(output_cusip_cik):
        os.mkdir(output_cusip_cik)
    folder = os.path.join(output_cusip_cik, args.folder)
    full_idx_file = os.path.join(output_cusip_cik, 'full_index.csv')
    full = pd.read_csv(full_idx_file, encoding='latin1')

    form = full[full.form.str.contains(filing)]

    len_ = len(form)
    print(len_)
    print('start to download')

    try:
        os.mkdir(folder)
    except:
        pass

    for n, row in enumerate(form.values):
        print(f'{n} out of {len_}')
        cik = row[0]
        firm = row[1]
        date = row[3]
        year = date.split('-')[0]
        month = date.split('-')[1]
        url = row[4].strip()
        sub_folder = os.path.join(folder, f'{year}_{month}')
        try:
            os.mkdir(sub_folder)
        except:
            pass
        cik_file = os.path.join(sub_folder, f'{cik}_{date}.html')
        if os.path.exists(cik_file):
            continue
        try:
            txt = requests.get(f'https://www.sec.gov/Archives/{url}',
                               timeout=60).text
            with open(cik_file,
                      'w',
                      errors='ignore') as f:
                f.write(txt)
        except:
            print(f'{cik}, {date} failed to download')
if __name__ == '__main__':
    main()