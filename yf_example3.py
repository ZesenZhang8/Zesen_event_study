"""
yf_example3.py

Module to download Qantas stock prices for a given year and save them to a CSV file.
"""

import os
import yf_example2
import toolkit_config as cfg

def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year into a CSV file.

    Parameters:
    year: The year for which to download the stock prices.

    Filename format: qan_prc_YYYY.csv, where YYYY is the year.

    The CSV file is saved under the data folder defined in toolkit_config module.
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    filename = f"qan_prc_{year}.csv"
    filepath = os.path.join(cfg.DATADIR, filename)
    yf_example2.yf_prc_to_csv(start=start_date, end=end_date, tic='QAN.AX', pth=filepath)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)
