## LINKEDIN POST — Project 3: ESG Performance Benchmarking

---

**I just finished my third portfolio project: ESG Performance Benchmarking across 430 S&P 500 companies. Here's what I found — including one result I didn't expect.**

---

I spent the last few weeks building a complete, end-to-end data analytics project on ESG (Environmental, Social, and Governance) performance. Every number below came from real, publicly available data — Sustainalytics ESG Risk Ratings accessed via Kaggle and GitHub. No fabricated values.

**The setup:**
430 S&P 500 companies · Sustainalytics ESG Risk Scores (~2024) · Python, Excel, Matplotlib, scikit-learn

---

**Finding 1: Sector is everything.**

One-way ANOVA: F = 27.978, p < 0.001.

Energy companies average an ESG risk score of 32.34 ("High" band). Real Estate companies average 13.09 ("Low" band). That's a gap of more than 19 points — nearly three full risk categories — just from sector membership. If you compare ESG scores across sectors without sector-relative normalisation, you're not measuring ESG performance. You're mostly measuring which industry you're in.

---

**Finding 2: Company size doesn't predict ESG quality — at least not here.**

The literature (Drempetic et al., 2020) shows larger firms tend to get better ESG ratings, largely because they have the reporting infrastructure smaller firms lack. I tested this in the S&P 500 using ln(employee count) vs ESG risk score.

Result: Pearson r = 0.051, p = 0.291. Not significant.

The S&P 500 is all large-cap. When every firm already has an ESG team and a sustainability report, the size-reporting advantage disappears. This is a scope condition for the existing literature, not a contradiction of it — and it matters for practitioners working exclusively within large-cap investment universes.

---

**Finding 3: Scores improved — but unevenly.**

I compared 216 companies that appear in both a 2021 Sustainalytics dataset and the 2024 dataset. Mean change: −1.50 points (i.e., improved). One-sample t-test: t = −5.826, p < 0.001. 66.7% of companies improved.

By sector:
🟢 Utilities improved most (Δ = −5.36), mainly through lower environmental risk scores
🔴 Energy is the only sector that got worse on average (Δ = +1.10)

Important caveat: Sustainalytics updated its methodology during this period. Some of the Utilities improvement may reflect methodology changes, not genuine operational improvement. I flagged this in the report.

---

**Finding 4: Three ESG archetypes emerge from clustering.**

K-Means with k=3 (selected by silhouette score = 0.366) identifies:

- 🟢 Low-Risk Leaders (n=197): Low overall risk, low environmental footprint. Mainly Technology and Real Estate. Mean composite score: 81.4.
- 🟡 Governance-Social Risk firms (n=107): Moderate total risk driven by social and governance exposure. Financial Services-heavy. Mean composite: 69.4.
- 🔴 Environmental Risk firms (n=126): Highest risk, driven by environmental scores. Energy, Materials, Utilities, Industrials. Mean composite: 61.4.

These archetypes suggest different strategy priorities — it's not enough to say a firm should "improve its ESG score." *Which* pillar needs attention depends entirely on which archetype the firm belongs to.

---

**The India connection:**

India's SEBI mandated BRSR Core reporting (with third-party assurance) for the top 150 listed companies from FY2023-24. I'm building a parallel hand-collected dataset from the FY2024-25 annual reports of 10 NIFTY large-cap companies across IT, banking, FMCG, cement, and automobiles — extracting GHG intensity, renewable energy share, female workforce share, and water intensity directly from BRSR disclosures.

The global benchmarks from this analysis provide the comparison point. The India data comes next.

---

**What I built:**
✔ 430-company dataset, cleaned and scored from scratch in Python  
✔ 10 publication-quality charts  
✔ 10-sheet Excel workbook with analysis, stat tests, and data quality log  
✔ 7,000-word research-style report with full APA 7 citations  
✔ BRSR Core extraction template for India spotlight (10 companies, FY2024-25)  
✔ Full GitHub documentation

All data sources are open and cited. All code is reproducible. All null findings are reported.

🔗 Full project on GitHub: [link]  
📄 Report and workbook available on request.

---

**One honest reflection:** I started this project with a plan to run a cross-provider ESG divergence analysis using MSCI, Sustainalytics, S&P Global, and LSEG data simultaneously. That plan collapsed when I realised those datasets aren't freely available in bulk. Changing the design mid-project — and being transparent about why — felt uncomfortable. It also felt like the right thing to do.

---

#DataAnalytics #ESG #Sustainability #BRSR #Python #DataScience #PortfolioProject #TISSMumbai #AnalyticsPortfolio #ESGInvesting #SustainableFinance

---

**[ALTERNATE SHORTER VERSION — for lower engagement / first post on a topic]**

Just completed a 430-company ESG benchmarking analysis using real Sustainalytics data from the S&P 500.

Three things I learned that surprised me:

1️⃣ Sector explains ESG risk far more than any individual company decision (ANOVA F=27.978, p<0.001). Comparing ESG scores across sectors without normalisation is misleading.

2️⃣ Company size doesn't predict ESG performance within the large-cap universe (r=0.051, p=0.291). The size-bias effect from the literature seems to require cross-cap-tier variation to show up.

3️⃣ 66.7% of companies improved their Sustainalytics scores between 2021 and 2024 — but Energy is the only sector that got worse on average.

K-Means clustering also identified three distinct ESG archetypes: Low-Risk Leaders, Governance-Social Risk firms, and Environmental Risk firms — each needing a different strategic response.

Full project → GitHub [link]
Tools: Python · Excel · Matplotlib · scikit-learn · SciPy

#DataAnalytics #ESG #Sustainability #BRSR #Python #PortfolioProject #TISSMumbai
