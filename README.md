# cik-cusip mapping

This repository produces the link between cik and cusip using EDGAR 13D and 13G fillings, that is more robust than Compustat (due to forward filling of new cusip to old records) and WRDS provided links. This repository is simply a Python implementation of the existing R implementations with simplified codes.

dl_13D_13G.py will download all existing 13D and 13G.

produce_links.ipynb will produce a csv file that extract cusip from fillings.

clean_links.ipynb will clean the csv file, including classifying cusip into cik-fiscal year pair, interpolate and fill to a full 1993-2018 mapping. 

When you use this file, you should do a "left join" to your compustat (or other) datasets to exclude unnecessary links I created during clean process. As long as you do not create cik-fyear pairs that are not in the original datasets, it is fine.

To download latest mapping file, go to https://bit.ly/2HhZS8G
