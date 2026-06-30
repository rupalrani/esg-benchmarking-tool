# ESG Performance Benchmarking: A Cross-Sector Analysis of S&P 500 Companies with a BRSR Regulatory Spotlight on India

**Author:** Rura  
**Affiliation:** School of Management and Labour Studies, Tata Institute of Social Sciences (TISS), Mumbai  
**Programme:** BSc Analytics and Sustainability Studies  
**Date:** June 2025  
**Dataset:** Sustainalytics ESG Risk Ratings (~2024), S&P 500; temporal comparison with Sustainalytics 2021 data  
**Tools:** Python 3.12 · Excel (openpyxl) · Matplotlib · Seaborn · scikit-learn · SciPy  
**Repository:** [github.com/rura/project3-esg-benchmarking] *(link to be updated on upload)*

---

## Abstract

This study benchmarks the environmental, social, and governance (ESG) risk profiles of 430 S&P 500 companies using Sustainalytics ESG Risk Ratings. Four analytical questions are addressed: (1) Do ESG risk scores differ significantly across Global Industry Classification Standard (GICS) sectors? (2) Is company size a reliable predictor of ESG performance among large-cap firms? (3) How have Sustainalytics scores evolved between 2021 and 2024 for the same set of companies? (4) Can unsupervised clustering identify meaningful ESG performance archetypes? Findings reveal highly significant sector-level heterogeneity (one-way ANOVA: F = 27.978, p < 0.001), with Energy companies carrying the greatest risk (mean = 32.34) and Real Estate the least (mean = 13.09). Contrary to the cross-cap literature, company size does not predict ESG performance within the S&P 500 sample (Pearson r = 0.051, p = 0.291). A temporal analysis of 216 overlapping firms shows a statistically significant mean improvement of 1.50 points between 2021 and 2024 (t = −5.826, p < 0.001), with Utilities and Materials sectors showing the largest gains. K-means clustering (k = 3, silhouette = 0.366) identifies three distinct ESG archetypes: Low-Risk Leaders (n = 197), Governance-Social Risk firms (n = 107), and Environmental Risk firms (n = 126). A composite ESG performance score, constructed using OECD normalisation with E/S/G weights of 40/30/30, classifies 108 companies as Leaders and 108 as Laggards; sensitivity analysis confirms the classification is robust to equal weighting (r = 0.988, only 35 reclassified). The study concludes with a regulatory spotlight comparing these global findings with India's Business Responsibility and Sustainability Reporting (BRSR) Core framework, currently mandated for the top 150 listed companies.

**Keywords:** ESG benchmarking · Sustainalytics · sector analysis · composite scoring · BRSR · SEBI · size bias · temporal drift · K-means clustering

---

## 1. Introduction

Environmental, social, and governance (ESG) analysis has moved from niche ethical investing to mainstream corporate finance. As of 2024, global assets managed under ESG criteria exceeded USD 30 trillion, and major regulators — from the US Securities and Exchange Commission to the European Securities and Markets Authority — have introduced or tightened non-financial disclosure requirements (GSIA, 2023). In India, the Securities and Exchange Board of India (SEBI) mandated the Business Responsibility and Sustainability Report (BRSR) for the top 1,000 listed companies from FY2022-23, and introduced BRSR Core — a verified subset of key performance indicators — for the top 150 companies from FY2023-24 (SEBI, 2023).

Despite this regulatory momentum, several empirical questions remain contested. Do ESG scores vary systematically by industry, or is the distribution roughly uniform? Does firm size explain ESG performance, as some studies suggest, or does this relationship dissolve within segments of similarly-sized companies? Are ESG scores trending in a consistent direction, or is cross-company divergence growing? Can clustering algorithms identify meaningful sub-groups of ESG performance that simple score rankings miss?

This project addresses these four questions using real, publicly available data — Sustainalytics-based ESG Risk Ratings for 430 S&P 500 companies — with a secondary temporal analysis comparing 2021 and 2024 scores for 216 overlapping firms. The methodology is fully transparent and reproducible; all data sources are cited, all code is published, and all null findings are reported alongside positive ones.

### 1.1 Research Questions

**RQ1.** Do Sustainalytics ESG risk scores differ significantly across GICS sectors among S&P 500 companies?

**RQ2.** Is company size (measured by full-time employee count) a statistically significant predictor of ESG risk score within the S&P 500?

**RQ3.** How have Sustainalytics ESG scores changed between 2021 and 2024, and does this trend vary by sector?

**RQ4.** Can K-means clustering of E/S/G pillar scores identify distinct and interpretable ESG performance archetypes?

---

## 2. Literature Review

### 2.1 ESG Ratings: Construction and Disagreement

ESG ratings are composite scores that aggregate company-level data on environmental footprint, labour practices, board governance, and related dimensions into a single metric or set of metrics. The methodology varies substantially across providers. Sustainalytics measures unmanaged ESG risk — the gap between a company's total exposure to material ESG issues and its management of those issues — on a numerical scale where lower is better (Sustainalytics, 2023). MSCI assigns industry-relative letter ratings from AAA to CCC based on how well companies manage financially relevant sustainability risks compared to sector peers (MSCI, 2024). S&P Global ESG Scores evaluate performance against 630+ data points drawn from company disclosures and engagement (S&P Global, 2024).

A key challenge is inter-provider disagreement. Berg, Koelbel, and Rigobon (2022) analyse ratings from six major providers and find that pairwise correlations range from 0.38 to 0.71 — a level of disagreement that is extraordinary given that all providers claim to measure the same underlying construct. The authors decompose this divergence into scope disagreement (which issues are included), measurement disagreement (how similar indicators are operationalised), and weight disagreement. Scope and measurement account for the majority of divergence. Gibson Brandon, Krueger, and Schmidt (2021) further show that ESG disagreement creates systematic noise in ESG-return studies, complicating causal inference. Christensen, Hail, and Leuz (2021) argue that mandatory disclosure regimes are one mechanism through which measurement quality can be improved, since they standardise what data companies must report. These findings motivate this project's single-provider focus (Sustainalytics), which holds measurement methodology constant throughout the analysis.

### 2.2 ESG and Financial Performance

A meta-analysis of 2,200 empirical studies by Friede, Busch, and Bassen (2015) finds that approximately 90% of studies report a non-negative relationship between ESG performance and corporate financial performance, with the majority showing positive results. The relationship is strongest for governance factors and in the context of portfolio-level analysis rather than individual company studies. More recent work has complicated this picture: Atz, Van Holt, Liu, and Bruno (2023) distinguish between correlation studies (which frequently find a positive link) and quasi-experimental studies exploiting exogenous variation (which find more modest and heterogeneous effects). The consensus is that ESG may reduce idiosyncratic risk and cost of capital while not necessarily generating abnormal returns after controlling for known risk factors.

For this study, the primary dataset's financial data is a 2019 vintage and therefore not suitable for ESG-return regressions. Financial metrics (P/E, market cap) are included as contextual variables only, and no causal ESG-performance claims are made.

### 2.3 Size Bias in ESG Ratings

Drempetic, Klein, and Zwergel (2020) document a systematic size bias in ESG ratings: larger companies tend to receive higher ESG scores, even after controlling for actual sustainability performance. The authors attribute this to reporting capacity — large firms have dedicated sustainability teams, external assurance, and established data pipelines, while smaller firms may struggle to comply with extensive disclosure requirements. Liang and Renneboog (2017) show that this effect operates across countries and is partially explained by institutional factors (investor attention, analyst coverage). Within the S&P 500 — a large-cap index — the size variation is far more compressed than across the full market cap distribution, making the size-bias effect harder to detect empirically. This project explicitly tests for size bias within this constrained sample, making a null finding an informative result rather than a failure.

### 2.4 ESG Score Dynamics and Temporal Trends

The temporal dynamics of ESG ratings remain understudied relative to the cross-sectional literature. Serafeim and Yoon (2022) show that changes in ESG scores — rather than levels — predict future abnormal returns, suggesting that analysts and investors respond to rating momentum. However, Sustainalytics has updated its methodology multiple times between 2021 and 2024, meaning that apparent score improvements may partly reflect methodological changes rather than genuine company-level progress. This caveat is reflected in the study's limitation section. Nonetheless, the direction and distribution of score changes across sectors provides useful descriptive evidence about which industries have been most active in reducing disclosed ESG risk during this period.

### 2.5 India's BRSR Framework

India's BRSR framework, introduced in 2021 and progressively strengthened through 2023-24, represents one of the most ambitious ESG disclosure mandates in Asia. Aligned with the nine Principles of the National Guidelines on Responsible Business Conduct (NGRBC), the BRSR requires companies to report against a broad set of environmental, social, and governance indicators. The BRSR Core sub-framework, effective from FY2023-24 for the top 150 companies, mandates nine specific key performance indicators (KPIs) — covering greenhouse gas emissions, water consumption, energy use, waste generation, gender diversity, employee wages, inclusive development, customer disclosure, and openness of business — and requires reasonable third-party assurance for these nine KPIs (SEBI, 2023).

This regulatory architecture provides the contextual backdrop for this project's India spotlight, in which BRSR Core indicators are manually extracted from the FY2024-25 annual reports of ten NIFTY large-cap companies across five sectors. While this spotlight dataset is too small for statistical inference, it enables a qualitative comparison of India's emerging ESG disclosure landscape against the global Sustainalytics benchmarks established in the primary analysis.

---

## 3. Data and Methodology

### 3.1 Primary Dataset

The primary dataset is the S&P 500 ESG Risk Ratings dataset, sourced from Kaggle (Pritish, 2024; dataset ID: pritish509/s-and-p-500-esg-risk-ratings) and accessed via a GitHub mirror (ggogitidze/SP-500-ESG). This dataset contains Sustainalytics-based ESG risk scores for S&P 500 constituent companies. Sustainalytics computes ESG Risk Ratings on a continuous 0-to-100+ scale; scores below 10 are classified as Negligible risk, 10-19.9 as Low, 20-29.9 as Medium, 30-39.9 as High, and 40+ as Severe (Sustainalytics, 2023). The dataset includes total ESG risk score, pillar-level scores (Environment, Social, Governance), controversy level and score, ESG risk percentile, risk level classification, sector, industry, and full-time employee count.

The raw dataset contains 503 rows. After excluding 73 companies with missing ESG scores and 1 company with a missing sector label, the analytical sample comprises **430 companies** across 11 GICS sectors. The 73 missing rows (14.5%) represent a limitation: they may not be missing at random, given that lower-coverage firms often have less analyst attention and may differ systematically in size or sector. This is noted explicitly in the data quality log and in the limitations section of this report.

A supplementary financial dataset (S&P 500 Constituents Financials; Zinovadr, Kaggle) containing market capitalisation, P/E ratio, price-to-book, EPS, and dividend yield for 505 companies was merged on the company ticker. Of the 430 analytical companies, 368 (85.6%) matched to financial data. This financial dataset is a 2019 vintage and is used for contextual description only.

### 3.2 Temporal Dataset

For the temporal analysis (RQ3), the Yahoo Finance ESG dataset scraped by sburstein (2021) and hosted at github.com/sburstein/ESG-Stock-Data was used. This dataset contains Sustainalytics-based ESG scores for 245 S&P 500 companies as of 1 March 2021. The overlap between the primary dataset and this temporal dataset is 216 companies. **Because both datasets use Sustainalytics methodology**, this analysis measures how the same provider's scores changed between 2021 and ~2024, not cross-provider divergence. This framing is explicitly maintained throughout the analysis. Sustainalytics updated its methodology during this period, meaning that some score changes may reflect methodological revision rather than genuine improvement or deterioration.

### 3.3 Composite ESG Performance Score

To convert Sustainalytics risk scores — where lower is better — into a composite performance score where higher is better, the following procedure was applied following OECD (2008) guidance on composite indicator construction:

1. **Normalisation.** Each pillar score (Environment, Social, Governance) was normalised to a 0-100 scale using Min-Max normalisation:  
   `norm_i = (x_i - x_min) / (x_max - x_min) × 100`

2. **Inversion.** Because higher Sustainalytics scores represent more risk (worse performance), each normalised pillar score was inverted:  
   `inverted_i = 100 - norm_i`

3. **Weighted aggregation.** A composite score was computed as:  
   `Composite = 0.40 × E_inv + 0.30 × S_inv + 0.30 × G_inv`

   The 40/30/30 weighting was chosen to reflect the relative emphasis on environmental indicators in SEBI's BRSR Core framework and the broader regulatory focus on Scope 1/2 emissions, energy, and water. An equal-weight scenario (33.3% each) was computed for sensitivity analysis.

4. **Classification.** Companies were classified as Leaders (composite ≥ 75th percentile), Laggards (composite ≤ 25th percentile), or Average (all others).

### 3.4 Statistical Tests

**Sector differences (RQ1).** A one-way ANOVA was used to test whether mean total ESG risk scores differ significantly across the 11 GICS sectors. The Kruskal-Wallis H-test (a non-parametric alternative that does not assume normality) was applied as a robustness check.

**Size bias (RQ2).** The natural logarithm of full-time employee count was computed to reduce right-skew. Pearson and Spearman correlations were calculated between ln(employees) and total ESG risk score. An OLS simple linear regression of ESG risk on ln(employees) was estimated. The logarithmic transformation follows Drempetic et al. (2020).

**Temporal drift (RQ3).** The change in ESG risk score for each of 216 overlapping companies (Δ = 2024 score − 2021 score) was computed. A one-sample t-test assessed whether the mean Δ is significantly different from zero. Sector-level mean changes were computed descriptively.

**Clustering (RQ4).** K-means clustering was applied to the three normalised and inverted pillar scores. The number of clusters was selected by maximising the average silhouette score over k ∈ {2, 3, 4, 5, 6}. Principal Component Analysis (PCA) was used to project cluster assignments onto two dimensions for visualisation, retaining 86.1% of variance in two components.

**Weight sensitivity.** Pearson correlation between the primary weighted composite and the equal-weight composite was computed. The number of companies changing classification tier under equal weighting was counted.

---

## 4. Results

### 4.1 Descriptive Statistics

The 430 companies in the analytical sample have a mean Sustainalytics ESG Risk Score of **21.53** (SD = 6.89), consistent with the "Medium" risk band (20-30). The distribution is roughly unimodal and slightly right-skewed, with a median of 21.05. The most common classification is Low risk (187 companies, 43.5%), followed by Medium (184, 42.8%), High (50, 11.6%), Negligible (6, 1.4%), and Severe (3, 0.7%). The preponderance of Low and Medium ratings reflects the composition of the S&P 500: a large-cap, largely US-listed index in which most companies have material ESG disclosure programs.

At the pillar level, Environment risk (mean = 6.49, SD = 5.45) shows the greatest dispersion, reflecting substantial variation between sectors such as Energy (mean Environment = 16.92) and Financial Services (mean = 1.41). Social risk (mean = 8.68, SD = 2.81) is the largest contributor to overall risk scores on average. Governance risk (mean = 6.73, SD = 2.21) is the most consistent across sectors.

### 4.2 Sector Analysis (RQ1)

Sector-level mean ESG risk scores, sorted from highest to lowest risk, are as follows:

| Sector | N | Mean Total | Mean Env | Mean Soc | Mean Gov |
|--------|---|-----------|---------|---------|---------|
| Energy | 20 | 32.34 | 16.92 | 8.93 | 6.50 |
| Basic Materials | 19 | 26.72 | 12.62 | 7.54 | 6.57 |
| Utilities | 28 | 26.71 | 11.81 | 9.44 | 5.47 |
| Consumer Defensive | 33 | 25.45 | 8.73 | 10.84 | 5.87 |
| Industrials | 60 | 24.01 | 7.10 | 10.84 | 6.08 |
| Financial Services | 63 | 21.19 | 1.41 | 9.63 | 10.14 |
| Healthcare | 53 | 20.58 | 1.79 | 11.48 | 7.31 |
| Comm. Services | 14 | 19.41 | 1.86 | 10.14 | 7.41 |
| Consumer Cyclical | 51 | 19.23 | 5.30 | 8.39 | 5.55 |
| Technology | 61 | 16.92 | 4.29 | 6.88 | 5.76 |
| Real Estate | 28 | 13.09 | 3.69 | 3.64 | 5.75 |

*Table 1. Mean Sustainalytics ESG Risk Scores by GICS Sector (S&P 500, ~2024, N=430). Lower score = lower ESG risk (better performance). Sustainalytics scale: Negligible <10, Low 10–20, Medium 20–30, High 30–40, Severe 40+.*

Energy companies carry the highest ESG risk by a substantial margin (mean = 32.34, "High" band), driven overwhelmingly by environmental exposure (mean Environment score = 16.92). Basic Materials and Utilities follow, both characterised by significant physical-world environmental footprints — mining, cement, chemicals for the former; power generation and grid infrastructure for the latter. Financial Services has the highest Governance risk of any sector (mean = 10.14), reflecting material exposure to regulatory compliance, data security, and systemic risk considerations. Healthcare has the highest Social risk (mean = 11.48), consistent with its exposure to clinical trial practices, drug pricing, and supply-chain labour issues.

Real Estate shows the lowest overall ESG risk (mean = 13.09, "Low" band), a finding that at first appears counterintuitive. The result is interpretable, however: REITs primarily hold and operate buildings rather than manufacturing or extracting resources, limiting their direct environmental footprint on the Sustainalytics methodology. High Environmental risk in the Energy sector (16.92) is more than four times the equivalent figure in Real Estate (3.69), illustrating the degree to which sector membership drives ESG risk profiles.

A one-way ANOVA confirms that these sector differences are statistically significant: **F(10, 419) = 27.978, p < 0.001**. The Kruskal-Wallis H-test, which makes no distributional assumptions, reinforces this result: **H(10) = 170.288, p < 0.001**. Sector membership is therefore a dominant structural driver of ESG risk in this sample, consistent with the material-issue mapping that underpins Sustainalytics' methodology (which assigns different issue weights by industry).

### 4.3 Composite Score and Classification

The composite ESG performance score, constructed using the OECD normalisation and inversion procedure, has a mean of 67.8 (SD = 11.2) on the 0-100 scale. The 75th percentile threshold is 74.7 (Leader) and the 25th percentile is 60.9 (Laggard). The classification yields:

- **Leaders (n = 108):** Composite score ≥ 74.7
- **Average (n = 214):** Composite score 60.9 – 74.7
- **Laggards (n = 108):** Composite score ≤ 60.9

The ten highest-scoring companies by composite score are: Hasbro (94.9), Keysight Technologies (93.6), CBRE Group (93.2), CDW Corporation (91.8), Accenture (90.9), AvalonBay Communities (90.2), The Interpublic Group (90.0), Robert Half (90.0), Crown Castle (89.8), and Prologis (89.7). These leaders span Consumer Cyclical, Technology, Real Estate, Industrials, and Communications — sectors where either physical-world environmental exposure is low or where management practices are particularly strong relative to peers.

The ten lowest-scoring companies are: Exxon Mobil (40.3), Occidental Petroleum (40.4), General Electric (42.6), APA Corporation (44.5), Boeing (46.2), Marathon Oil (46.4), TransDigm Group (46.5), Wells Fargo (47.4), Chevron (47.7), and 3M (48.4). Energy companies dominate, with four of the five highest-risk firms in the sector appearing in this list. Boeing and GE reflect significant industrial and supply-chain controversies; Wells Fargo and 3M carry legacy legal and environmental liabilities, respectively.

### 4.4 Weight Sensitivity

The primary composite (E=40%, S=30%, G=30%) and the equal-weight composite (E=S=G=33.3%) are almost perfectly correlated: Pearson r = **0.988**. Under equal weighting, only **35 of 430 companies** (8.1%) change classification tier (e.g., from Leader to Average or Average to Laggard). This confirms that the composite classification is robust to the specific choice of weights within a reasonable range, and that results are not an artefact of the weighting scheme.

### 4.5 Size Bias Test (RQ2)

Among the 425 companies with non-missing employee data, the Pearson correlation between ln(full-time employees) and total ESG risk score is **r = 0.051 (p = 0.291)** — not statistically significant at conventional thresholds. The Spearman rank correlation is similarly negligible: **ρ = 0.031 (p = 0.520)**. An OLS regression of ESG risk on ln(employees) yields a slope of β = 0.253 with r² = 0.003, indicating that company size explains less than 0.3% of ESG score variance in this sample.

This null finding is informative. The Drempetic et al. (2020) size-bias effect is documented across the full market-cap distribution, from micro-cap to mega-cap. Within the S&P 500 — where the smallest company (2019 market cap data) is approximately USD 2.6 billion and the largest USD 809 billion — the variation in company size is substantially compressed relative to the full market. The signal that drives the cross-market size bias (the inability of small companies to build reporting infrastructure) is largely absent when all companies are large enough to have meaningful ESG disclosure teams. This interpretation is consistent with the data and does not contradict Drempetic et al.; rather, it establishes a scope condition for when the effect holds.

### 4.6 Temporal Drift Analysis (RQ3)

For 216 companies present in both the 2021 (sburstein/ESG-Stock-Data) and ~2024 (primary dataset) Sustainalytics data, the mean change in total ESG risk score is **Δ = −1.495** (standard deviation = 3.77). A one-sample t-test confirms this is significantly different from zero: **t(215) = −5.826, p < 0.001**. On average, companies in this sample reduced their Sustainalytics ESG risk scores by approximately 1.5 points over three years. A negative Δ represents improvement (lower risk), so 66.7% of companies improved their scores while 32.4% worsened.

The sector-level drift varies substantially:

| Sector | N | Mean Δ Total | Mean Δ Env | Mean Δ Soc | Mean Δ Gov |
|--------|---|-------------|----------|----------|----------|
| Energy | 7 | +1.100 | +1.100 | −0.529 | +0.129 |
| Consumer Staples | 9 | +0.700 | +0.744 | +0.178 | −0.133 |
| Comm. Services | 10 | −0.060 | +0.740 | +0.040 | −0.840 |
| Consumer Discretionary | 25 | −0.376 | −0.192 | +0.264 | −0.456 |
| Financials | 19 | −0.437 | −0.237 | −0.316 | +0.121 |
| Industrials | 32 | −0.903 | +0.028 | −0.531 | −0.556 |
| Information Technology | 42 | −1.255 | +0.543 | −1.267 | −0.400 |
| Real Estate | 23 | −1.874 | −0.770 | −1.326 | +0.391 |
| Health Care | 24 | −3.175 | −0.446 | −1.704 | −1.071 |
| Materials | 10 | −3.740 | −2.020 | −1.580 | −0.210 |
| Utilities | 15 | −5.360 | −3.407 | −1.487 | −0.613 |

*Table 2. Mean Change in Sustainalytics ESG Risk Score (2021 → 2024) by Sector. Negative Δ = improvement.*

Utilities show the largest improvement (Δ = −5.36), concentrated in the Environmental pillar (−3.41), which is consistent with substantial renewable energy investment by US utilities between 2021 and 2024 as well as possible Sustainalytics methodology updates for this sector. Materials (Δ = −3.74) and Health Care (Δ = −3.18) also show meaningful gains. Energy is the only sector to worsen on average (+1.10), driven entirely by increasing environmental risk scores; this is consistent with the sector's continued exposure to fossil-fuel liabilities and ongoing litigation in this period.

An important caveat: Sustainalytics revised elements of its methodology during this period, particularly around sector-level issue weighting. Some portion of the score changes — especially for Utilities, which experienced the largest shift — may reflect methodological revision rather than genuine company-level progress. This limits causal conclusions from the temporal analysis.

### 4.7 K-Means Clustering (RQ4)

K-means clustering on the three normalised and inverted pillar scores (Environment, Social, Governance) across 430 companies identifies **k = 3** as the optimal number of clusters, based on the maximum average silhouette score (silhouette = 0.366 at k = 3, versus 0.355 at k = 2 and 0.346 at k = 4). PCA reduces the three-dimensional cluster space to two components explaining 86.1% of total variance (PC1: 48.8%, PC2: 37.3%), confirming that the data has substantial lower-dimensional structure.

The three clusters have the following profiles:

| Cluster | N | Label | Mean ESG Total | Mean Env | Mean Soc | Mean Gov | Mean Composite |
|---------|---|-------|---------------|---------|---------|---------|----------------|
| 0 | 197 | Low-Risk Leaders | 15.83 | 3.53 | 6.61 | 5.69 | 81.39 |
| 1 | 107 | Governance-Social Risk | 23.54 | 2.04 | 12.17 | 9.34 | 69.43 |
| 2 | 126 | Environmental Risk | 28.74 | 12.33 | 10.29 | 6.12 | 61.44 |

*Table 3. K-Means Cluster Profiles (k=3, silhouette=0.366). Higher composite = better ESG performance.*

**Cluster 0 — Low-Risk Leaders (n=197):** Companies in this cluster have low overall risk (mean total = 15.83, "Low" band) and low environmental exposure in particular (3.53). They dominate the Leader classification. This cluster is disproportionately populated by Technology and Real Estate companies, where physical-world environmental impacts are limited. Mean composite score of 81.4 places these companies firmly in the top tier.

**Cluster 1 — Governance-Social Risk (n=107):** Moderate total risk (23.54, lower "Medium" band) with elevated Social (12.17) and Governance (9.34) scores relative to Cluster 0. Financial Services firms account for a significant share of this cluster, given their material exposure to regulatory compliance, executive remuneration, and data-privacy governance risks. Healthcare also contributes, given its social exposure to clinical ethics and pricing practices.

**Cluster 2 — Environmental Risk (n=126):** The highest-risk cluster (28.74, upper "Medium" band), characterised by substantially elevated Environmental scores (12.33). This cluster contains the majority of Energy, Basic Materials, Utilities, and Industrials companies. The defining characteristic is physical-world environmental footprint: emissions, resource extraction, waste, and water use. These companies carry the greatest ESG risk under any weighting scheme that includes environmental factors, and form the core of the Laggard classification.

The three archetypes are analytically useful because they suggest different intervention priorities. For Cluster 2 companies, reducing carbon and resource intensity is the primary lever. For Cluster 1 companies, governance reforms (board composition, executive pay alignment, data security) and social improvements (human capital management, supply-chain labour standards) are more relevant. For Cluster 0 companies, maintaining performance and improving disclosure quality is the main challenge.

---

## 5. India Spotlight: BRSR Core Framework

### 5.1 Regulatory Context

India's BRSR Core framework occupies a distinctive position in the global ESG regulatory landscape: unlike voluntary guidelines or broad disclosure mandates, BRSR Core requires third-party reasonable assurance for a specific set of nine KPIs, making it one of the most verifiable ESG frameworks in any emerging market (SEBI, 2023). The nine attributes are:

1. Greenhouse gas (GHG) emissions footprint
2. Water footprint
3. Energy footprint
4. Waste management
5. Description of key products with environmental or social concerns
6. Employee wellbeing (wages, safety)
7. Gender diversity and equal opportunity
8. Inclusive development
9. Openness of business (customer data, anti-competitive behaviour)

For the top 150 companies by market capitalisation — who have faced BRSR Core requirements since FY2023-24 — these nine KPIs carry assurance obligations, meaning that third-party auditors are required to review the underlying data, not just the disclosed numbers.

### 5.2 India Spotlight Sample

The India BRSR Spotlight collects FY2024-25 BRSR Core indicators from ten large-cap NIFTY companies across five sectors:

| Sector | Companies |
|--------|-----------|
| IT Services | Tata Consultancy Services (TCS), Infosys |
| Banking | HDFC Bank, ICICI Bank |
| FMCG | Hindustan Unilever, ITC Limited |
| Cement | UltraTech Cement, Ambuja Cement |
| Automobiles | Tata Motors, Maruti Suzuki India |

Data is manually extracted from each company's FY2024-25 Annual Report or standalone BRSR document, using the indicators prescribed under BRSR Core Attribute 1 (GHG intensity), Attribute 2 (water), Attribute 3 (energy), and Attribute 7 (gender diversity). The extraction template, formulas, and source links are available in the companion Excel workbook (Project3_India_BRSR_Spotlight.xlsx).

*Note: This spotl dataset is under active construction. All cells in the extraction template remain blank until verified figures are entered from company reports. No estimates or imputed values are used.*

### 5.3 Comparative Observations

While the India spotlight data is too small for statistical inference, several structural observations arise from the literature and regulatory context:

**Disclosure quality is highest in IT and FMCG.** Companies like TCS, Infosys, and HUL have published detailed, externally assured ESG reports for several years and are likely to have the most complete BRSR Core disclosures. Cement companies (UltraTech, Ambuja) face the highest environmental exposure — cement production is one of the most carbon-intensive manufacturing processes — and are therefore under the greatest pressure to report and reduce GHG intensity.

**The BRSR Core intensities are not directly comparable to Sustainalytics scores.** Sustainalytics' Environmental score reflects both exposure to material ESG issues and management quality, normalised against peers within the same sub-industry globally. BRSR Core data are absolute or intensity-based physical metrics (e.g., tCO2e per INR Crore of turnover), reported against a domestic regulatory baseline rather than a global peer benchmark. This makes systematic comparison challenging without a bridge methodology.

**India's ESG disclosure trajectory differs from the US trajectory.** The S&P 500 temporal analysis shows that Utilities, Materials, and Health Care improved most between 2021 and 2024 in the US context. India's BRSR Core, mandated only from FY2023-24, is at a much earlier stage in the disclosure lifecycle. The Drempetic et al. (2020) size-bias concern may be more acute in India, where the gap between large-cap disclosers and SMEs is substantially larger than within the S&P 500.

---

## 6. Discussion

### 6.1 Sector as the Primary ESG Risk Driver

The most consistent and robust finding in this analysis is that sector membership explains ESG risk to a far greater degree than any other variable examined. The ANOVA F-statistic of 27.978 is large by the standards of observational social science research, and the range from Energy (32.34) to Real Estate (13.09) spans more than 19 score points — nearly three full risk bands in the Sustainalytics classification system. This finding has immediate practical implications for ESG investing: comparing ESG scores across sectors without sector-relative normalisation will systematically disadvantage energy-intensive industries regardless of management quality. An Energy company scoring 28 (upper "Medium") may be a top performer within its sector; the same score for a Technology company would place it in the upper half of the High risk category.

This is one reason why Sustainalytics employs industry-relative scoring in its published risk ratings, and why MSCI uses a letter-grade system benchmarked against sector peers rather than against the universe. For retail investors and analysts using raw total scores for cross-sector comparisons, this structural confound is a material risk. The composite score constructed in this project applies Min-Max normalisation across the full sample rather than within sectors, which preserves the absolute differences; users who wish to perform sector-neutral comparisons should apply normalisation within sector groups.

### 6.2 The Null Size-Bias Finding

The absence of a statistically significant relationship between company size and ESG performance (r = 0.051, p = 0.291) within the S&P 500 is itself a valuable finding. It establishes that the size bias documented in the broader literature is primarily a phenomenon of cross-cap-tier comparison, not of large-cap variation. For practitioners working exclusively with large-cap equities — which describes the majority of institutional ESG mandates — this suggests that size-adjusting ESG scores is unnecessary when the investment universe is already constrained to the large-cap tier.

It also has methodological implications: adding employee count or market cap as a control variable in ESG-return regressions conducted within the S&P 500 is likely unnecessary and may introduce multicollinearity without removing confounding.

### 6.3 ESG Score Improvement: Real Progress or Methodology Artefact?

The finding that 66.7% of companies improved their Sustainalytics scores between 2021 and 2024 (mean Δ = −1.495, p < 0.001) is encouraging but requires careful interpretation. Several mechanisms could produce this pattern:

1. **Genuine sustainability improvements.** Companies have invested in renewable energy, supply-chain audits, board diversity, and other sustainability initiatives.
2. **Disclosure expansion.** As BRSR, SEC climate disclosure, and CSRD preparatory requirements have driven better data collection, companies have more accurately reported practices that were previously obscured.
3. **Sustainalytics methodology updates.** The provider has revised its methodology, particularly around sector-specific issue weights, which may have mechanically reduced scores for sectors like Utilities.

The Utilities sector's exceptional improvement (Δ = −5.36) is most plausibly explained by a combination of all three: substantial renewable investment (genuine), improved emissions reporting (disclosure), and likely adjustments to how Sustainalytics weights transition risk for utilities. The Energy sector's worsening (+1.10) despite the broad trend of improvement is consistent with increasing regulatory and litigation pressure on oil and gas, as well as Sustainalytics adjusting physical and transition risk weights upward for this sector.

### 6.4 Limitations

This study has several limitations that should be considered when interpreting the results:

1. **Single ESG provider.** All primary findings are specific to Sustainalytics methodology. Berg et al. (2022) show that pairwise inter-provider correlations can be as low as 0.38; different providers could produce substantially different rankings.

2. **Missing data.** Seventy-three companies (14.5%) lack ESG scores and are excluded. If missingness is correlated with ESG quality (e.g., if companies with the most controversial practices are less likely to be rated), the analytical sample may be biased toward better ESG performers.

3. **Financial data vintage.** The financial dataset is a 2019 vintage. No ESG-financial performance relationships are estimated, but the stale financial data precludes this analysis even if it were desired.

4. **Temporal analysis limitations.** The 2021-to-2024 temporal comparison uses the same Sustainalytics provider but cannot fully isolate genuine company-level improvement from methodology changes. The 216-company overlap is a convenience sample of companies present in both datasets, not a random sample of S&P 500 constituents.

5. **US large-cap scope.** All findings relate to US-listed, large-cap companies with extensive ESG disclosure programs. Results should not be generalised to small-cap, unlisted, or emerging-market firms without additional analysis.

6. **Composite weighting is a judgement call.** While the 40/30/30 weighting is motivated by SEBI's BRSR Core emphasis and sensitivity analysis confirms robustness, there is no universally correct weighting scheme. Different stakeholders (investors, regulators, communities) would reasonably emphasise different pillars.

---

## 7. Conclusion

This study benchmarks ESG performance across 430 S&P 500 companies using a transparent, reproducible methodology applied to publicly available Sustainalytics data. The core findings are:

1. **Sector drives ESG risk.** ANOVA (F = 27.978, p < 0.001) confirms highly significant sector-level differences, with Energy companies bearing nearly 2.5 times the ESG risk of Real Estate companies. Practitioners should always contextualise ESG scores within sector peer groups.

2. **Size bias is absent within large-cap.** Company size does not predict ESG performance within the S&P 500 (Pearson r = 0.051, p = 0.291). This null finding establishes a scope condition for the cross-market size-bias literature.

3. **Scores improved overall, with sector variation.** 66.7% of the 216-company overlapping sample improved their Sustainalytics scores between 2021 and 2024 (mean Δ = −1.495, p < 0.001). Utilities showed the largest gains; Energy worsened. Interpretation must account for possible methodology updates.

4. **Three ESG archetypes.** K-means clustering identifies Low-Risk Leaders (n=197), Governance-Social Risk firms (n=107), and Environmental Risk firms (n=126), each requiring distinct sustainability strategies.

5. **Composite classification is robust.** The weighted composite (E=40%, S=30%, G=30%) and the equal-weight composite are correlated at r = 0.988; only 8.1% of companies change classification under alternative weighting.

For India, the BRSR Core framework represents a significant step toward verified, standardised ESG disclosure among large-cap listed companies. The manual BRSR Core spotlight being compiled from FY2024-25 annual reports of ten NIFTY companies will provide complementary qualitative evidence. Extending the quantitative benchmarking methodology developed here to a sufficiently large set of BRSR-reporting Indian companies — as disclosure data accumulates over successive BRSR Core cycles — is a viable direction for future research.

---

## References

Atz, U., Van Holt, T., Liu, Z., & Bruno, C. (2023). Does sustainability generate better financial performance? Review, meta-analysis, and propositions. *Journal of Sustainable Finance & Investment, 13*(1), 802–825. https://doi.org/10.1080/20430795.2022.2106934

Berg, F., Koelbel, J. F., & Rigobon, R. (2022). Aggregate confusion: The divergence of ESG ratings. *Review of Finance, 26*(6), 1315–1344. https://doi.org/10.1093/rof/rfac033

Christensen, H. B., Hail, L., & Leuz, C. (2021). Mandatory CSR and sustainability reporting: Economic analysis and literature review. *Review of Accounting Studies, 26*(3), 1176–1248. https://doi.org/10.1007/s11142-021-09609-5

Drempetic, S., Klein, C., & Zwergel, B. (2020). The influence of firm size on the ESG score: Corporate sustainability ratings under review. *Journal of Business Ethics, 167*(2), 333–360. https://doi.org/10.1007/s10551-019-04164-1

Friede, G., Busch, T., & Bassen, A. (2015). ESG and financial performance: Aggregated evidence from more than 2000 empirical studies. *Journal of Sustainable Finance & Investment, 5*(4), 210–233. https://doi.org/10.1080/20430795.2015.1118917

Gibson Brandon, R., Krueger, P., & Schmidt, P. S. (2021). ESG rating disagreement and stock returns. *Financial Analysts Journal, 77*(4), 104–127. https://doi.org/10.1080/0015198X.2021.1963186

Global Sustainable Investment Alliance (GSIA). (2023). *Global sustainable investment review 2022.* GSIA. https://www.gsi-alliance.org/

Liang, H., & Renneboog, L. (2017). On the foundations of corporate social responsibility. *Journal of Finance, 72*(2), 853–910. https://doi.org/10.1111/jofi.12487

Ministry of Corporate Affairs (MCA), Government of India. (2019). *National guidelines on responsible business conduct (NGRBC).* MCA.

MSCI. (2024). *MSCI ESG ratings methodology.* MSCI Inc. https://www.msci.com/our-solutions/esg-investing/esg-ratings

OECD. (2008). *Handbook on constructing composite indicators: Methodology and user guide.* OECD Publishing. https://doi.org/10.1787/9789264043466-en

Pritish, A. (2024). *S&P 500 ESG risk ratings* [Dataset]. Kaggle. https://www.kaggle.com/datasets/pritish509/s-and-p-500-esg-risk-ratings

Securities and Exchange Board of India (SEBI). (2021). *Business responsibility and sustainability reporting by listed entities* (SEBI/LAD-NRO/GN/2021/22). SEBI. https://www.sebi.gov.in/

Securities and Exchange Board of India (SEBI). (2023). *BRSR Core — ESG disclosures for value chain* (SEBI/HO/CFD/CFD-SEC-2/P/CIR/2023/122). SEBI. https://www.sebi.gov.in/

Serafeim, G., & Yoon, A. (2022). Stock price reactions to ESG news: The role of ESG ratings and disagreement. *Review of Accounting Studies, 28*(3), 1500–1530. https://doi.org/10.1007/s11142-022-09675-3

S&P Global. (2024). *S&P Global ESG scores methodology.* S&P Global. https://www.spglobal.com/esg/scores/

Sburstein. (2021). *S&P 500 ESG and stock data* [Dataset]. GitHub. https://github.com/sburstein/ESG-Stock-Data

Sustainalytics. (2023). *ESG risk ratings: Methodology abstract.* Morningstar Sustainalytics. https://www.sustainalytics.com/esg-research/resource/corporate-esg-research/esg-risk-ratings

Zinovadr. (n.d.). *S&P 500 companies with financial information* [Dataset]. Kaggle. https://www.kaggle.com/datasets/zinovadr/sp-500-companies-with-financial-information

---

*All analyses were conducted in Python 3.12. Code, data, and workbook are available at the project GitHub repository. This report was written by the author; AI tools were used for data processing and drafting support and are not listed as co-authors.*
