#!/usr/bin/python
import argparse
import csv
import os
from pathlib import Path

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

    to_dl = []
    with open("full_index.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if filing in row["form"]:
                to_dl.append(row)

    len_ = len(to_dl)
    print(len_)
    print("start to download")

    for n, row in enumerate(to_dl):
        print(f"{n} out of {len_}")
        cik = row["cik"].strip()
        date = row["date"].strip()
        year = row["date"].split("-")[0].strip()
        month = row["date"].split("-")[1].strip()
        url = row["url"].strip()
        Path(f"./{folder}/{year}_{month}").mkdir(parents=True, exist_ok=True)
        if os.path.exists(f"./{folder}/{year}_{month}/{cik}_{date}.txt"):
            continue
        try:
            txt = requests.get(
                f"https://www.sec.gov/Archives/{url}", headers=user_agent, timeout=60
            ).text
            with open(
                f"./{folder}/{year}_{month}/{cik}_{date}.txt", "w", errors="ignore"
            ) as f:
                f.write(txt)
        except:
            print(f"{cik}, {date} failed to download")
