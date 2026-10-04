"""Additional discriminant-validity evidence: HTMT, nested CFA comparisons, second-order model."""
import json, sys
import numpy as np, pandas as pd
from scipy.optimize import minimize
from scipy import stats
d = pd.read_excel(sys.argv[1])
DIMS = {"USE": range(7, 12), "ENV": range(12, 18), "VEG": range(18, 24), "SOIL": range(24, 30), "GOV": range(30, 36)}
cols = [f"Q{i}_code" for r in DIMS.values() for i in r]
X = d[cols].to_numpy(float); N = len(X); S = np.cov(X.T); p = S.shape[0]
Rm = np.corrcoef(X.T)
idx = {}; k = 0
for n, r in DIMS.items():
    idx[n] = list(range(k, k + len(r))); k += len(r)
# HTMT (Henseler et al., 2015)
names = list(DIMS); htmt = pd.DataFrame(np.nan, names, names)
for a in names:
    for b in names:
        if a >= b and a != b: pass
        if a == b: continue
        het = np.abs(Rm[np.ix_(idx[a], idx[b])]).mean()
        def mono(n):
            m = np.abs(Rm[np.ix_(idx[n], idx[n])]); return m[np.triu_indices(len(idx[n]), 1)].mean()
        htmt.loc[a, b] = het / np.sqrt(mono(a) * mono(b))
# bootstrap CI for VEG-SOIL HTMT
rng = np.random.default_rng(1); bs = []
for _ in range(2000):
    Xb = X[rng.integers(0, N, N)]; Rb = np.corrcoef(Xb.T)
    het = np.abs(Rb[np.ix_(idx["VEG"], idx["SOIL"])]).mean()
    mv = np.abs(Rb[np.ix_(idx["VEG"], idx["VEG"])])[np.triu_indices(6, 1)].mean()
    ms = np.abs(Rb[np.ix_(idx["SOIL"], idx["SOIL"])])[np.triu_indices(6, 1)].mean()
    bs.append(het / np.sqrt(mv * ms))
def fit(assign, nf, second_order=False):
    fac = np.array(assign)
    nphi = nf * (nf - 1) // 2
    iu = np.triu_indices(nf, 1)
    def sig(t):
        L = np.zeros((p, nf)); L[np.arange(p), fac] = t[:p]
        th = np.exp(t[p:2 * p])
        if second_order:
            g = np.tanh(t[2 * p:2 * p + nf]); Phi = np.outer(g, g); np.fill_diagonal(Phi, 1)
        else:
            Phi = np.eye(nf); Phi[iu] = np.tanh(t[2 * p:]); Phi = Phi + Phi.T - np.eye(nf)
        return L @ Phi @ L.T + np.diag(th), Phi
    def f(t):
        Sg = sig(t)[0]; s, ld = np.linalg.slogdet(Sg)
        return 1e6 if s <= 0 else ld + np.trace(S @ np.linalg.inv(Sg)) - np.linalg.slogdet(S)[1] - p
    extra = nf if second_order else nphi
    t0 = np.concatenate([np.full(p, .7), np.log(np.full(p, .5)), np.full(extra, .6)])
    r = minimize(f, t0, method="L-BFGS-B", options={"maxiter": 8000, "maxfun": 300000})
    q = 2 * p + extra; df = p * (p + 1) // 2 - q; chi = (N - 1) * r.fun
    Fb = np.sum(np.log(np.diag(S))) - np.linalg.slogdet(S)[1]; cb, dfb = (N - 1) * Fb, p * (p - 1) // 2
    cfi = 1 - max(chi - df, 0) / max(cb - dfb, chi - df); rmsea = np.sqrt(max(chi - df, 0) / (df * (N - 1)))
    aic = chi + 2 * q; bic = chi + q * np.log(N)
    return {"chi2": round(chi, 1), "df": df, "CFI": round(cfi, 3), "RMSEA": round(rmsea, 3), "AIC": round(aic, 1), "BIC": round(bic, 1),
            "Phi": np.round(sig(r.x)[1], 2).tolist(), "gamma": (np.round(np.tanh(r.x[2*p:2*p+nf]), 2).tolist() if second_order else None)}
a5 = [0]*5 + [1]*6 + [2]*6 + [3]*6 + [4]*6
a4 = [0]*5 + [1]*6 + [2]*12 + [3]*6            # VEG+SOIL merged
a4b = [0]*5 + [1]*12 + [2]*6 + [3]*6           # ENV+VEG merged
m5, m4, m4b = fit(a5, 5), fit(a4, 4), fit(a4b, 4)
so = fit(a5, 5, second_order=True)
out = {"HTMT": htmt.round(3).to_dict(), "HTMT_max": round(float(np.nanmax(htmt.values)), 3),
       "HTMT_VEG_SOIL_CI95": np.percentile(bs, [2.5, 97.5]).round(3).tolist(),
       "cfa5": {k: v for k, v in m5.items() if k != "Phi"}, "cfa4_VEGSOIL_merged": {k: v for k, v in m4.items() if k != "Phi"},
       "cfa4_ENVVEG_merged": {k: v for k, v in m4b.items() if k != "Phi"},
       "delta_5_vs_4VS": {"chi2": round(m4["chi2"] - m5["chi2"], 1), "df": m4["df"] - m5["df"],
                          "p": float(stats.chi2.sf(m4["chi2"] - m5["chi2"], m4["df"] - m5["df"]))},
       "delta_5_vs_4EV": {"chi2": round(m4b["chi2"] - m5["chi2"], 1), "df": m4b["df"] - m5["df"],
                          "p": float(stats.chi2.sf(m4b["chi2"] - m5["chi2"], m4b["df"] - m5["df"]))},
       "second_order": {k: v for k, v in so.items() if k != "Phi"}}
json.dump(out, open("validity_extra.json", "w"), indent=1)
print(json.dumps(out, indent=1))
