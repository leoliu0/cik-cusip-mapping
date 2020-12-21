# cik-cusip mapping

This repository produces the link between cik and cusip using EDGAR 13D and 13G fillings, that is more robust than Compustat (due to backward filling of new cusip to old records). It is a competitor to WRDS SEC platform while this one is free.

This is written in python36+, I don't provide a requirement file and I only use very common libraries, if you run into Module not Found problem, just pip install them

dl_idx.py will download the EDGAR index file containing addresses for each filing.

dl.py will download a certain type of filing, check form_type.txt for available filing types. for example,
```python
dl.py 13G 13G # this will download all 13G (second 13G) filing into 13G (first 13G) folder
```
```python
parse_cusip.py 13G # this will process all files in 13G directory, creating a file called 13G.csv with filing name, cik, cusip number.
```
```python
post-proc.py 13G # this will process 13G.csv, generate cusip6 and cusip8 fields, and output to cik-cusip-maps.csv.
```
```python
post-proc.py 13D # this will process 13D.csv, generate cusip6 and cusip8 fields, and output to cik-cusip-maps.csv.
```
Well, if you do not care obtaining the original data, just download cik-cusip-maps.csv, it has the mapping without timestamp information, but should be good if you use it for merging databases. Please deal with duplications yourself.

The reason why I do not provide timestamp is because there will be truncations due to timing of the filings. For example, when filings are filed in 2005 and 2007 for a link, I can only see the link in 2005 and 2007, but the link should be valid in 2006 too. One way to fix this is to interpolate the link to 2006. The bad situation is the link can be found in early years like 2006, but no more filings after that, then we do not know when should the link is valid to, or how long after we should extrapolate. Since this is arbitrary choice of the user, I will just remove the timestamp for you to deal with yourself. For database merging purpose, this should be fine because two databases you are merging should have timestamp and it's rare for duplicated links to exist at some given time. 

Insert filing date and filename into the csv as a record for tracing.