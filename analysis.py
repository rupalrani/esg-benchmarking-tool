"""
Project 3 — ESG Performance Benchmarking
Full analysis pipeline: cleaning → EDA → composite scoring →
statistical tests → clustering → temporal drift analysis
Author: Rura | TISS Mumbai | BSc Analytics & Sustainability Studies
Data:
  Primary  : S&P 500 ESG Risk Ratings (Sustainalytics-based, ~2024)
             ggogitidze/SP-500-ESG via kaggle.com/datasets/pritish509/s-and-p-500-esg-risk-ratings
  Financial: S&P 500 Constituents Financials (zinovadr, Kaggle, 2019 vintage)
  Temporal : Yahoo Finance ESG (Sustainalytics 2021) via sburstein/ESG-Stock-Data
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
from scipy.stats import f_oneway, pearsonr, spearmanr, kruskal
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import warnings, json
warnings.filterwarnings("ignore")

CHART_DIR = "/home/claude/outputs/charts"
DATA_DIR  = "/home/claude/outputs/data"

PALETTE = {
    "dark_blue"  : "#003f5c",
    "mid_blue"   : "#2f7db8",
    "teal"       : "#0d8a6e",
    "orange"     : "#e07b39",
    "red"        : "#c0392b",
    "yellow"     : "#f4c842",
    "grey"       : "#7f8c8d",
    "light_grey" : "#ecf0f1",
}
SECTOR_COLORS = [
    "#003f5c","#2f4b7c","#665191","#a05195","#d45087",
    "#f95d6a","#ff7c43","#ffa600","#2f7db8","#0d8a6e","#44b0a8"
]

plt.rcParams.update({
    "font.family"       : "DejaVu Sans",
    "font.size"         : 10,
    "axes.titlesize"    : 12,
    "axes.titleweight"  : "bold",
    "axes.spines.top"   : False,
    "axes.spines.right" : False,
    "figure.dpi"        : 150,
    "savefig.bbox"      : "tight",
    "savefig.dpi"       : 150,
})

RESULTS = {}  # collect all key numbers for report

# ─────────────────────────────────────────────────────────────
# 1. LOAD RAW DATA
# ─────────────────────────────────────────────────────────────
print("1. Loading raw data …")
df_raw = pd.read_csv("/home/claude/sp500esg_repo1/SP 500 ESG Risk Ratings.csv")
df_fin = pd.read_csv("/home/claude/sp500esg_repo1/constituents-financials_csv.csv")
df_yf  = pd.read_csv("/home/claude/esg_yahoo_repo/sp_esg_stock_data.csv")

print(f"   Raw ESG rows  : {len(df_raw)}")
print(f"   Financial rows: {len(df_fin)}")
print(f"   YF 2021 rows  : {len(df_yf)}")

# ─────────────────────────────────────────────────────────────
# 2. CLEAN PRIMARY ESG DATASET
# ─────────────────────────────────────────────────────────────
print("2. Cleaning primary dataset …")
df = df_raw.copy()
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Rename columns to clean names
RENAME = {
    "symbol"               : "ticker",
    "name"                 : "company",
    "full_time_employees"  : "employees_raw",
    "total_esg_risk_score" : "esg_total",
    "environment_risk_score": "esg_env",
    "governance_risk_score" : "esg_gov",
    "social_risk_score"    : "esg_soc",
    "controversy_level"    : "controversy_level",
    "controversy_score"    : "controversy_score",
    "esg_risk_percentile"  : "esg_pct_raw",
    "esg_risk_level"       : "esg_risk_level",
}
df.rename(columns=RENAME, inplace=True, errors="ignore")

# Employee: remove commas, convert to int
def parse_employees(x):
    if pd.isna(x): return np.nan
    return int(str(x).replace(",", "").strip())

df["employees"] = df["employees_raw"].apply(parse_employees)

# ESG percentile: extract numeric
df["esg_percentile"] = (
    df["esg_pct_raw"].astype(str)
    .str.extract(r"(\d+)")[0]
    .astype(float)
)

# Drop rows with no ESG score (73 missing)
df_clean = df.dropna(subset=["esg_total", "esg_env", "esg_soc", "esg_gov"]).copy()
print(f"   After dropping missing ESG: {len(df_clean)} rows")

# Standardise sector names
sector_remap = {"Communication Services": "Comm. Services"}
df_clean["sector"] = df_clean["sector"].replace(sector_remap)
df_clean = df_clean.dropna(subset=["sector"])
print(f"   After dropping missing sector: {len(df_clean)} rows")

# ESG Risk Level: consolidate rare levels
level_order = ["Negligible", "Low", "Medium", "High", "Severe"]
# Fill missing risk levels using percentile thresholds matching Sustainalytics bands
# (Negligible 0-10, Low 10-20, Medium 20-30, High 30-40, Severe 40+)
def impute_level(row):
    if pd.notna(row["esg_risk_level"]): return row["esg_risk_level"]
    s = row["esg_total"]
    if   s < 10 : return "Negligible"
    elif s < 20 : return "Low"
    elif s < 30 : return "Medium"
    elif s < 40 : return "High"
    else        : return "Severe"
df_clean["esg_risk_level"] = df_clean.apply(impute_level, axis=1)
df_clean["esg_risk_level"] = pd.Categorical(df_clean["esg_risk_level"],
                                             categories=level_order, ordered=True)

n_clean = len(df_clean)
RESULTS["n_primary_clean"] = n_clean

# ─────────────────────────────────────────────────────────────
# 3. MERGE FINANCIAL DATA
# ─────────────────────────────────────────────────────────────
print("3. Merging financial data …")
df_fin_clean = df_fin[["Symbol","Market Cap","Price/Earnings","Price/Book",
                        "Dividend Yield","Earnings/Share"]].copy()
df_fin_clean.columns = ["ticker","market_cap","pe_ratio","pb_ratio",
                        "div_yield","eps"]
df_merged = df_clean.merge(df_fin_clean, on="ticker", how="left")
n_with_fin = df_merged["market_cap"].notna().sum()
print(f"   Companies with financial data: {n_with_fin}")
RESULTS["n_with_financials"] = int(n_with_fin)

# ─────────────────────────────────────────────────────────────
# 4. COMPOSITE ESG PERFORMANCE SCORE (OECD method)
# ─────────────────────────────────────────────────────────────
print("4. Building composite ESG score …")
# Sustainalytics: HIGHER score = MORE RISK (worse ESG)
# We invert so that a HIGH composite = GOOD ESG performance
pillars = ["esg_env", "esg_soc", "esg_gov"]
scaler  = MinMaxScaler()

# Normalise each pillar 0-100 (raw scale)
df_merged[["env_norm","soc_norm","gov_norm"]] = (
    scaler.fit_transform(df_merged[pillars]) * 100
)
# Invert so higher = better ESG
for col in ["env_norm","soc_norm","gov_norm"]:
    df_merged[col] = 100 - df_merged[col]

# Weighted composite: E=40%, S=30%, G=30% (SEBI BRSR emphasis on environment)
W_E, W_S, W_G = 0.40, 0.30, 0.30
df_merged["composite_score"] = (
    W_E * df_merged["env_norm"] +
    W_S * df_merged["soc_norm"] +
    W_G * df_merged["gov_norm"]
)

# Equal-weight for sensitivity check
df_merged["composite_eq"] = df_merged[["env_norm","soc_norm","gov_norm"]].mean(axis=1)

# Also invert total ESG score
total_min = df_merged["esg_total"].min()
total_max = df_merged["esg_total"].max()
df_merged["esg_total_inv"] = 100 - (
    (df_merged["esg_total"] - total_min) / (total_max - total_min) * 100
)

# ─────────────────────────────────────────────────────────────
# 5. LEADER / AVERAGE / LAGGARD CLASSIFICATION
# ─────────────────────────────────────────────────────────────
print("5. Classifying leaders / average / laggards …")
q75 = df_merged["composite_score"].quantile(0.75)
q25 = df_merged["composite_score"].quantile(0.25)

def classify(s):
    if s >= q75: return "Leader"
    if s <= q25: return "Laggard"
    return "Average"

df_merged["classification"] = df_merged["composite_score"].apply(classify)
class_counts = df_merged["classification"].value_counts()
RESULTS["classification_counts"] = class_counts.to_dict()
RESULTS["q75_composite"] = round(q75, 2)
RESULTS["q25_composite"] = round(q25, 2)
print(f"   Leaders: {class_counts.get('Leader',0)}  "
      f"Average: {class_counts.get('Average',0)}  "
      f"Laggards: {class_counts.get('Laggard',0)}")

# Top/bottom 10
top10 = df_merged.nlargest(10, "composite_score")[
    ["ticker","company","sector","composite_score","esg_total","esg_risk_level"]]
bot10 = df_merged.nsmallest(10, "composite_score")[
    ["ticker","company","sector","composite_score","esg_total","esg_risk_level"]]
RESULTS["top10_leaders"] = top10.to_dict("records")
RESULTS["top10_laggards"] = bot10.to_dict("records")

# ─────────────────────────────────────────────────────────────
# 6. SECTOR ANALYSIS
# ─────────────────────────────────────────────────────────────
print("6. Sector analysis …")
sector_stats = (
    df_merged.groupby("sector")
    .agg(
        n           = ("ticker","count"),
        mean_total  = ("esg_total","mean"),
        std_total   = ("esg_total","std"),
        mean_env    = ("esg_env","mean"),
        mean_soc    = ("esg_soc","mean"),
        mean_gov    = ("esg_gov","mean"),
        mean_comp   = ("composite_score","mean"),
    )
    .round(2)
    .sort_values("mean_total", ascending=False)
    .reset_index()
)
RESULTS["sector_stats"] = sector_stats.to_dict("records")
print(sector_stats[["sector","n","mean_total","mean_env","mean_soc","mean_gov"]].to_string())

# Sector with most leaders / laggards
sector_class = df_merged.groupby(["sector","classification"]).size().unstack(fill_value=0)
RESULTS["sector_classification"] = sector_class.to_dict()

# ─────────────────────────────────────────────────────────────
# 7. STATISTICAL TESTS
# ─────────────────────────────────────────────────────────────
print("7. Statistical tests …")

# ANOVA: are sector differences in total ESG risk score significant?
sector_groups = [g["esg_total"].values for _, g in df_merged.groupby("sector")]
f_stat, p_anova = f_oneway(*sector_groups)
print(f"   One-way ANOVA: F={f_stat:.3f}, p={p_anova:.4f}")

# Kruskal-Wallis (non-parametric version)
kw_stat, p_kw = kruskal(*sector_groups)
print(f"   Kruskal-Wallis: H={kw_stat:.3f}, p={p_kw:.4f}")

RESULTS["anova"] = {"f_stat": round(f_stat,3), "p_value": round(p_anova,6)}
RESULTS["kruskal"] = {"h_stat": round(kw_stat,3), "p_value": round(p_kw,6)}

# Sensitivity: do E-weight vs equal-weight change classification?
w_esg = df_merged[["composite_score","composite_eq"]].corr().iloc[0,1]
RESULTS["weight_sensitivity_corr"] = round(w_esg, 4)
reclassified = (df_merged.apply(lambda r:
    classify(r["composite_eq"]), axis=1) != df_merged["classification"]).sum()
RESULTS["reclassified_count"] = int(reclassified)
print(f"   Composite correlation (weighted vs equal): {w_esg:.4f}")
print(f"   Companies reclassified by equal weighting: {reclassified}")

# ─────────────────────────────────────────────────────────────
# 8. SIZE BIAS TEST
# ─────────────────────────────────────────────────────────────
print("8. Size bias test (employees vs ESG risk) …")
size_df = df_merged.dropna(subset=["employees","esg_total"]).copy()
size_df["log_employees"] = np.log(size_df["employees"])

r_pearson, p_pearson = pearsonr(size_df["log_employees"], size_df["esg_total"])
r_spear,   p_spear   = spearmanr(size_df["log_employees"], size_df["esg_total"])
print(f"   Pearson  r={r_pearson:.3f} p={p_pearson:.4f}")
print(f"   Spearman ρ={r_spear:.3f}  p={p_spear:.4f}")
RESULTS["size_bias"] = {
    "n": len(size_df),
    "pearson_r": round(r_pearson,4), "pearson_p": round(p_pearson,6),
    "spearman_rho": round(r_spear,4), "spearman_p": round(p_spear,6),
}

# OLS regression (simple)
slope, intercept, r_val, p_val, se = stats.linregress(
    size_df["log_employees"], size_df["esg_total"])
RESULTS["size_regression"] = {
    "slope": round(slope,4), "intercept": round(intercept,4),
    "r_squared": round(r_val**2, 4), "p_value": round(p_val,6),
}

# ─────────────────────────────────────────────────────────────
# 9. TEMPORAL DRIFT ANALYSIS (2021 → 2024, same Sustainalytics provider)
# ─────────────────────────────────────────────────────────────
print("9. Temporal drift analysis (2021 → 2024) …")
df_yf_clean = df_yf.rename(columns={
    "ticker": "ticker",
    "esgScore.tot": "esg_total_2021",
    "esgScore.env": "esg_env_2021",
    "esgScore.soc": "esg_soc_2021",
    "esgScore.gov": "esg_gov_2021",
}).copy()

df_temp = df_merged[["ticker","company","sector",
                      "esg_total","esg_env","esg_soc","esg_gov"]].merge(
    df_yf_clean[["ticker","esg_total_2021","esg_env_2021",
                  "esg_soc_2021","esg_gov_2021","sector"]],
    on="ticker", how="inner", suffixes=("_2024","")
)
df_temp.rename(columns={"sector_x":"sector"}, inplace=True)
df_temp.drop(columns=["sector_y"], inplace=True, errors="ignore")

df_temp["delta_total"] = df_temp["esg_total"] - df_temp["esg_total_2021"]
df_temp["delta_env"]   = df_temp["esg_env"]   - df_temp["esg_env_2021"]
df_temp["delta_soc"]   = df_temp["esg_soc"]   - df_temp["esg_soc_2021"]
df_temp["delta_gov"]   = df_temp["esg_gov"]   - df_temp["esg_gov_2021"]

n_temp = len(df_temp)
mean_delta = df_temp["delta_total"].mean()
median_delta = df_temp["delta_total"].median()
pct_improved = (df_temp["delta_total"] < 0).mean() * 100   # lower score = improved
pct_worsened = (df_temp["delta_total"] > 0).mean() * 100

print(f"   Companies with both years: {n_temp}")
print(f"   Mean delta (+ = worsened): {mean_delta:.3f}")
print(f"   Improved (lower risk): {pct_improved:.1f}%")
print(f"   Worsened (higher risk): {pct_worsened:.1f}%")

# Sector-level drift
sector_drift = (
    df_temp.groupby("sector")
    .agg(n=("delta_total","count"),
         mean_delta=("delta_total","mean"),
         mean_delta_env=("delta_env","mean"),
         mean_delta_soc=("delta_soc","mean"),
         mean_delta_gov=("delta_gov","mean"),
    )
    .round(3)
    .sort_values("mean_delta", ascending=False)
    .reset_index()
)
print(sector_drift.to_string())

# t-test: is mean delta significantly different from zero?
t_stat, p_ttest = stats.ttest_1samp(df_temp["delta_total"].dropna(), 0)
print(f"   t-test vs 0: t={t_stat:.3f}, p={p_ttest:.4f}")

RESULTS["temporal"] = {
    "n": n_temp,
    "mean_delta": round(mean_delta,4),
    "median_delta": round(median_delta,4),
    "pct_improved": round(pct_improved,2),
    "pct_worsened": round(pct_worsened,2),
    "t_stat": round(t_stat,4),
    "p_ttest": round(p_ttest,6),
}
RESULTS["sector_drift"] = sector_drift.to_dict("records")

# ─────────────────────────────────────────────────────────────
# 10. K-MEANS CLUSTERING
# ─────────────────────────────────────────────────────────────
print("10. K-means clustering …")
cluster_features = ["env_norm","soc_norm","gov_norm"]
X_cl = df_merged[cluster_features].dropna()
idx_cl = X_cl.index

# Elbow + silhouette for k=2..6
inertias, silhouettes = [], []
K_range = range(2, 7)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_cl)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_cl, labels))
    print(f"   k={k}: inertia={km.inertia_:.1f}, silhouette={silhouette_score(X_cl,labels):.4f}")

best_k = K_range.start + int(np.argmax(silhouettes))
print(f"   Best k by silhouette: {best_k}")
km_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df_merged.loc[idx_cl, "cluster"] = km_final.fit_predict(X_cl)
df_merged["cluster"] = df_merged["cluster"].fillna(-1).astype(int)

# Cluster profiles
cluster_profile = (
    df_merged[df_merged["cluster"] >= 0]
    .groupby("cluster")
    .agg(n=("ticker","count"),
         mean_total=("esg_total","mean"),
         mean_env=("esg_env","mean"),
         mean_soc=("esg_soc","mean"),
         mean_gov=("esg_gov","mean"),
         mean_comp=("composite_score","mean"))
    .round(2)
)
print(cluster_profile)

RESULTS["clustering"] = {
    "best_k": best_k,
    "best_silhouette": round(max(silhouettes), 4),
    "cluster_profile": cluster_profile.reset_index().to_dict("records"),
}

# PCA for 2D visualization
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_cl)
RESULTS["pca_variance"] = [round(v,4) for v in pca.explained_variance_ratio_]
print(f"   PCA explained variance: {pca.explained_variance_ratio_}")

# ─────────────────────────────────────────────────────────────
# 11. EXPORT CLEAN CSVs
# ─────────────────────────────────────────────────────────────
print("11. Exporting clean CSVs …")
df_merged.to_csv(f"{DATA_DIR}/sp500_esg_analysis.csv", index=False)
sector_stats.to_csv(f"{DATA_DIR}/sector_summary.csv", index=False)
df_temp.to_csv(f"{DATA_DIR}/temporal_drift.csv", index=False)
top10.to_csv(f"{DATA_DIR}/top10_leaders.csv", index=False)
bot10.to_csv(f"{DATA_DIR}/top10_laggards.csv", index=False)
cluster_profile.to_csv(f"{DATA_DIR}/cluster_profiles.csv")

# ─────────────────────────────────────────────────────────────
# 12. VISUALIZATIONS
# ─────────────────────────────────────────────────────────────
print("12. Building charts …")

# ── CHART 1: ESG Risk Score Distribution ─────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Distribution of Sustainalytics ESG Risk Scores — S&P 500 Companies",
             fontsize=13, fontweight="bold", y=1.01)

ax = axes[0]
ax.hist(df_merged["esg_total"].dropna(), bins=30,
        color=PALETTE["mid_blue"], edgecolor="white", linewidth=0.5, alpha=0.9)
mu = df_merged["esg_total"].mean()
sd = df_merged["esg_total"].std()
ax.axvline(mu, color=PALETTE["orange"], lw=2, ls="--", label=f"Mean = {mu:.1f}")
ax.axvline(mu - sd, color=PALETTE["grey"], lw=1.5, ls=":", label=f"±1 SD ({mu-sd:.1f} – {mu+sd:.1f})")
ax.axvline(mu + sd, color=PALETTE["grey"], lw=1.5, ls=":")
ax.set_xlabel("Total ESG Risk Score (0 = lowest risk, 40+ = severe)")
ax.set_ylabel("Number of Companies")
ax.set_title("Overall Score Distribution")
ax.legend(fontsize=9)
# add risk-level bands
for lo, hi, label, col in [
    (0,10,"Negligible","#27ae60"),(10,20,"Low","#2ecc71"),
    (20,30,"Medium","#f39c12"),(30,40,"High","#e67e22"),(40,50,"Severe","#c0392b")
]:
    ax.axvspan(lo, hi, alpha=0.06, color=col)
    ax.text((lo+hi)/2, ax.get_ylim()[1]*0.93, label,
            ha="center", fontsize=7, color=col)

ax2 = axes[1]
risk_counts = df_merged["esg_risk_level"].value_counts().reindex(level_order).dropna()
colors = ["#27ae60","#2ecc71","#f39c12","#e67e22","#c0392b"]
bars = ax2.bar(risk_counts.index, risk_counts.values,
               color=colors[:len(risk_counts)], edgecolor="white", width=0.6)
for bar, val in zip(bars, risk_counts.values):
    ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5,
             str(int(val)), ha="center", va="bottom", fontsize=9, fontweight="bold")
ax2.set_xlabel("Sustainalytics ESG Risk Level")
ax2.set_ylabel("Number of Companies")
ax2.set_title("Companies by Risk Level")

plt.tight_layout()
plt.savefig(f"{CHART_DIR}/01_esg_score_distribution.png")
plt.close()
RESULTS["n_clean"] = n_clean
RESULTS["mean_esg"] = round(mu, 2)
RESULTS["sd_esg"] = round(sd, 2)

# ── CHART 2: Sector ESG Risk (sorted bar) ────────────────────
fig, ax = plt.subplots(figsize=(11, 6))
ss = sector_stats.sort_values("mean_total", ascending=True)
y_pos = range(len(ss))
colors_s = [SECTOR_COLORS[i % len(SECTOR_COLORS)] for i in range(len(ss))]
bars = ax.barh(list(y_pos), ss["mean_total"], color=colors_s,
               height=0.65, edgecolor="white")
for bar, std_val in zip(bars, ss["std_total"]):
    x = bar.get_width()
    ax.errorbar(x, bar.get_y()+bar.get_height()/2,
                xerr=std_val, fmt="none", color="#555", capsize=3, lw=1.5)
    ax.text(x + 0.4, bar.get_y()+bar.get_height()/2,
            f"{x:.1f}", va="center", fontsize=9, fontweight="bold")
ax.set_yticks(list(y_pos))
ax.set_yticklabels(ss["sector"], fontsize=10)
ax.set_xlabel("Mean Total ESG Risk Score (lower = less risk)")
ax.set_title("Mean ESG Risk Score by GICS Sector — S&P 500 (Sustainalytics, ~2024)",
             pad=12)
grand_mean = df_merged["esg_total"].mean()
ax.axvline(grand_mean, color=PALETTE["orange"], ls="--", lw=1.5,
           label=f"Grand mean = {grand_mean:.1f}")
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/02_sector_esg_risk.png")
plt.close()

# ── CHART 3: Pillar Box Plots by Sector ──────────────────────
pillar_labels = {"esg_env": "Environment", "esg_soc": "Social", "esg_gov": "Governance"}
fig, axes = plt.subplots(3, 1, figsize=(13, 14), sharex=True)
fig.suptitle("ESG Pillar Risk Scores by Sector — S&P 500", fontsize=13,
             fontweight="bold", y=1.005)
sectors_sorted = sector_stats.sort_values("mean_total", ascending=False)["sector"].tolist()
for ax, (col, lab) in zip(axes, pillar_labels.items()):
    data_by_sector = [df_merged[df_merged["sector"]==s][col].dropna().values
                      for s in sectors_sorted]
    bp = ax.boxplot(data_by_sector, patch_artist=True, vert=True,
                    medianprops=dict(color=PALETTE["orange"], lw=2),
                    flierprops=dict(marker=".", color=PALETTE["grey"],
                                   alpha=0.5, markersize=4))
    for i, patch in enumerate(bp["boxes"]):
        patch.set_facecolor(SECTOR_COLORS[i % len(SECTOR_COLORS)])
        patch.set_alpha(0.7)
    ax.set_xticks(range(1, len(sectors_sorted)+1))
    ax.set_xticklabels(sectors_sorted, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel(f"{lab} Risk Score", fontsize=10)
    ax.set_title(f"{lab} Risk by Sector", fontsize=11)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/03_pillar_boxplots_sector.png")
plt.close()

# ── CHART 4: Classification Breakdown by Sector ──────────────
fig, ax = plt.subplots(figsize=(12, 6))
sc_df = df_merged.groupby(["sector","classification"]).size().unstack(fill_value=0)
for cls_col in ["Leader","Average","Laggard"]:
    if cls_col not in sc_df.columns: sc_df[cls_col] = 0
sc_df = sc_df[["Leader","Average","Laggard"]]
sc_df_pct = sc_df.div(sc_df.sum(axis=1), axis=0) * 100
sc_df_pct = sc_df_pct.loc[sector_stats.sort_values("mean_total", ascending=False)["sector"]]
sc_df_pct.plot(kind="barh", stacked=True,
               color=[PALETTE["teal"], PALETTE["yellow"], PALETTE["red"]],
               ax=ax, width=0.65, edgecolor="white")
ax.set_xlabel("Proportion of Companies (%)")
ax.set_title("Leader / Average / Laggard Classification by Sector (%)", pad=12)
ax.legend(title="Classification", bbox_to_anchor=(1, 1), loc="upper left")
for i, (sector, row) in enumerate(sc_df_pct.iterrows()):
    cum = 0
    for cls in ["Leader","Average","Laggard"]:
        pct = row.get(cls, 0)
        if pct > 5:
            ax.text(cum + pct/2, i, f"{pct:.0f}%",
                    ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        cum += pct
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/04_classification_by_sector.png")
plt.close()

# ── CHART 5: Composite Score Distribution ────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
comp_vals = df_merged["composite_score"]
ax.hist(comp_vals, bins=30, color=PALETTE["teal"],
        edgecolor="white", linewidth=0.5, alpha=0.9)
ax.axvline(q75, color=PALETTE["teal"], lw=2, ls="--", label=f"Leader threshold (≥{q75:.1f})")
ax.axvline(q25, color=PALETTE["red"], lw=2, ls="--", label=f"Laggard threshold (≤{q25:.1f})")
ax.set_xlabel("Composite ESG Performance Score (higher = better, 0–100 scale)")
ax.set_ylabel("Number of Companies")
ax.set_title("Composite ESG Performance Score Distribution — S&P 500\n"
             "(E=40%, S=30%, G=30%, inverted Sustainalytics risk scale)")
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/05_composite_score_distribution.png")
plt.close()

# ── CHART 6: Size Bias — Log Employees vs ESG Total ─────────
fig, ax = plt.subplots(figsize=(9, 6))
scatter_df = size_df.copy()
level_color_map = {
    "Negligible": "#27ae60", "Low": "#2ecc71",
    "Medium": "#f39c12", "High": "#e67e22", "Severe": "#c0392b"
}
for lvl, grp in scatter_df.groupby("esg_risk_level"):
    ax.scatter(grp["log_employees"], grp["esg_total"],
               c=level_color_map.get(str(lvl), PALETTE["grey"]),
               alpha=0.55, s=28, label=str(lvl), edgecolors="none")
# Regression line
x_range = np.linspace(scatter_df["log_employees"].min(),
                      scatter_df["log_employees"].max(), 200)
ax.plot(x_range, slope*x_range + intercept,
        color=PALETTE["dark_blue"], lw=2.5, ls="--",
        label=f"OLS fit  r²={r_val**2:.3f}")
ax.set_xlabel("ln(Full-Time Employees)")
ax.set_ylabel("Total ESG Risk Score (higher = more risk)")
ax.set_title(f"Size Bias: Company Size vs ESG Risk Score\n"
             f"Pearson r = {r_pearson:.3f}, p = {p_pearson:.4f} "
             f"(n = {len(scatter_df)})")
ax.legend(title="ESG Risk Level", fontsize=9)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/06_size_bias.png")
plt.close()

# ── CHART 7: Temporal Drift — Distribution of Δ Score ────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("ESG Score Evolution: 2021 → 2024 (Sustainalytics)\n"
             f"Same provider, n = {n_temp} overlapping S&P 500 companies",
             fontsize=12, fontweight="bold")
ax = axes[0]
ax.hist(df_temp["delta_total"], bins=30,
        color=PALETTE["mid_blue"], edgecolor="white", linewidth=0.5, alpha=0.9)
ax.axvline(0, color="black", lw=1.5, ls="-")
ax.axvline(mean_delta, color=PALETTE["orange"], lw=2, ls="--",
           label=f"Mean Δ = {mean_delta:+.2f}")
ax.set_xlabel("Δ ESG Risk Score (positive = risk increased, i.e. worsened)")
ax.set_ylabel("Number of Companies")
ax.set_title("Distribution of Score Change (2021 → 2024)")
ax.legend(fontsize=9)

ax2 = axes[1]
sd2 = sector_drift.sort_values("mean_delta", ascending=True)
bar_colors = [PALETTE["teal"] if x < 0 else PALETTE["red"] for x in sd2["mean_delta"]]
ax2.barh(sd2["sector"], sd2["mean_delta"], color=bar_colors,
         height=0.65, edgecolor="white")
ax2.axvline(0, color="black", lw=1.2)
for i, (val, n_val) in enumerate(zip(sd2["mean_delta"], sd2["n"])):
    ax2.text(val + (0.1 if val >= 0 else -0.1),
             i, f"{val:+.2f} (n={n_val})",
             va="center", ha="left" if val >= 0 else "right", fontsize=8)
ax2.set_xlabel("Mean Δ ESG Risk Score\n(negative = improvement, positive = worsened)")
ax2.set_title("Score Change by Sector (2021 → 2024)")
improved_patch = mpatches.Patch(color=PALETTE["teal"], label="Improved (lower risk)")
worsened_patch = mpatches.Patch(color=PALETTE["red"], label="Worsened (higher risk)")
ax2.legend(handles=[improved_patch, worsened_patch], fontsize=8)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/07_temporal_drift.png")
plt.close()

# ── CHART 8: K-Means Cluster Plot (PCA 2D) ───────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("K-Means ESG Cluster Analysis — S&P 500 Companies",
             fontsize=12, fontweight="bold")

ax = axes[0]
cluster_colors = [PALETTE["dark_blue"], PALETTE["teal"], PALETTE["orange"],
                  PALETTE["red"], PALETTE["mid_blue"]]
cl_labels = km_final.fit_predict(X_cl)
for ci in range(best_k):
    mask = cl_labels == ci
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1],
               c=cluster_colors[ci], alpha=0.55, s=28,
               label=f"Cluster {ci+1}", edgecolors="none")
ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")
ax.set_title("PCA — 2D Cluster Projection")
ax.legend(fontsize=9)

ax2 = axes[1]
k_range_list = list(K_range)
ax2b = ax2.twinx()
ax2.plot(k_range_list, inertias, "o--", color=PALETTE["mid_blue"], lw=2, label="Inertia")
ax2b.plot(k_range_list, silhouettes, "s-", color=PALETTE["orange"], lw=2, label="Silhouette")
ax2.set_xlabel("Number of Clusters (k)")
ax2.set_ylabel("Inertia (Within-cluster SSE)", color=PALETTE["mid_blue"])
ax2b.set_ylabel("Silhouette Score", color=PALETTE["orange"])
ax2.set_title("Elbow & Silhouette Analysis")
ax2.set_xticks(k_range_list)
lines1, lab1 = ax2.get_legend_handles_labels()
lines2, lab2 = ax2b.get_legend_handles_labels()
ax2.legend(lines1+lines2, lab1+lab2, fontsize=9)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/08_clustering.png")
plt.close()

# ── CHART 9: Top 10 Leaders & Laggards ───────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("Top 10 ESG Leaders & Laggards — S&P 500 Composite Score",
             fontsize=12, fontweight="bold")
for ax, df_10, color, title in [
    (axes[0], top10.iloc[::-1], PALETTE["teal"], "Top 10 Leaders"),
    (axes[1], bot10.iloc[::-1], PALETTE["red"],  "Top 10 Laggards"),
]:
    bars = ax.barh(df_10["ticker"], df_10["composite_score"],
                   color=color, height=0.6, edgecolor="white", alpha=0.85)
    for bar, co, sec in zip(bars, df_10["composite_score"], df_10["sector"]):
        ax.text(bar.get_width() + 0.5, bar.get_y()+bar.get_height()/2,
                f"{co:.1f} | {sec}", va="center", fontsize=7.5)
    ax.set_xlabel("Composite ESG Performance Score")
    ax.set_title(title)
    ax.set_xlim(0, 100)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/09_leaders_laggards.png")
plt.close()

# ── CHART 10: Controversy Level Heatmap ──────────────────────
df_merged["controversy_num"] = (
    df_merged["controversy_level"]
    .map({"Negligible": 0, "Low": 1, "Medium": 2,
          "Significant": 3, "High": 4, "Severe": 5})
)
ct_heat = df_merged.groupby(["sector","esg_risk_level"])["controversy_num"].mean().unstack()
ct_heat = ct_heat.reindex(columns=level_order)

fig, ax = plt.subplots(figsize=(10, 7))
im = ax.imshow(ct_heat.values, aspect="auto", cmap="RdYlGn_r", vmin=0, vmax=3)
ax.set_xticks(range(len(ct_heat.columns)))
ax.set_xticklabels(ct_heat.columns, fontsize=10)
ax.set_yticks(range(len(ct_heat.index)))
ax.set_yticklabels(ct_heat.index, fontsize=10)
for i in range(len(ct_heat.index)):
    for j in range(len(ct_heat.columns)):
        val = ct_heat.values[i, j]
        if not np.isnan(val):
            ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                    fontsize=9, color="black" if 0.8 < val < 2.5 else "white")
plt.colorbar(im, ax=ax, label="Mean Controversy Score (0=Negligible → 5=Severe)")
ax.set_title("Mean Controversy Score: Sector × ESG Risk Level\n"
             "(S&P 500, Sustainalytics ~2024)", pad=12)
ax.set_xlabel("ESG Risk Level")
ax.set_ylabel("Sector")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/10_controversy_heatmap.png")
plt.close()

print("All 10 charts saved.")

# ─────────────────────────────────────────────────────────────
# 13. SAVE KEY RESULTS JSON
# ─────────────────────────────────────────────────────────────
with open(f"{DATA_DIR}/key_results.json", "w") as f:
    json.dump(RESULTS, f, indent=2, default=str)

# ── extra summary for report writing
print("\n══════════════════════════════════════════")
print("KEY NUMBERS FOR REPORT")
print("══════════════════════════════════════════")
print(f"N (clean primary)     : {n_clean}")
print(f"Mean ESG risk score   : {mu:.2f} ± {sd:.2f}")
print(f"Sector ANOVA F / p    : {f_stat:.3f} / {p_anova:.6f}")
print(f"Kruskal-Wallis H / p  : {kw_stat:.3f} / {p_kw:.6f}")
print(f"Size-bias Pearson r/p : {r_pearson:.3f} / {p_pearson:.4f}")
print(f"Size-bias Spearman ρ/p: {r_spear:.3f} / {p_spear:.4f}")
print(f"Size OLS slope / r²   : {slope:.4f} / {r_val**2:.4f}")
print(f"Weight sensitivity r  : {w_esg:.4f}  reclassified: {reclassified}")
print(f"Temporal n / Δ mean   : {n_temp} / {mean_delta:+.3f}")
print(f"Temporal t / p        : {t_stat:.3f} / {p_ttest:.4f}")
print(f"% improved 2021→2024  : {pct_improved:.1f}%")
print(f"Best k (silhouette)   : {best_k}  score={max(silhouettes):.4f}")
print("\nSector means (sorted high→low risk):")
print(sector_stats[["sector","n","mean_total","mean_env","mean_soc","mean_gov"]].to_string(index=False))
print("\nTop sector drift (2021→2024):")
print(sector_drift[["sector","n","mean_delta","mean_delta_env","mean_delta_soc","mean_delta_gov"]].to_string(index=False))
print("\nTop 10 leaders:")
print(top10[["ticker","company","sector","composite_score","esg_total"]].to_string(index=False))
print("\nTop 10 laggards:")
print(bot10[["ticker","company","sector","composite_score","esg_total"]].to_string(index=False))
print("\nCluster profiles:")
print(cluster_profile.to_string())
PYEOF