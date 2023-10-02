# -*- coding: utf-8 -*-
"""PDF_Scholar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ytlgkVPJXLftHuIbotW3JxNb8a4ZbbT1
"""

!pip install PyPaperbot

import os

def scrape_google_scholar(query: str,
                          scholar_pages: str,
                          download_dir: str,
                          min_year: int,
                          ):
    """
    Wrapper for cmd line call for Google Scholar sraper

    Params:
        query : Query to be submitted to Google scholar
        scholar_pages : Number of pages to inspect. Each page has maximum of 10.
                        Total possible papers upper bounded by (scholar_pages x 10)
        download_dir : Directory to place downloaded files
        min_year : Minimum publication year to download

    Returns
        None
    """
    query_str = f'"{query}"'
    download_str = f'"{download_dir}"'

    cmd = f'python -m PyPaperBot --query={query_str} --scholar-pages={scholar_pages} --min-year={min_year} --dwn-dir={download_str}'

    os.system(cmd)

# Sample call
scrape_google_scholar(query = "supply chain",
                      scholar_pages = 1,
                      download_dir="/content/sample_data",
                      min_year = 1950)

!python -m PyPaperBot --query="supply chain" --scholar-pages=2 --dwn-dir="/content/sample_data"
