# cik-cusip mapping

This repository produces the link between cik and cusip using EDGAR 13D and 13G fillings, that is more robust than Compustat (due to forward filling of new cusip to old records). It is a competitor to WRDS SEC platform while this one is free.

This is written in python36+, I don't provide a requirement file and I only use very common libraries, if you run into Module not Found problem, just pip install them

dl_idx.py will download the EDGAR index file containing addresses for each filing.

dl.py will download a certain type of filing, check form_type.txt for available filing types. for example,
```python
dl.py 13G 13G # this will download all 13G (second 13G) filing into 13G (first 13G) folder
```

When you use this file, you should do a "left join" to your compustat (or other) datasets to exclude unnecessary links I created during clean process. As long as you do not create cik-fyear pairs that are not in the original datasets, it is fine.

To download latest mapping file, go to https://bit.ly/2HhZS8G
