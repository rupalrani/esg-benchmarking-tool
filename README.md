# 🌿 ESG Performance Benchmarking Tool

> Sector-relative ESG scoring framework for S&P 500 firms using real Sustainalytics and Yahoo Finance data — aligned to IFRS S1/S2, TCFD, and GRI standards. Key finding: **sector explains ~40% of ESG score variance**.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

---

## 📌 Overview

This project constructs an **end-to-end ESG performance benchmarking system** using open-access S&P 500 Sustainalytics ESG scores and Yahoo Finance financial data. Rather than raw ESG scores, this tool calculates **sector-relative ESG scores** — accounting for the well-documented fact that sector membership is the dominant driver of ESG performance.

The framework aligns to three major disclosure standards:
- **IFRS S1/S2** (International Sustainability Standards Board)
- **TCFD** (Task Force on Climate-related Financial Disclosures)
- **GRI** (Global Reporting Initiative)

Outputs include a publication-ready academic paper (targeted at *Finance Research Letters*), a 12-sheet Excel research workbook, an interactive Power BI scorecard, and LinkedIn-ready infographic content.

---

## 🏆 Key Results

| Finding | Value |
|---------|-------|
| Variance in ESG scores explained by sector | **~40%** (R² from sector fixed-effects model) |
| Data source | S&P 500 Sustainalytics ESG scores + Yahoo Finance |
| Framework alignment | IFRS S1/S2 · TCFD · GRI |
| Journal target | *Finance Research Letters* |
| Excel workbook sheets | 12 |
| Output formats | Power BI scorecard · Academic paper · LinkedIn infographic · SQL scripts |

---

## 🔍 Methodology

```
1. Data Collection
   ├── Sustainalytics ESG scores for S&P 500 constituents (open access)
   └── Yahoo Finance: market cap, sector, financial ratios

2. Data Cleaning & SQL Processing
   ├── Sector classification harmonisation (GICS standard)
   ├── Handling missing ESG sub-scores (E, S, G pillars)
   └── Merging financial and ESG datasets

3. Sector-Relative Scoring
   ├── Compute sector mean and standard deviation for each ESG pillar
   ├── Z-score normalisation within sector groups
   └── Composite sector-relative ESG score construction

4. Statistical Analysis
   ├── OLS regression: ESG score ~ sector dummies (sector explains ~40% variance)
   ├── Correlation: ESG scores vs financial performance (ROE, leverage, market cap)
   └── Sector-level benchmarking tables

5. Framework Alignment
   ├── Map E pillar → TCFD climate metrics
   ├── Map S pillar → GRI 400 Social Standards
   └── Map G pillar → IFRS S1 governance disclosures

6. Visualisation & Output
   ├── Power BI interactive scorecard (sector drilldowns, firm-level comparison)
   ├── 12-sheet Excel workbook (data, analysis, benchmarking, references)
   └── Academic paper draft (~Finance Research Letters format)
```

---

## 📁 Repository Structure

```
esg-benchmarking-tool/
│
├── README.md
├── requirements.txt
│
├── scripts/
│   ├── 01_data_collection.py        # Sustainalytics + Yahoo Finance data pull
│   ├── 02_data_cleaning.py          # ETL, sector harmonisation, merging
│   ├── 03_sector_relative_scoring.py # Z-score normalisation; composite score
│   ├── 04_regression_analysis.py    # OLS regression; sector variance decomposition
│   ├── 05_framework_mapping.py      # IFRS S1/S2, TCFD, GRI pillar alignment
│   └── sql_queries.sql              # SQL for data aggregation and benchmarking
│
├── data/
│   └── README.md                    # Data sources and download instructions
│
└── outputs/
    └── README.md                    # Dashboard screenshots and chart exports
```

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Data Sources

🔗 **ESG Scores (Sustainalytics via Kaggle):** [S&P 500 ESG Risk Ratings — pritish509](https://www.kaggle.com/datasets/pritish509/s-and-p-500-esg-risk-ratings)  
🔗 **ESG + Stock Data (Yahoo Finance sourced):** [S&P 500 ESG and Stocks Data 2023–24 — rikinzala](https://www.kaggle.com/datasets/rikinzala/s-and-p-500-esg-and-stocks-data-2023-24)  
🔗 **Yahoo Finance financial data:** Fetched live via the `yfinance` Python library (no download needed)

Download the ESG dataset CSV and place it in the `data/` folder. The `yfinance` library handles financial data automatically during script execution.

### Run the Pipeline
```bash
# Step 1: Collect data
python scripts/01_data_collection.py

# Step 2: Clean and merge
python scripts/02_data_cleaning.py

# Step 3: Build sector-relative scores
python scripts/03_sector_relative_scoring.py

# Step 4: Regression and statistical analysis
python scripts/04_regression_analysis.py

# Step 5: Map to disclosure frameworks
python scripts/05_framework_mapping.py
```

---

## 📊 Key Outputs

| Output | Description |
|--------|-------------|
| Power BI Scorecard | Interactive firm + sector ESG benchmarking dashboard |
| Academic Paper | Draft formatted for *Finance Research Letters* |
| Excel Workbook | 12 sheets: data, EDA, regression, sector tables, references |
| LinkedIn Infographic | Visual summary of key ESG findings for public sharing |
| SQL Scripts | Reproducible data extraction and aggregation queries |

---

## 📐 Framework Alignment

| ESG Pillar | Standard |
|-----------|---------|
| Environmental (E) | TCFD — physical + transition risk metrics |
| Social (S) | GRI 400 series — labour, community, human rights |
| Governance (G) | IFRS S1 — board composition, transparency, accountability |
| Integrated | IFRS S2 — climate-related disclosure requirements |

---

## 👩‍💻 About

Developed as **Portfolio Project 3** — part of an end-to-end analytics portfolio built during BS Analytics & Sustainability Studies at TISS Mumbai.

📫 [rupalrani2303@gmail.com](mailto:rupalrani2303@gmail.com) · [LinkedIn](https://www.linkedin.com/in/rupal-rani-a23b36257) · [GitHub](https://github.com/rupalrani)
