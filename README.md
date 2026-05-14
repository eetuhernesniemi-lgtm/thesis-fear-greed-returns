README - Thesis Analysis
========================================================
Author: Eetu Hernesniemi
Thesis: Relationship Between the CNN Fear & Greed Index and Future Stock Market Returns
Tallinn University of Technology, 2026

EXECUTION ORDER
---------------
Step 0: Manual data download (see notes below)
Step 1: Run download_stocks2.py          -> produces sp500_monthly_returns.csv
Step 2: Run EDGAR_data_download.ipynb    -> produces edgar_panel_data.xlsx
Step 3: Run full_analysis_with_descriptives.ipynb -> reads all three input files
                                            from Google Drive, produces all
                                            tables and regression results

DATA LOADING
------------
The main analysis notebook (full_analysis_with_descriptives.ipynb) loads the
three input files directly from Google Drive — no manual file upload needed.
The share links at the top of Cell 1 point to the author's Google Drive copies:

  EDGAR_SHARE_URL   -> edgar_panel_data.xlsx
  RETURNS_SHARE_URL -> sp500_monthly_returns.csv
  FNG_SHARE_URL     -> fear_greed_index.csv

To use your own copies: upload the files to Google Drive, set sharing to
"Anyone with the link can view", and paste the share links into the three
SHARE_URL variables at the top of Cell 1.

MANUAL DOWNLOADS (not produced by code)
----------------------------------------
fear_greed_index.csv -- downloaded manually on 2026-05-02 from
https://www.kaggle.com/datasets/ashishpatel8736/historical-and-fear-greed-index-datasets
(Patel, A., 2024). No editing was done; the file was saved as-is from Kaggle.

NOTE ON TABLE 2
---------------
Table 2 (descriptive statistics) is produced by the descriptive
statistics cell in full_analysis_with_descriptives.ipynb.

NOTE ON TABLE 3
---------------
Table 3 (correlation matrix) is produced by the correlation
matrix cell in full_analysis_with_descriptives.ipynb.
