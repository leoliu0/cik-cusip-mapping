#!/usr/bin/python
import argparse
import csv
import os

import pandas as pd
import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filing", type=str)
    parser.add_argument("folder", type=str)

    user_agent = {"User-agent": "Mozilla/5.0"}

    args = parser.parse_args()
    filing = args.filing
    folder = args.folder

    full = pd.read_csv("full_index.csv", encoding="latin1")

    form = full[full.form.str.contains(filing)]

    len_ = len(form)
    print(len_)
    print("start to download")

    try:
        os.mkdir(folder)
    except:
        pass

    for n, row in enumerate(form.values):
        print(f"{n} out of {len_}")
        cik = row[0]
        firm = row[1]
        date = row[3]
        year = date.split("-")[0]
        month = date.split("-")[1]
        url = row[4].strip()
        try:
            os.mkdir(f"./{folder}/{year}_{month}")
        except:
            pass
        if os.path.exists(f"./{folder}/{year}_{month}/{cik}_{date}.html"):
            continue
        try:
            txt = requests.get(
                f"https://www.sec.gov/Archives/{url}", headers=user_agent, timeout=60
            ).text
            with open(
                f"./{folder}/{year}_{month}/{cik}_{date}.html", "w", errors="ignore"
            ) as f:
                f.write(txt)
        except:
            print(f"{cik}, {date} failed to download")
