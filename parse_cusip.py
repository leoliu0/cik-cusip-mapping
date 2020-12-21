import csv
import os
import re
import sys
import logging
from collections import *
from glob import glob
from multiprocessing import Pool

logging.getLogger().setLevel(logging.INFO)
OUT_PATH = '/datadrive'

files = sys.argv[1]
# pat = re.compile('[\( >][0-9A-Z]{1}[0-9]{4}[0-9A-Z]{1}\s*[0-9]{0,2}\s*[0-9]{0,1}[\) \n<]')
pat = re.compile('[\( >][0-9A-Z]{1}[0-9]{3}[0-9A-Za-z]{2}[- ]*[0-9]{0,2}[- ]*[0-9]{0,1}[\) \n<]')
w = re.compile('\w+')

def parse(file):
    with open(file,'r') as f:
        a = f.readlines()

    record = 0
    cik = None
    for x in a:
        if 'SUBJECT COMPANY' in x:
            record = 1
        if 'CENTRAL INDEX KEY' in x and record == 1:
            cik = x.split('CENTRAL INDEX KEY:')[1].split('\n')[0].strip()
            logging.info(f"CIK is: {cik}")
            #cik = x.split('\t\t\t')[-1].strip()
            break

    date = None
    for x in a:
        if 'FILED AS OF DATE' in x:
            date = x.split('FILED AS OF DATE:')[1].split('\n')[0].strip()
            break
    cusips = []
    record = 0
    for x in a:
        if '<DOCUMENT>' in x:
            record = 1
        if record == 1:
            y = pat.findall(x)
            if y:
                cusips.append(y[0].strip().strip('<>'))

    if len(cusips)==0:
        cusip=None
    else:
        cusip = Counter(cusips).most_common()[0][0]
        cusip = ''.join(w.findall(cusip))
    fn = file.split('/')[-1]
    return [fn,date, cik,cusip]

def main():
    output_cusip_cik = os.path.join(OUT_PATH, 'cusip_cik_output')
    with Pool(30) as p:
        with open(f'{files}.csv','w') as w:
            wr = csv.writer(w)
            for res in p.imap(parse,glob(os.path.join(output_cusip_cik,f'{files}/*/*')),chunksize=100):
                wr.writerow(res)

if __name__=='__main__':
    main()
