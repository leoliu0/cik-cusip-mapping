# cik-cusip_link

This repository produces the link between cik and cusip using EDGAR 13D and 13G fillings, that is more robust than Compustat (due to forward filling of new cusip to old records) and WRDS provided links. This repository is simply a Python implementation of the existing R implementations with simplified codes.

dl_13D_13G.py will download all existing 13D and 13G

get_cusip_cik.py will produce a csv file that contains the links.
