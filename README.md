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
Well, if you do not care obtaining the original data, just download cik-cusip-maps.csv, it has the mapping without timestamp information, but should be good if you use it for merging databases. Please deal with duplications yourself.
