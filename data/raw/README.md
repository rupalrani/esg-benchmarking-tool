# Raw Data — Not Redistributed

This folder is where the primary dataset should be placed before running `analysis.py`.

**Primary dataset (required):** `SP 500 ESG Risk Ratings.csv`
Download from Kaggle: [S&P 500 ESG Risk Ratings](https://www.kaggle.com/datasets/pritish509/s-and-p-500-esg-risk-ratings) (Pritish, 2024)

**Temporal dataset (for 2021→2024 drift analysis):**
Clone into `data/raw/esg_yahoo_2021/`:
```bash
git clone https://github.com/sburstein/ESG-Stock-Data.git data/raw/esg_yahoo_2021
```

**Financial context dataset (optional, descriptive only):**
[S&P 500 Companies with Financial Information](https://www.kaggle.com/datasets/zinovadr/sp-500-companies-with-financial-information) (Zinovadr)

These datasets are not redistributed here in line with their respective licences — see the main README's Data Sources section for full citation details. Once placed, run:
```bash
python analysis.py
```
