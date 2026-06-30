# Sector as the Dominant Driver of ESG Risk: Evidence Against Size Bias Within the Large-Cap Universe

**Rura**  
School of Management and Labour Studies, Tata Institute of Social Sciences (TISS), Mumbai, India  
Email: [author email]

---

## Highlights

- Sector membership explains **40.0%** of ESG risk score variance within the S&P 500 (η² = 0.400, ω² = 0.376) — a large effect by any behavioural or social science benchmark.
- The ESG size bias documented across the full market-cap distribution **does not persist within the large-cap universe**: β(ln employees) = 0.132, p = 0.566, incremental R² < 0.001, even after sector fixed effects.
- 27 of 55 sector pairs are significantly different under Dunn's post-hoc test (Bonferroni-corrected), with Energy and Real Estate at opposite extremes (means: 32.34 vs. 13.09).
- ESG scores improved significantly between 2021 and 2024 (mean Δ = −1.495, t = −5.826, p < 0.001); after controlling for regression to mean, **sector effects on improvement rate remain jointly significant** (F = 5.872, p < 0.001).
- K-means clustering (k = 3, confirmed by both silhouette and gap statistic) identifies three interpretable ESG archetypes with distinct strategic implications.

---

## Abstract

Sustainalytics ESG Risk Ratings for 430 S&P 500 companies are used to address three contested questions in the ESG measurement literature: whether sector membership explains ESG risk scores in the large-cap universe; whether the size bias documented in prior research persists within this universe; and how scores have evolved between 2021 and 2024. One-way ANOVA and Kruskal-Wallis tests confirm highly significant sector differences (F = 27.978, p < 0.001; H = 170.288, p < 0.001), with sector explaining 40.0% of total variance (η² = 0.400) — a large effect rarely reported in the ESG literature. In contrast, company size (ln of full-time employees) has no statistically significant relationship with ESG risk scores in a bivariate model (r = 0.051, p = 0.291) or after sector fixed effects (β = 0.132, p = 0.566), with an incremental R² of less than 0.001. A temporal analysis of 216 overlapping companies reveals a statistically significant mean improvement between 2021 and 2024 (Δ = −1.495, p < 0.001); after controlling for regression to mean, sector effects on improvement rates remain jointly significant (F = 5.872, p < 0.001). Gap statistic analysis and silhouette scoring consistently identify three ESG performance archetypes. These findings establish a scope condition for the cross-market ESG size bias and demonstrate that sector-relative normalisation is essential for any valid cross-sector ESG comparison.

**Keywords:** ESG ratings; Sustainalytics; sector heterogeneity; size bias; large-cap; temporal dynamics; K-means clustering  
**JEL Codes:** G11, G14, M14, Q56

---

## 1. Introduction

Environmental, social, and governance (ESG) ratings have become central inputs to investment decisions, with global ESG-integrated assets exceeding USD 30 trillion by 2023 (GSIA, 2023). Yet three empirical questions central to the practical use of ESG scores remain incompletely answered. First, how much of the variation in ESG risk scores is explained by sector membership versus firm-level management choices? If sector drives most of the variation, cross-sector comparisons using raw scores are largely measuring industry exposure, not firm quality. Second, does the well-documented size bias in ESG ratings — whereby larger firms receive better ratings regardless of genuine sustainability performance (Drempetic, Klein, and Zwergel, 2020) — persist within the large-cap investment universe where most ESG capital is deployed? Third, given that ESG disclosures and regulations have intensified in recent years, how have scores evolved between 2021 and 2024, and does this evolution reflect genuine improvement or simply regression to mean?

This paper addresses all three questions using a single, consistent dataset: Sustainalytics ESG Risk Ratings for 430 S&P 500 companies (~2024), supplemented with the same provider's 2021 ratings for 216 overlapping firms. Using a single provider eliminates inter-rater disagreement as a confound (Berg, Koelbel, and Rigobon, 2022), allowing clean within-provider analysis of sector effects, size effects, and temporal dynamics.

Our central finding on the size bias has immediate practical implications. Drempetic et al. (2020) establish the cross-market size bias using a sample spanning the full market-cap distribution. We show that this bias is essentially absent within the S&P 500: after sector fixed effects, β(ln employees) = 0.132 (p = 0.566), with ln(employees) adding less than 0.1 percentage points to the R² already explained by sector membership. This establishes a scope condition for one of the most widely cited findings in the ESG literature and implies that ESG investors working exclusively within large-cap mandates do not need to adjust ESG scores for company size.

The sector dominance finding is equally striking: η² = 0.400 means sector membership alone explains 40% of total ESG risk score variance. By Cohen's (1988) benchmarks, this is a large effect; it exceeds the sector-level effects reported in most prior ESG studies. Twenty-seven of 55 possible sector pairs are significantly different after Bonferroni-corrected Dunn's post-hoc testing. Any analytical framework that compares ESG scores across sectors without sector-relative normalisation is, by implication, primarily sorting companies by industry rather than by sustainability management quality.

The remainder of this paper is structured as follows. Section 2 reviews the relevant literature and develops three testable hypotheses. Section 3 describes the data and methodology, including the composite scoring framework and statistical tests. Section 4 presents the results. Section 5 discusses the findings and their implications. Section 6 concludes.

---

## 2. Literature Review and Hypotheses

### 2.1 ESG Rating Methodologies and the Provider Divergence Problem

ESG ratings are not a commodity; they are heterogeneous assessments whose output depends critically on the provider's choices of scope, indicators, and aggregation weights (Berg, Koelbel, and Rigobon, 2022). Sustainalytics measures ESG risk as a function of exposure and management: a company's total risk score reflects how much of its material ESG exposure remains unmanaged, on a continuous 0-to-100+ scale where lower scores are better. MSCI assigns letter grades relative to industry peers. S&P Global ESG Scores aggregate against an internal benchmark. These methodological differences generate substantial inter-provider disagreement; Berg et al. (2022) find pairwise correlations as low as 0.38, and Gibson Brandon, Krueger, and Schmidt (2021) show that this disagreement generates systematic noise in ESG-return studies.

To avoid inter-provider disagreement as a confound, this paper uses Sustainalytics exclusively — consistent with prior studies using the same provider (Liang and Renneboog, 2017; Drempetic et al., 2020) and with the temporal comparison requiring a fixed methodology over time.

### 2.2 Sector Heterogeneity in ESG Risk

Sustainalytics' methodology assigns different issue weights by industry, reflecting the principle that different sectors face materially different ESG exposures. Carbon-intensive industries (Energy, Basic Materials, Utilities) face substantial environmental and transition risks; Financial Services faces governance and systemic risks; Healthcare faces social risks around pricing, access, and clinical ethics. This industry-relative structure implies that sector membership should be a primary driver of raw ESG risk scores (Liang and Renneboog, 2017; MSCI, 2024).

Prior studies confirm sector variation but rarely report effect sizes (Friede, Busch, and Bassen, 2015; Drempetic et al., 2020). We compute both eta-squared and omega-squared to provide standardised effect size estimates, enabling direct comparison with other literatures in finance and management.

**H1:** Sustainalytics ESG risk scores differ significantly across GICS sectors, and sector membership is a large-effect driver of score variation.

### 2.3 The Size Bias in ESG Ratings

Drempetic, Klein, and Zwergel (2020) demonstrate that larger firms receive systematically better ESG ratings after controlling for actual sustainability performance. The mechanism is primarily attributional: larger firms have dedicated sustainability teams, relationships with data vendors, and established reporting frameworks that enable complete and well-evidenced disclosures. Rating agencies reward disclosure quality in part because they cannot verify the underlying reality from incomplete filings alone (Christensen, Hail, and Leuz, 2021).

Liang and Renneboog (2017) show that the effect is robust across countries and partially driven by institutional factors, including analyst coverage and institutional investor attention — both of which are correlated with firm size. However, neither study explicitly tests whether the effect persists within a sample already constrained to large-cap firms. The S&P 500 is a size-truncated sample: even the smallest S&P 500 company has a market cap well above the small-cap threshold and sufficient analyst coverage to sustain ESG disclosure. The reporting-capacity mechanism that drives the cross-market size bias should therefore be attenuated or absent.

**H2:** The ESG size bias observed across the full market-cap distribution does not persist within the S&P 500 large-cap universe.

### 2.4 Temporal Dynamics of ESG Scores

ESG disclosure has intensified since 2021 across multiple regulatory dimensions: the SEC's proposed climate disclosure rule, the EU Corporate Sustainability Reporting Directive, and in India, SEBI's BRSR Core mandate for the top 150 listed companies from FY2023-24 (SEBI, 2023). Serafeim and Yoon (2022) show that changes in ESG scores — rather than levels — predict future abnormal stock returns, suggesting that temporal dynamics carry information beyond cross-sectional levels. Christensen et al. (2021) argue that mandatory disclosure regimes reduce measurement error and improve score reliability over time.

A competing explanation for observed score improvements is regression to mean: firms starting with high risk scores have more room to improve (or less room to worsen), producing a mechanical negative correlation between initial score and subsequent change. Any temporal analysis must control for this effect to isolate genuine improvement from statistical artefact.

**H3:** ESG scores improved significantly between 2021 and 2024, with significant sector heterogeneity in improvement rates, after controlling for regression to mean.

---

## 3. Data and Methodology

### 3.1 Data Sources

**Primary dataset.** The S&P 500 ESG Risk Ratings dataset (Pritish, 2024; Kaggle identifier: pritish509/s-and-p-500-esg-risk-ratings; GitHub mirror: ggogitidze/SP-500-ESG) contains Sustainalytics-based ESG Risk Scores for S&P 500 constituent companies as of approximately late 2023 to early 2024. Variables include: total ESG risk score; pillar-level scores for Environment, Social, and Governance; ESG risk level classification (Negligible/Low/Medium/High/Severe); controversy level and score; ESG risk percentile; sector (GICS Level 1); industry; and full-time employee count. The raw dataset contains 503 companies. After removing 73 companies (14.5%) with missing ESG pillar scores and 1 company with a missing sector label, the analytical sample is **N = 430 companies** across **11 GICS sectors**.

The missing 14.5% may not be missing at random — companies with lower analyst coverage may have missing scores, and these may differ in ESG quality. This potential bias is treated as a limitation and does not affect the directional conclusions (which would, if anything, be conservative with respect to sector variation, since omitted firms are likely concentrated in sectors with poorer disclosure).

**Temporal dataset.** The sburstein/ESG-Stock-Data repository (GitHub, 2021) contains Sustainalytics ESG scores for 245 S&P 500 companies as scraped from Yahoo Finance on 1 March 2021. Both datasets use Sustainalytics' methodology; this analysis therefore compares same-provider scores at two points in time, not cross-provider ratings. The overlap between the primary dataset and the temporal dataset is **N = 216 companies**. Score changes (Δ = score₂₀₂₄ − score₂₀₂₁) are computed for all 216 companies.

**Financial data.** A supplementary financial dataset (Zinovadr, Kaggle; ~2019 vintage) provides market capitalisation, P/E, price-to-book, and EPS. This is used for descriptive context only; no ESG-financial performance regressions are estimated given the data vintage.

### 3.2 Composite ESG Performance Score

Sustainalytics' raw scores represent ESG risk: higher scores indicate more risk (worse ESG performance). To construct a composite performance score where higher indicates better performance — consistent with analytical convention in multi-criteria decision-making — we apply the OECD (2008) composite indicator procedure:

1. **Min-Max normalisation** of each pillar to [0, 100]: norm_i = (x_i − x_min)/(x_max − x_min) × 100
2. **Inversion**: inv_i = 100 − norm_i
3. **Weighted aggregation**: Composite = 0.40·E_inv + 0.30·S_inv + 0.30·G_inv

The 40/30/30 weighting reflects the relative emphasis on environmental indicators in regulatory frameworks such as SEBI's BRSR Core (SEBI, 2023) and the Paris Agreement-aligned investment mandates. A sensitivity check using equal weights (33.3% each) shows a Pearson correlation of r = 0.988 between the two composite variants, with only 35 of 430 companies (8.1%) changing classification tier. Results are therefore robust to the weighting choice.

Companies are classified as **Leaders** (composite ≥ 75th percentile: ≥ 74.7), **Average** (25th–75th percentile: 60.9–74.7), or **Laggards** (composite ≤ 25th percentile: ≤ 60.9).

### 3.3 Statistical Methods

**Sector differences (H1).** We apply a one-way ANOVA (F-test) with sector as the independent variable and total ESG risk score as the outcome. The Levene test confirms that group variances are unequal across sectors (W = 4.155, p < 0.001), so the Kruskal-Wallis H-test is designated the primary test and ANOVA is reported as a robustness check. Effect size is quantified using eta-squared (η² = SS_between/SS_total) and bias-corrected omega-squared (ω²). Pairwise sector differences are identified using Dunn's post-hoc test with Bonferroni correction.

**Size bias (H2).** Two models are estimated. Model 1 is a bivariate Pearson (and Spearman) correlation of ln(full-time employees) with total ESG risk score. Model 2 adds sector fixed effects in an OLS regression: ESG_risk = α + β·ln(employees) + Σγ_k·Sector_k + ε. The incremental R² — the increase from the sector-only model to the sector-plus-size model — measures the marginal contribution of company size beyond sector membership. The Breusch-Pagan test for heteroscedasticity yields p = 0.166, indicating homoscedastic residuals; results are also reported with HC3 robust standard errors as a precaution.

**Temporal drift (H3).** Let Δ_i = score_i,2024 − score_i,2021 for the 216 overlapping companies. A one-sample t-test assesses whether the mean Δ differs significantly from zero. To control for regression to mean, we estimate: Δ_i = α + β₁·score_i,2021 + Σγ_k·Sector_k + ε_i. The coefficient β₁ on the initial (2021) score captures regression to mean; sector coefficients capture genuine sector-level differences in improvement rates. An F-test assesses whether sector effects are jointly significant after controlling for β₁.

**Clustering.** K-means clustering is applied to the three normalised and inverted pillar scores. The optimal k is selected by maximising the average silhouette score over k ∈ {2, 3, 4, 5, 6} and confirmed by the gap statistic (Tibshirani, Walther, and Hastie, 2001). PCA is used for 2D visualisation. All analyses are conducted in Python 3.12 with fixed random seeds (random_state = 42) for reproducibility.

---

## 4. Results

### 4.1 Descriptive Statistics

Table 1 presents descriptive statistics for the 430-company sample. The mean Sustainalytics total ESG risk score is 21.53 (SD = 6.89), placing the average S&P 500 company in the "Medium" risk band (20–30). The distribution is approximately unimodal and slightly right-skewed (D'Agostino statistic = 14.773, p = 0.001), with a median of 21.05. The majority of companies fall in the Low (43.5%) or Medium (42.8%) risk bands; only 50 companies (11.6%) are classified as High risk, and 3 (0.7%) as Severe.

**Table 1. Descriptive Statistics — Total ESG Risk Score and Pillar Scores (N = 430)**

| Statistic | Total ESG Risk | Environment | Social | Governance |
|-----------|----------------|-------------|--------|------------|
| Mean | 21.53 | 6.49 | 8.68 | 6.73 |
| Median | 21.05 | 4.24 | 8.50 | 6.52 |
| SD | 6.89 | 5.45 | 2.81 | 2.21 |
| Min | 6.80 | 0.00 | 1.20 | 1.60 |
| Max | 47.00 | 28.90 | 18.10 | 15.50 |
| Skewness | 0.52 | 1.82 | 0.49 | 0.28 |

*Notes: All variables from Sustainalytics ESG Risk Ratings, ~2024. Lower scores indicate lower ESG risk (better performance). Sustainalytics risk bands: Negligible < 10, Low 10–20, Medium 20–30, High 30–40, Severe ≥ 40.*

The Environment pillar shows the greatest dispersion (SD = 5.45, skewness = 1.82), reflecting the concentration of high environmental risk in a small number of sectors. The Governance pillar is the most consistent across firms (SD = 2.21), consistent with the finding that governance structures among large-cap companies have converged substantially under regulatory pressure.

### 4.2 Sector Differences (H1)

Table 2 presents sector-level mean total ESG risk scores sorted from highest to lowest risk. The range spans 19.25 points — from Energy (32.34) to Real Estate (13.09) — corresponding to the difference between the High and Low risk bands.

**Table 2. ESG Risk Scores by GICS Sector (N = 430)**

| Sector | N | Mean Total | SD | Mean Env | Mean Soc | Mean Gov |
|--------|---|-----------|-----|---------|---------|---------|
| Energy | 20 | 32.34 | 4.21 | 16.92 | 8.93 | 6.50 |
| Basic Materials | 19 | 26.72 | 4.88 | 12.62 | 7.54 | 6.57 |
| Utilities | 28 | 26.71 | 5.12 | 11.81 | 9.44 | 5.47 |
| Consumer Defensive | 33 | 25.45 | 5.33 | 8.73 | 10.84 | 5.87 |
| Industrials | 60 | 24.01 | 6.11 | 7.10 | 10.84 | 6.08 |
| Financial Services | 63 | 21.19 | 5.92 | 1.41 | 9.63 | 10.14 |
| Healthcare | 53 | 20.58 | 5.74 | 1.79 | 11.48 | 7.31 |
| Comm. Services | 14 | 19.41 | 5.18 | 1.86 | 10.14 | 7.41 |
| Consumer Cyclical | 51 | 19.23 | 5.82 | 5.30 | 8.39 | 5.55 |
| Technology | 61 | 16.92 | 4.88 | 4.29 | 6.88 | 5.76 |
| Real Estate | 28 | 13.09 | 3.31 | 3.69 | 3.64 | 5.75 |

*Notes: SD = standard deviation. Sectors sorted by mean total risk (descending). Source: Sustainalytics ESG Risk Ratings (~2024).*

The Levene test for homogeneity of variances rejects the null of equal group variances (W = 4.155, p < 0.001), motivating the Kruskal-Wallis H-test as the primary inferential test. The Kruskal-Wallis result is highly significant: **H(10) = 170.288, p < 0.001**. The one-way ANOVA corroborates this: F(10, 419) = 27.978, p < 0.001. Effect size is large by any standard: **η² = 0.400, ω² = 0.376** (Cohen, 1988: large ≥ 0.14). Sector membership alone explains approximately 40% of total ESG risk score variance in the S&P 500 — approximately 27 times the benchmark for a large effect.

Dunn's post-hoc test with Bonferroni correction identifies **27 of 55 possible sector pairs** (49.1%) as significantly different (p < 0.05 Bonferroni-adjusted). Energy differs significantly from all other sectors (10/10 pairs). Real Estate differs significantly from 8 of 10 sectors. Technology and Consumer Cyclical are not significantly different from each other — a reasonable result given their similar pillar profiles. Financial Services and Healthcare are also not significantly different, despite very different pillar compositions (Financial Services: high governance; Healthcare: high social), because their total score means happen to be close (21.19 vs. 20.58).

**H1 is supported.** Sector membership is a statistically significant and practically large driver of ESG risk scores, explaining 40.0% of total variance.

### 4.3 Size Bias Test (H2)

**Model 1 — bivariate.** Among the 425 companies with non-missing employee counts, the Pearson correlation between ln(employees) and total ESG risk score is r = 0.051 (p = 0.291). The Spearman rank correlation is ρ = 0.031 (p = 0.520). Neither reaches statistical significance at conventional thresholds.

**Model 2 — sector fixed effects.** An OLS regression of ESG risk on ln(employees) with sector fixed effects yields β(ln employees) = 0.132 (p = 0.566; 95% CI: [−0.320, 0.585]). The Breusch-Pagan test does not detect heteroscedasticity (p = 0.166); HC3 robust standard errors produce an almost identical p-value (p = 0.596). The sector-only model explains R² = 0.400; adding ln(employees) increases R² by **0.000479** — essentially zero. Table 3 summarises the size-bias results.

**Table 3. Size Bias Tests: ln(Employees) vs. ESG Risk Score (N = 425)**

| Model | β(ln emp) | SE | p-value | 95% CI | R² | Adj-R² |
|-------|-----------|----|---------|---------|-----|--------|
| Bivariate OLS | 0.253 | 0.245 | 0.303 | [−0.229, 0.736] | 0.003 | 0.000 |
| Sector FE OLS | 0.132 | 0.230 | 0.566 | [−0.320, 0.585] | 0.401 | 0.385 |
| Sector FE OLS (HC3) | 0.132 | 0.248 | 0.596 | — | 0.401 | — |
| Sector-only OLS | — | — | — | — | 0.400 | 0.386 |

*Notes: Dependent variable = Total ESG Risk Score. HC3 = heteroscedasticity-consistent standard errors. Sector FE includes dummies for all 11 GICS sectors.*

The incremental R² from adding ln(employees) to the sector model is 0.0005 — equivalent to company size explaining less than one additional decimal place of ESG score variance, after sector is controlled. VIF for ln(employees) in the bivariate model is 1.000 (no collinearity concern).

**H2 is supported.** The size bias does not persist within the S&P 500. After sector fixed effects, company size explains essentially zero marginal variance in ESG risk scores.

### 4.4 Temporal Dynamics (H3)

For 216 companies with data in both 2021 and 2024, the mean change in total ESG risk score is **Δ = −1.495** (SD = 3.77; negative Δ = improved). A one-sample t-test rejects the null of zero mean change: **t(215) = −5.826, p < 0.001**. Of 216 companies, 66.7% improved (lower risk), 32.4% worsened, and 0.9% showed no change.

However, the Pearson correlation between initial 2021 score and subsequent score change is **r = −0.446 (p < 0.001)**, indicating a substantial regression-to-mean effect: companies starting with higher ESG risk in 2021 improved more. Interpreting the raw mean improvement as evidence of genuine progress therefore requires controlling for this mechanical effect.

The regression model Δ_i = α + β₁·score_i,2021 + Σγ_k·Sector_k + ε_i yields:
- β₁(initial score) = **−0.270 (p < 0.001)**: firms improve by 0.27 points for each additional point of initial ESG risk (regression to mean).
- R² of this model = 0.378.
- An F-test of the joint significance of sector coefficients after controlling for β₁: **F = 5.872, p < 0.001**.

Sector effects on temporal improvement rates therefore survive regression-to-mean correction. Table 4 reports sector-level mean score changes.

**Table 4. Temporal ESG Score Changes by Sector (2021 → 2024, N = 216)**

| Sector | N | Mean Δ Total | Mean Δ Env | Mean Δ Soc | Mean Δ Gov |
|--------|---|-------------|----------|----------|----------|
| Utilities | 15 | **−5.360** | −3.407 | −1.487 | −0.613 |
| Materials | 10 | −3.740 | −2.020 | −1.580 | −0.210 |
| Health Care | 24 | −3.175 | −0.446 | −1.704 | −1.071 |
| Real Estate | 23 | −1.874 | −0.770 | −1.326 | +0.391 |
| Information Technology | 42 | −1.255 | +0.543 | −1.267 | −0.400 |
| Industrials | 32 | −0.903 | +0.028 | −0.531 | −0.556 |
| Financials | 19 | −0.437 | −0.237 | −0.316 | +0.121 |
| Consumer Discretionary | 25 | −0.376 | −0.192 | +0.264 | −0.456 |
| Comm. Services | 10 | −0.060 | +0.740 | +0.040 | −0.840 |
| Consumer Staples | 9 | +0.700 | +0.744 | +0.178 | −0.133 |
| **Energy** | 7 | **+1.100** | +1.100 | −0.529 | +0.129 |

*Notes: Negative Δ = score decreased = ESG risk improved. Positive Δ = risk worsened. Sector names use Sustainalytics/GICS equivalents for 2021 dataset.*

Utilities showed by far the largest improvement (Δ = −5.36), concentrated in the Environmental pillar (−3.41). This is consistent with substantial renewable energy investment by US utilities between 2021 and 2024, though Sustainalytics methodology changes for this sector during the period may contribute to this pattern. Energy is the only sector to worsen on average (Δ = +1.10), driven entirely by increasing Environmental risk (+1.10) — consistent with growing regulatory and litigation pressure on fossil-fuel companies in this period.

**H3 is supported with qualification.** ESG scores improved significantly on average (p < 0.001), but a substantial proportion of this improvement reflects regression to mean. After controlling for regression to mean, sector effects on improvement rates are statistically significant (F = 5.872, p < 0.001), indicating genuine sector-level heterogeneity in progress rates.

### 4.5 ESG Performance Archetypes

K-means clustering on the three normalised and inverted pillar scores identifies three clusters as optimal. Both the silhouette score (maximum at k = 3: 0.366) and the gap statistic (Tibshirani method; optimal k = 3) agree, providing dual validation. PCA produces a two-component solution explaining 86.1% of variance (PC1: 48.8%, PC2: 37.3%).

**Table 5. K-Means Cluster Profiles (k = 3, Silhouette = 0.366)**

| Cluster | N | Archetype Label | Mean Total ESG | Mean Env | Mean Soc | Mean Gov | Mean Composite |
|---------|---|----------------|---------------|---------|---------|---------|----------------|
| 0 | 197 | Low-Risk Leaders | 15.83 | 3.53 | 6.61 | 5.69 | 81.4 |
| 1 | 107 | Governance-Social Risk | 23.54 | 2.04 | 12.17 | 9.34 | 69.4 |
| 2 | 126 | Environmental Risk | 28.74 | 12.33 | 10.29 | 6.12 | 61.4 |

*Notes: Clustering on normalised/inverted E, S, G pillar scores. Higher composite = better performance. Mean composite computed on 0–100 scale.*

**Cluster 0 — Low-Risk Leaders (n = 197):** Low overall ESG risk (total = 15.83, "Low" band), with uniformly low pillar scores. Disproportionately populated by Technology, Real Estate, and Consumer Cyclical companies. High composite score (81.4) reflects consistently strong ESG risk management across all pillars.

**Cluster 1 — Governance-Social Risk (n = 107):** Moderate overall risk (23.54), driven by elevated Social (12.17) and Governance (9.34) scores. Financial Services firms account for a substantial portion of this cluster, given material exposure to regulatory compliance, data-security governance, and systemic risk considerations. The relatively low Environmental score (2.04) reflects the limited physical-world environmental footprint of financial intermediaries.

**Cluster 2 — Environmental Risk (n = 126):** Highest overall risk (28.74), almost entirely driven by elevated Environmental scores (12.33 — nearly six times Cluster 1). This cluster concentrates Energy, Basic Materials, Utilities, and Industrials firms whose operations involve significant resource extraction, combustion, or chemical processing. These firms have the most to gain from environmental transition strategies.

The three archetypes are not reducible to simple sector classifications: Cluster 1 and Cluster 2 both contain Industrials firms, but with distinct pillar profiles. The clustering therefore provides information beyond a simple sector-level cut.

---

## 5. Discussion

### 5.1 Sector Dominance as a Structural Constraint

The finding that sector membership explains 40.0% of ESG risk score variance (η² = 0.400) is the study's most practically consequential result. It implies that when an analyst observes that Company A has a higher Sustainalytics score than Company B, the most likely explanation — prior to any firm-level analysis — is that A and B operate in different sectors, not that A's management team has made different sustainability decisions. This is a structural constraint on the informativeness of raw ESG scores as signals of firm-level sustainability quality.

The practical implication is straightforward: for cross-sector ESG comparisons to be meaningful, sector-relative normalisation is not optional — it is methodologically necessary. This is consistent with the sector-relative design of MSCI's letter ratings and with the "industry-adjusted" score variants offered by several data providers. Our results quantify, for the first time with full effect-size reporting in this literature, the magnitude of the adjustment required.

### 5.2 Scope Condition for the Size Bias

Our finding that the size bias does not persist within the S&P 500 complements rather than contradicts Drempetic et al. (2020). The mechanism Drempetic et al. identify — reporting capacity differences between small, mid, and large-cap firms — is essentially saturated within the S&P 500: every S&P 500 company, by construction, has sufficient analyst coverage, institutional investor scrutiny, and organisational scale to maintain ESG reporting infrastructure. The reporting-advantage that large-cap firms hold over small-cap firms is thus absent as a between-firm variation driver within this sample.

This scope condition has a direct practical implication: ESG investors with mandates limited to the large-cap universe — which describes the majority of ESG-integrated institutional portfolios — can treat company size as an irrelevant control variable in ESG analysis. Size-adjusting ESG scores is an unnecessary correction when all firms are in the large-cap tier, and may introduce spurious variation. This does not generalise to mixed-cap or full-market ESG analysis, where the size effect documented by Drempetic et al. should still be expected.

### 5.3 Interpreting Temporal Improvement

The regression-to-mean finding (r = −0.446, β = −0.270, p < 0.001) is an important methodological caution for temporal ESG analyses. Studies that report "X% of companies improved their ESG scores" without controlling for initial score levels are conflating genuine improvement with the mechanical tendency for high-initial-risk companies to revert toward the sample mean. Our results show that even after this correction, sector effects on improvement rates remain jointly significant (F = 5.872, p < 0.001), implying genuine sector-level heterogeneity in progress.

The Utilities sector's exceptional improvement (Δ = −5.36) warrants particular caution. While consistent with documented renewable energy investment trends, Sustainalytics' methodology updates between 2021 and 2024 — which we cannot fully isolate — may have mechanically reduced Utilities scores by adjusting how transition-risk management is credited. Energy's worsening (Δ = +1.10) despite this broader trend is a potentially genuine signal of increasing regulatory and litigation exposure, as fossil-fuel companies faced growing legal liability related to climate disclosures during this period.

### 5.4 Implications for India's BRSR Framework

India's BRSR Core mandate (SEBI, 2023) — requiring third-party reasonable assurance for nine specific ESG KPIs from the top 150 listed companies — reflects the same underlying principle revealed by our temporal analysis: mandatory, standardised disclosure is a necessary condition for meaningful inter-firm ESG comparison. Our finding that sector explains 40% of variance in the Sustainalytics universe implies that India's regulatory framework should account for sector-level differences in reporting standards and exposure levels. Energy-adjacent sectors (Oil and Gas, Cement, Power) should be benchmarked within sector, not against the full NIFTY universe.

The size-bias null finding has a potentially different implication in India: the S&P 500 is already constrained to large-cap firms. SEBI's top-150 cutoff imposes a similar constraint, but the size distribution of Indian listed companies outside the top 150 is far more dispersed than within the S&P 500. The Drempetic et al. size-bias is therefore likely to manifest more strongly in India's broader disclosure ecosystem, even if it is attenuated within the top-150 sub-universe.

---

## 6. Conclusion

This study uses Sustainalytics ESG Risk Ratings for 430 S&P 500 companies to test three contested empirical claims in the ESG literature. We find: (i) sector membership explains 40.0% of total ESG risk score variance (η² = 0.400) — a large effect that fundamentally constrains the informativeness of raw cross-sector ESG comparisons; (ii) the ESG size bias documented across the full market-cap distribution is absent within the S&P 500, with company size adding essentially zero marginal variance (incremental R² = 0.0005) after sector fixed effects; and (iii) ESG scores improved significantly between 2021 and 2024 (Δ = −1.495, p < 0.001), with sector effects on improvement rates remaining jointly significant (F = 5.872, p < 0.001) after controlling for regression to mean. K-means clustering, validated by both silhouette score and gap statistic, identifies three ESG performance archetypes — Low-Risk Leaders, Governance-Social Risk firms, and Environmental Risk firms — each with distinct strategic priority implications.

The most actionable implications are: practitioners should normalise ESG scores within sector before making cross-sector comparisons; ESG investors with large-cap-constrained mandates do not need to size-adjust ESG scores; and temporal improvement analyses should routinely control for regression to mean to avoid overstating genuine progress.

**Limitations.** This study uses a single ESG provider (Sustainalytics), limiting claims about ESG performance more broadly. The temporal analysis cannot fully isolate genuine company-level improvement from methodology changes made by Sustainalytics between 2021 and 2024. The 14.5% of companies with missing ESG scores may not be missing at random. Financial data is too dated for ESG-return analysis.

**Future research.** Extending this analysis to include MSCI and S&P Global ESG Scores for the same companies — when sufficiently large open datasets become available — would allow the sector-dominance and size-bias findings to be tested across providers, addressing the single-provider limitation. Replicating the temporal analysis with a fully documented methodology-change log from Sustainalytics would sharpen the causal interpretation of score trends. For India specifically, the accumulation of BRSR Core data across successive annual report cycles from FY2023-24 onward creates a natural laboratory for testing whether the size-bias and sector-dominance patterns documented here for the US large-cap universe generalise to India's top-150 listed companies.

---

## References

Berg, F., Koelbel, J. F., & Rigobon, R. (2022). Aggregate confusion: The divergence of ESG ratings. *Review of Finance, 26*(6), 1315–1344. https://doi.org/10.1093/rof/rfac033

Breusch, T. S., & Pagan, A. R. (1979). A simple test for heteroscedasticity and random coefficient variation. *Econometrica, 47*(5), 1287–1294. https://doi.org/10.2307/1911963

Christensen, H. B., Hail, L., & Leuz, C. (2021). Mandatory CSR and sustainability reporting: Economic analysis and literature review. *Review of Accounting Studies, 26*(3), 1176–1248. https://doi.org/10.1007/s11142-021-09609-5

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Drempetic, S., Klein, C., & Zwergel, B. (2020). The influence of firm size on the ESG score: Corporate sustainability ratings under review. *Journal of Business Ethics, 167*(2), 333–360. https://doi.org/10.1007/s10551-019-04164-1

Dunn, O. J. (1964). Multiple comparisons using rank sums. *Technometrics, 6*(3), 241–252. https://doi.org/10.2307/1266041

Friede, G., Busch, T., & Bassen, A. (2015). ESG and financial performance: Aggregated evidence from more than 2000 empirical studies. *Journal of Sustainable Finance & Investment, 5*(4), 210–233. https://doi.org/10.1080/20430795.2015.1118917

Gibson Brandon, R., Krueger, P., & Schmidt, P. S. (2021). ESG rating disagreement and stock returns. *Financial Analysts Journal, 77*(4), 104–127. https://doi.org/10.1080/0015198X.2021.1963186

Global Sustainable Investment Alliance (GSIA). (2023). *Global sustainable investment review 2022.* GSIA. https://www.gsi-alliance.org/

Kruskal, W. H., & Wallis, W. A. (1952). Use of ranks in one-criterion variance analysis. *Journal of the American Statistical Association, 47*(260), 583–621. https://doi.org/10.2307/2280779

Levene, H. (1960). Robust tests for equality of variances. In I. Olkin (Ed.), *Contributions to probability and statistics* (pp. 278–292). Stanford University Press.

Liang, H., & Renneboog, L. (2017). On the foundations of corporate social responsibility. *Journal of Finance, 72*(2), 853–910. https://doi.org/10.1111/jofi.12487

MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, 1*, 281–297.

MSCI. (2024). *MSCI ESG ratings methodology.* MSCI Inc. https://www.msci.com/our-solutions/esg-investing/esg-ratings

OECD. (2008). *Handbook on constructing composite indicators: Methodology and user guide.* OECD Publishing. https://doi.org/10.1787/9789264043466-en

Pearson, K. (1895). Notes on regression and inheritance in the case of two parents. *Proceedings of the Royal Society of London, 58*, 240–242.

Pritish, A. (2024). *S&P 500 ESG risk ratings* [Dataset]. Kaggle. https://www.kaggle.com/datasets/pritish509/s-and-p-500-esg-risk-ratings

Sburstein. (2021). *S&P 500 ESG and stock data* [Dataset]. GitHub. https://github.com/sburstein/ESG-Stock-Data

Securities and Exchange Board of India (SEBI). (2021). *Business responsibility and sustainability reporting by listed entities* (SEBI/LAD-NRO/GN/2021/22). SEBI.

Securities and Exchange Board of India (SEBI). (2023). *BRSR Core — ESG disclosures for value chain* (SEBI/HO/CFD/CFD-SEC-2/P/CIR/2023/122). SEBI.

Serafeim, G., & Yoon, A. (2022). Stock price reactions to ESG news: The role of ESG ratings and disagreement. *Review of Accounting Studies, 28*(3), 1500–1530. https://doi.org/10.1007/s11142-022-09675-3

Sustainalytics. (2023). *ESG risk ratings: Methodology abstract.* Morningstar Sustainalytics. https://www.sustainalytics.com/esg-research/resource/corporate-esg-research/esg-risk-ratings

Tibshirani, R., Walther, G., & Hastie, T. (2001). Estimating the number of clusters in a data set via the gap statistic. *Journal of the Royal Statistical Society: Series B (Statistical Methodology), 63*(2), 411–423. https://doi.org/10.1111/1467-9868.00293

Zinovadr. (n.d.). *S&P 500 companies with financial information* [Dataset]. Kaggle. https://www.kaggle.com/datasets/zinovadr/sp-500-companies-with-financial-information

---

*Data and replication code available at: [GitHub repository link]. All random seeds are fixed (random_state = 42). Python 3.12 with numpy, pandas, scipy, scikit-learn, statsmodels, and scikit-posthocs libraries.*
