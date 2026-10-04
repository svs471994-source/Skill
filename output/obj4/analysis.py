"""Objective 4 - community perception of urban green space (Bengaluru).
Reproducible analysis: python analysis.py <responses.xlsx>
Writes tables (CSV), figures (PNG, 300 dpi) and results.json next to this file.
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from scipy.optimize import minimize
from statsmodels.stats.multitest import multipletests

OUT = Path(__file__).parent
FIG = OUT / "figs"
FIG.mkdir(exist_ok=True)
RNG = np.random.default_rng(20240)

d = pd.read_excel(sys.argv[1])
N = len(d)
DIMS = {
    "Usage & access": range(7, 12),
    "Environmental perception": range(12, 18),
    "Vegetation & climate awareness": range(18, 24),
    "Soil & ecological function": range(24, 30),
    "Governance & management": range(30, 36),
}
SHORT = {"Usage & access": "USE", "Environmental perception": "ENV",
         "Vegetation & climate awareness": "VEG", "Soil & ecological function": "SOIL",
         "Governance & management": "GOV"}
CLASS = {1: "I Urban forest", 2: "II Managed parks", 3: "III Institutional",
         4: "IV Lake-riparian", 5: "V Grassland/scrub", 6: "VI Neighbourhood", 7: "VII Avenue"}
items = {dim: [f"Q{i}_code" for i in r] for dim, r in DIMS.items()}
allq = [c for v in items.values() for c in v]
for dim, cols in items.items():
    d[dim] = d[cols].mean(axis=1)
d["GSPI"] = d[list(DIMS)].mean(axis=1)
to100 = lambda x: (x - 1) / 4 * 100
R = {"N": N}




def varimax(Phi_, gamma=1.0, q=100, tol=1e-8):
    p_, k_ = Phi_.shape
    Rm = np.eye(k_)
    dd = 0
    for _ in range(q):
        Lm = Phi_ @ Rm
        u, sv, vh = np.linalg.svd(Phi_.T @ (Lm ** 3 - (gamma / p_) * Lm @ np.diag(np.diag(Lm.T @ Lm))))
        Rm = u @ vh
        dn_ = sv.sum()
        if dd != 0 and dn_ / dd < 1 + tol:
            break
        dd = dn_
    return Phi_ @ Rm


def kmo_overall(Xm):
    C = np.corrcoef(Xm.T)
    Inv = np.linalg.inv(C)
    Pm = -Inv / np.sqrt(np.outer(np.diag(Inv), np.diag(Inv)))
    np.fill_diagonal(C, 0); np.fill_diagonal(Pm, 0)
    return (C ** 2).sum() / ((C ** 2).sum() + (Pm ** 2).sum())

def boot_ci(x, f=np.mean, B=5000):
    x = np.asarray(x)
    bs = [f(x[RNG.integers(0, len(x), len(x))]) for _ in range(B)]
    return np.percentile(bs, [2.5, 97.5])


# ---- sample profile -------------------------------------------------------
prof = {}
for c in ["Age", "Gender", "Education", "Occupation", "Residence", "GreenType"]:
    prof[c] = d[c].value_counts().to_dict()
R["profile"] = prof
d.groupby("GreenType").size().to_frame("n").to_csv(OUT / "t_class_n.csv")

# ---- item descriptives ----------------------------------------------------
rows = []
for q in range(7, 36):
    x = d[f"Q{q}_code"]
    rows.append({"item": f"Q{q}", "mean": x.mean(), "sd": x.std(), "pct_agree": (x >= 4).mean() * 100,
                 "pct_neutral": (x == 3).mean() * 100, "pct_disagree": (x <= 2).mean() * 100,
                 "skew": stats.skew(x)})
pd.DataFrame(rows).round(2).to_csv(OUT / "t_items.csv", index=False)

# ---- index descriptives ---------------------------------------------------
rows = []
for v in list(DIMS) + ["GSPI"]:
    x = to100(d[v])
    lo, hi = boot_ci(x)
    rows.append({"index": v, "mean100": x.mean(), "ci_lo": lo, "ci_hi": hi, "sd100": x.std(),
                 "median100": x.median(), "mean15": d[v].mean()})
idx = pd.DataFrame(rows)
idx.round(1).to_csv(OUT / "t_indexes.csv", index=False)
R["indexes"] = idx.round(2).to_dict("records")

# ---- reliability ----------------------------------------------------------
def alpha(X):
    k = X.shape[1]
    return k / (k - 1) * (1 - X.var(ddof=1).sum() / X.sum(axis=1).var(ddof=1))


R["alpha"] = {dim: round(alpha(d[c]), 3) for dim, c in items.items()}
R["alpha"]["all29"] = round(alpha(d[allq]), 3)

# ---- factorability, parallel analysis, EFA --------------------------------
X = d[allq]
Cm = np.corrcoef(X.T)
chi = -(N - 1 - (2 * 29 + 5) / 6) * np.log(np.linalg.det(Cm))
p = stats.chi2.sf(chi, 29 * 28 // 2)
kmo = kmo_overall(X.to_numpy(float))
R["kmo"], R["bartlett"] = round(kmo, 3), {"chi2": round(chi, 1), "p": float(p), "df": 29 * 28 // 2}
ev = np.linalg.eigvalsh(Cm)[::-1]
sim = np.array([np.linalg.eigvalsh(np.corrcoef(RNG.integers(1, 6, X.shape).T.astype(float)))[::-1]
                for _ in range(500)])
pa = np.percentile(sim, 95, axis=0)
R["eigenvalues"] = ev[:8].round(2).tolist()
R["parallel_95"] = pa[:8].round(2).tolist()
R["n_factors_parallel"] = int((ev > pa).sum())
R["harman_first_pct"] = round(ev[0] / 29 * 100, 1)
w_, v_ = np.linalg.eigh(Cm)
o_ = np.argsort(w_)[::-1][:5]
Lraw = v_[:, o_] * np.sqrt(w_[o_])
Lv = varimax(Lraw)
for j in range(5):
    if Lv[:, j].sum() < 0:
        Lv[:, j] *= -1
load = pd.DataFrame(Lv, index=[f"Q{q}" for q in range(7, 36)], columns=[f"F{i+1}" for i in range(5)])
load.round(2).to_csv(OUT / "t_efa_loadings.csv")
R["efa_var_explained_pct"] = round(float((Lv ** 2).sum() / 29 * 100), 1)
R["efa_crossloadings_ge_0.40"] = int(((load.abs() >= 0.40).sum(axis=1) > 1).sum())
R["efa_primary_matches_design"] = bool(all(
    load.iloc[[q - 7 for q in r_]].abs().mean().idxmax() == load.iloc[[q - 7 for q in r_]].abs().mean().idxmax() for r_ in DIMS.values()))

# ---- CFA (5 correlated factors, ML, standardised latent variances) ---------
Xs = d[allq].to_numpy(float)
S = np.cov(Xs.T, ddof=1)
p_obs = S.shape[0]
fac_of = np.repeat(np.arange(5), [len(v) for v in items.values()])
iu = np.triu_indices(5, 1)


def sigma(theta):
    lam = np.zeros((p_obs, 5))
    lam[np.arange(p_obs), fac_of] = theta[:p_obs]
    th = np.exp(theta[p_obs:2 * p_obs])
    Phi = np.eye(5)
    Phi[iu] = np.tanh(theta[2 * p_obs:])
    Phi = Phi + Phi.T - np.eye(5)
    return lam @ Phi @ lam.T + np.diag(th), lam, th, Phi


def fml(theta):
    Sg = sigma(theta)[0]
    sgn, ld = np.linalg.slogdet(Sg)
    if sgn <= 0:
        return 1e6
    return ld + np.trace(S @ np.linalg.inv(Sg)) - np.linalg.slogdet(S)[1] - p_obs


t0 = np.concatenate([np.full(p_obs, 0.7), np.log(np.full(p_obs, 0.5)), np.full(10, 0.4)])
res = minimize(fml, t0, method="L-BFGS-B", options={"maxiter": 5000, "maxfun": 200000})
Sg, lam, th, Phi = sigma(res.x)
F = res.fun
q_par = p_obs * 2 + 10
df_m = p_obs * (p_obs + 1) // 2 - q_par
chi2 = (N - 1) * F
# baseline (independence) model
Fb = np.sum(np.log(np.diag(S))) - np.linalg.slogdet(S)[1]
chi_b, df_b = (N - 1) * Fb, p_obs * (p_obs - 1) // 2
cfi = 1 - max(chi2 - df_m, 0) / max(chi_b - df_b, chi2 - df_m, 1e-9)
tli = ((chi_b / df_b) - (chi2 / df_m)) / ((chi_b / df_b) - 1)
rmsea = np.sqrt(max(chi2 - df_m, 0) / (df_m * (N - 1)))
Dm = np.diag(1 / np.sqrt(np.diag(S)))
resid = Dm @ (S - Sg) @ Dm
srmr = np.sqrt(np.mean(resid[np.tril_indices(p_obs)] ** 2))
std_load = lam[np.arange(p_obs), fac_of] / np.sqrt(np.diag(Sg))
R["cfa"] = {"chi2": round(chi2, 1), "df": df_m, "chi2_df": round(chi2 / df_m, 2), "CFI": round(cfi, 3),
            "TLI": round(tli, 3), "RMSEA": round(rmsea, 3), "SRMR": round(srmr, 3),
            "converged": bool(res.success)}
# single-factor comparison model
def sigma1(theta):
    l = theta[:p_obs]
    return np.outer(l, l) + np.diag(np.exp(theta[p_obs:]))


def f1(theta):
    Sg1 = sigma1(theta)
    sgn, ld = np.linalg.slogdet(Sg1)
    return 1e6 if sgn <= 0 else ld + np.trace(S @ np.linalg.inv(Sg1)) - np.linalg.slogdet(S)[1] - p_obs


r1 = minimize(f1, np.concatenate([np.full(p_obs, 0.6), np.log(np.full(p_obs, 0.6))]), method="L-BFGS-B",
              options={"maxiter": 5000, "maxfun": 200000})
chi1, df1 = (N - 1) * r1.fun, p_obs * (p_obs + 1) // 2 - 2 * p_obs
R["cfa_single_factor"] = {"chi2": round(chi1, 1), "df": df1,
                          "CFI": round(1 - max(chi1 - df1, 0) / max(chi_b - df_b, chi1 - df1), 3),
                          "RMSEA": round(np.sqrt(max(chi1 - df1, 0) / (df1 * (N - 1))), 3)}
R["cfa_delta_chi2"] = {"delta": round(chi1 - chi2, 1), "df": df1 - df_m}
rel = []
for k, dim in enumerate(DIMS):
    m = fac_of == k
    l = std_load[m]
    e = 1 - l ** 2
    rel.append({"dimension": dim, "k": int(m.sum()), "alpha": R["alpha"][dim],
                "omega": (l.sum() ** 2) / (l.sum() ** 2 + e.sum()), "AVE": (l ** 2).mean(),
                "min_loading": l.min(), "max_loading": l.max()})
rel = pd.DataFrame(rel)
rel.round(3).to_csv(OUT / "t_reliability.csv", index=False)
R["reliability"] = rel.round(3).to_dict("records")
dn = list(DIMS)
Rr = np.corrcoef(d[dn].T)
# discriminant validity: sqrt(AVE) vs inter-factor correlations (latent)
R["factor_corr_latent"] = np.round(Phi, 2).tolist()
R["fornell_larcker_ok"] = bool(all(np.sqrt(rel.AVE.iloc[i]) > abs(Phi[i, j])
                                   for i in range(5) for j in range(5) if i != j))
R["max_latent_corr"] = round(float(np.max(np.abs(Phi[iu]))), 2)
R["index_corr"] = pd.DataFrame(Rr, index=dn, columns=dn).round(2).to_dict()

# ---- confirmatory family of group tests (Holm over all) --------------------
GROUPS = {"Green-space class": "GreenType_code", "Length of residence": "Residence_code",
          "Education": "Education_code", "Age": "Age_code", "Occupation": "Occupation_code",
          "Gender": "Gender_code"}
rows = []
for gname, g in GROUPS.items():
    for v in dn + ["GSPI"]:
        grp = [x[v].values for _, x in d.groupby(g)]
        H, pv = stats.kruskal(*grp)
        k = len(grp)
        rows.append({"factor": gname, "outcome": v, "H": H, "df": k - 1, "p": pv,
                     "eps2": (H - k + 1) / (N - k)})
kw = pd.DataFrame(rows)
kw["p_holm"] = multipletests(kw.p, method="holm")[1]
kw["sig_raw"] = kw.p < 0.05
kw["sig_holm"] = kw.p_holm < 0.05
kw.round(4).to_csv(OUT / "t_group_tests.csv", index=False)
R["n_tests"] = len(kw)
R["n_sig_raw"] = int(kw.sig_raw.sum())
R["n_sig_holm"] = int(kw.sig_holm.sum())
R["sig_holm"] = kw[kw.sig_holm].round(4).to_dict("records")
R["sig_raw_only"] = kw[kw.sig_raw & ~kw.sig_holm].round(4).to_dict("records")

# post hoc (Mann-Whitney, Holm) for Holm-significant effects
post = {}
for _, r_ in kw[kw.sig_holm].iterrows():
    g = GROUPS[r_.factor]
    lv = sorted(d[g].unique())
    pr = []
    for i in range(len(lv)):
        for j in range(i + 1, len(lv)):
            a, b = d[d[g] == lv[i]][r_.outcome], d[d[g] == lv[j]][r_.outcome]
            U, pv = stats.mannwhitneyu(a, b)
            pr.append((lv[i], lv[j], pv, 1 - 2 * U / (len(a) * len(b)) * -1 if False else (2 * U / (len(a) * len(b)) - 1)))
    adj = multipletests([x[2] for x in pr], method="holm")[1]
    post[f"{r_.factor}->{r_.outcome}"] = [{"a": int(a), "b": int(b), "p_holm": round(float(pa_), 4),
                                           "rank_biserial": round(float(rb), 2)}
                                          for (a, b, _, rb), pa_ in zip(pr, adj) if pa_ < 0.05]
R["posthoc"] = post

# ---- class profile ---------------------------------------------------------
prof = d.groupby("GreenType_code").agg(n=("ID", "size"))
for v in dn + ["GSPI"]:
    prof[v] = to100(d.groupby("GreenType_code")[v].mean())
prof.index = [CLASS[i] for i in prof.index]
prof.round(1).to_csv(OUT / "t_class_profile.csv")
R["class_profile"] = prof.round(1).reset_index().to_dict("records")

# residence profile
rp = d.groupby("Residence_code").agg(n=("ID", "size"))
for v in dn + ["GSPI"]:
    rp[v] = to100(d.groupby("Residence_code")[v].mean())
rp.index = ["<1 yr", "1-5 yr", "6-10 yr", ">10 yr"]
rp.round(1).to_csv(OUT / "t_residence_profile.csv")
R["residence_profile"] = rp.round(1).reset_index().to_dict("records")

# ---- appreciation-awareness gap (H4) ---------------------------------------
ENV, SOIL, VEG, GOV = [d[k] for k in ["Environmental perception", "Soil & ecological function",
                                      "Vegetation & climate awareness", "Governance & management"]]
gap = to100(ENV) - to100(SOIL)
d["gap"] = gap
w = stats.wilcoxon(ENV, SOIL)
dz = (ENV - SOIL).mean() / (ENV - SOIL).std()
R["gap_overall"] = {"mean": round(gap.mean(), 1), "ci": boot_ci(gap).round(1).tolist(),
                    "wilcoxon_p": float(w.pvalue), "dz": round(dz, 2),
                    "pct_env_gt_soil": round(float((ENV > SOIL).mean() * 100), 1),
                    "pct_equal": round(float((ENV == SOIL).mean() * 100), 1)}
R["pairwise_dims"] = {}
for a, b in [("Environmental perception", "Governance & management"),
             ("Soil & ecological function", "Governance & management"),
             ("Vegetation & climate awareness", "Soil & ecological function")]:
    ww = stats.wilcoxon(d[a], d[b])
    R["pairwise_dims"][f"{SHORT[a]}-{SHORT[b]}"] = {"mean_diff100": round(float(to100(d[a]).mean() - to100(d[b]).mean()), 1),
                                                     "p": float(ww.pvalue)}
rows = []
for k, g in d.groupby("GreenType_code"):
    lo, hi = boot_ci(g.gap, B=5000)
    ww = stats.wilcoxon(g.Environmental_perception if False else g["Environmental perception"],
                        g["Soil & ecological function"])
    rows.append({"class": CLASS[k], "n": len(g), "gap": g.gap.mean(), "lo": lo, "hi": hi, "p_wilcoxon": ww.pvalue})
gp = pd.DataFrame(rows)
gp["p_holm"] = multipletests(gp.p_wilcoxon, method="holm")[1]
gp.round(3).to_csv(OUT / "t_gap_by_class.csv", index=False)
R["gap_by_class"] = gp.round(3).to_dict("records")
Hg, pg = stats.kruskal(*[g.gap.values for _, g in d.groupby("GreenType_code")])
R["gap_heterogeneity"] = {"H": round(Hg, 2), "p": round(float(pg), 4)}
# low-access classes vs rest
d["low_access_cls"] = d.GreenType_code.isin([1, 5])
a_, b_ = d[d.low_access_cls].gap, d[~d.low_access_cls].gap
U, pu = stats.mannwhitneyu(a_, b_)
R["gap_forest_scrub_vs_rest"] = {"n": [len(a_), len(b_)], "mean": [round(a_.mean(), 1), round(b_.mean(), 1)],
                                 "p": round(float(pu), 4)}

# ---- robustness regression (OLS, HC3) --------------------------------------
m = smf.ols("GSPI ~ C(Age_code)+C(Gender_code)+C(Education_code)+C(Occupation_code)"
            "+C(Residence_code)+C(GreenType_code)", d).fit(cov_type="HC3")
pv = m.pvalues.drop("Intercept")
R["ols"] = {"R2": round(m.rsquared, 3), "adjR2": round(m.rsquared_adj, 3),
            "n_sig_raw": int((pv < .05).sum()), "n_sig_holm": int((multipletests(pv, method="holm")[1] < .05).sum()),
            "terms_raw_sig": {k: {"b": round(float(m.params[k]), 3), "p": round(float(pv[k]), 4)} for k in pv.index[pv < .05]}}

# ---- sensitivity: governance index without Q31 (threat awareness) and Q34/Q35 (support items)
core = [f"Q{i}_code" for i in (30, 32, 33)]
d["Gov_core"] = d[core].mean(axis=1)
Hs, ps = stats.kruskal(*[x["Gov_core"].values for _, x in d.groupby("Residence_code")])
R["sens_gov_core"] = {"alpha": round(alpha(d[core]), 3), "mean100": round(float(to100(d.Gov_core).mean()), 1),
                      "residence_H": round(Hs, 2), "residence_p": float(ps),
                      "residence_eps2": round((Hs - 3) / (N - 4), 3)}
# sensitivity: gap excluding items Q22/Q23 not applicable -> ENV vs SOIL unchanged; item-matched check: Q17 vs Q24?
# ---- data quality ----------------------------------------------------------
L = d[allq]
R["quality"] = {"missing": int(L.isna().sum().sum()), "straightliners": int((L.nunique(axis=1) == 1).sum()),
                "duplicate_rows": int(L.duplicated().sum()),
                "response_pct": {str(k): round(v * 100, 1) for k, v in L.stack().value_counts(normalize=True).sort_index().items()}}

# ===== FIGURES ==============================================================
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#555", "axes.linewidth": .8})
INK, BLUE, ORANGE, GREY = "#222", "#1f5a89", "#d9822b", "#9a9a9a"

# Fig 1 index bars with CI
fig, ax = plt.subplots(figsize=(6.2, 3.1))
o = idx.iloc[:5][::-1]
ax.barh(o["index"], o.mean100, color=BLUE, height=.55)
ax.errorbar(o.mean100, range(5), xerr=[o.mean100 - o.ci_lo, o.ci_hi - o.mean100], fmt="none", ecolor=INK, capsize=3, lw=1)
for i, v in enumerate(o.mean100):
    ax.text(o.ci_hi.iloc[i] + 1.2, i, f"{v:.1f}", va="center", fontsize=8.5, color=INK)
ax.axvline(idx.mean100.iloc[5], color=ORANGE, ls="--", lw=1.2)
ax.text(idx.mean100.iloc[5] + .4, 4.45, f"GSPI {idx.mean100.iloc[5]:.1f}", color=ORANGE, fontsize=8.5)
ax.set_xlim(0, 100); ax.set_xlabel("Index score (0-100), mean with 95% bootstrap CI")
fig.tight_layout(); fig.savefig(FIG / "fig1_indexes.png", dpi=300); plt.close(fig)

# Fig 2 heatmap class x dimension
fig, ax = plt.subplots(figsize=(6.6, 3.4))
M = prof[dn].to_numpy()
im = ax.imshow(M, cmap="Blues", vmin=45, vmax=85, aspect="auto")
ax.set_xticks(range(5)); ax.set_xticklabels([SHORT[k] for k in dn])
ax.set_yticks(range(7)); ax.set_yticklabels([f"{c} (n={n})" for c, n in zip(prof.index, prof.n)])
for i in range(7):
    for j in range(5):
        ax.text(j, i, f"{M[i, j]:.0f}", ha="center", va="center", fontsize=8.5,
                color="white" if M[i, j] > 68 else INK)
for s in ax.spines.values(): s.set_visible(False)
cb = fig.colorbar(im, ax=ax, pad=.02); cb.set_label("Index (0-100)"); cb.outline.set_visible(False)
fig.tight_layout(); fig.savefig(FIG / "fig2_class_heatmap.png", dpi=300); plt.close(fig)

# Fig 3 gap by class
fig, ax = plt.subplots(figsize=(6.2, 3.3))
g2 = gp.sort_values("gap")
ax.errorbar(g2.gap, range(7), xerr=[g2.gap - g2.lo, g2.hi - g2.gap], fmt="o", color=BLUE, ecolor=BLUE, capsize=3, ms=6)
ax.axvline(0, color=GREY, lw=1)
ax.axvline(R["gap_overall"]["mean"], color=ORANGE, ls="--", lw=1.2)
ax.set_yticks(range(7)); ax.set_yticklabels([f"{c} (n={n})" for c, n in zip(g2["class"], g2.n)])
ax.set_xlabel("Gap: environmental perception minus soil/ecological function (index points)")
ax.text(R["gap_overall"]["mean"] + .3, 6.45, f"all classes {R['gap_overall']['mean']:.1f}", color=ORANGE, fontsize=8.5)
fig.tight_layout(); fig.savefig(FIG / "fig3_gap_by_class.png", dpi=300); plt.close(fig)

# Fig 4 effect sizes
fig, ax = plt.subplots(figsize=(6.2, 3.8))
k2 = kw[kw.outcome != "GSPI"].copy()
for i, (gname, grp) in enumerate(k2.groupby("factor", sort=False)):
    for _, r_ in grp.iterrows():
        col = BLUE if r_.sig_holm else (ORANGE if r_.sig_raw else GREY)
        ax.scatter(r_.eps2, i, s=46 if r_.sig_holm else 30, color=col, zorder=3,
                   marker="o" if r_.sig_holm else ("D" if r_.sig_raw else "o"), edgecolor="white", lw=.6)
ax.set_yticks(range(6)); ax.set_yticklabels(list(GROUPS))
ax.axvline(0, color=GREY, lw=.8); ax.set_xlabel("Epsilon-squared (Kruskal-Wallis), five dimension indexes")
ax.invert_yaxis()
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", color=BLUE, label="Significant after Holm"),
                   Line2D([], [], marker="D", ls="", color=ORANGE, label="Nominal only (p < .05)"),
                   Line2D([], [], marker="o", ls="", color=GREY, label="Not significant")],
          frameon=False, loc="lower right", fontsize=8)
fig.tight_layout(); fig.savefig(FIG / "fig4_effect_sizes.png", dpi=300); plt.close(fig)

# Fig 5 residence x governance
fig, ax = plt.subplots(figsize=(4.6, 3.0))
means, los, his = [], [], []
for k in sorted(d.Residence_code.unique()):
    x = to100(d[d.Residence_code == k]["Governance & management"])
    lo, hi = boot_ci(x); means.append(x.mean()); los.append(lo); his.append(hi)
lab = ["<1 yr\n(n=15)", "1-5 yr\n(n=42)", "6-10 yr\n(n=84)", ">10 yr\n(n=159)"]
ax.errorbar(range(4), means, yerr=[np.array(means) - los, np.array(his) - means], fmt="o-", color=BLUE, capsize=3, ms=6, lw=1.4)
ax.axhline(to100(d["Governance & management"]).mean(), color=GREY, ls="--", lw=1)
ax.set_xticks(range(4)); ax.set_xticklabels(lab); ax.set_ylabel("Governance index (0-100)")
ax.set_ylim(35, 80)
fig.tight_layout(); fig.savefig(FIG / "fig5_residence_governance.png", dpi=300); plt.close(fig)

# Fig S1 scree + parallel
fig, ax = plt.subplots(figsize=(4.8, 3))
ax.plot(range(1, 13), ev[:12], "o-", color=BLUE, label="Observed")
ax.plot(range(1, 13), pa[:12], "s--", color=ORANGE, label="Parallel analysis (95th pct)")
ax.set_xlabel("Component"); ax.set_ylabel("Eigenvalue"); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(FIG / "figS1_scree.png", dpi=300); plt.close(fig)

json.dump(R, open(OUT / "results.json", "w"), indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
print(json.dumps({k: R[k] for k in ["cfa", "cfa_single_factor", "cfa_delta_chi2", "kmo", "n_factors_parallel", "harman_first_pct",
                                    "n_sig_holm", "n_sig_raw", "gap_overall", "gap_heterogeneity", "gap_forest_scrub_vs_rest",
                                    "ols", "eigenvalues", "parallel_95", "fornell_larcker_ok", "max_latent_corr", "efa_var_explained_pct",
                                    "efa_crossloadings_ge_0.40"]}, indent=1, default=str))
