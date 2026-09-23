import pandas as pd, numpy as np, json
from scipy import stats
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.libqsturng import qsturng
df=pd.read_csv('data_long.csv')
out={}
def cell(exp,trait):
    d=df[(df.exp==exp)&(df.trait==trait)].copy()
    return d
# ---------- lab germination chi-square ----------
for exp in ['lab_iso','lab_con']:
    g=df[(df.exp==exp)&(df.trait=='germ_n')].set_index('inoc')['mean']
    n=df[(df.exp==exp)&(df.trait=='seeds')].set_index('inoc')['mean']
    tab=np.vstack([g.values,(n-g).values])
    chi,p,dof,_=stats.chi2_contingency(tab)
    out[f'{exp}_chi2']=dict(chi2=round(chi,2),df=int(dof),p=float(p))
    # Fisher best vs control
    best=g.drop('Control').idxmax()
    o,pf=stats.fisher_exact([[g[best],n[best]-g[best]],[g['Control'],n['Control']-g['Control']]])
    out[f'{exp}_fisher_best']=dict(best=best,p=float(pf))
# ---------- polyhouse germination binomial GLM ----------
for exp in ['iso','con']:
    g=cell(exp,'germ_n').rename(columns={'mean':'g'}); n=cell(exp,'seeds').rename(columns={'mean':'n'})
    d=g[['inoc','sal','g']].merge(n[['inoc','sal','n']])
    d['f']=d.g/d.n; d['S']=d.sal.astype(str)
    m0=smf.glm('f~C(inoc)',d,family=sm.families.Binomial(),var_weights=d.n).fit()
    m1=smf.glm('f~C(inoc)+C(S)',d,family=sm.families.Binomial(),var_weights=d.n).fit()
    mS=smf.glm('f~C(S)',d,family=sm.families.Binomial(),var_weights=d.n).fit()
    lr_sal=m0.deviance-m1.deviance; df_sal=m0.df_resid-m1.df_resid
    lr_inoc=mS.deviance-m1.deviance; df_inoc=mS.df_resid-m1.df_resid
    lr_int=m1.deviance; df_int=m1.df_resid
    out[f'{exp}_germ_glm']=dict(
        sal=dict(LR=round(lr_sal,2),df=int(df_sal),p=float(stats.chi2.sf(lr_sal,df_sal))),
        inoc=dict(LR=round(lr_inoc,2),df=int(df_inoc),p=float(stats.chi2.sf(lr_inoc,df_inoc))),
        inter=dict(LR=round(lr_int,2),df=int(df_int),p=float(stats.chi2.sf(lr_int,df_int))))
# ---------- two-way ANOVA from summary statistics (balanced, n=3) ----------
def anova_summary(exp,trait,n=3):
    d=cell(exp,trait).dropna(subset=['sd'])
    A=sorted(d.inoc.unique()); B=sorted(d.sal.unique())
    if len(d)==0 or len(d)!=len(A)*len(B): return None
    M=d.pivot(index='inoc',columns='sal',values='mean').loc[A,B].values
    S=d.pivot(index='inoc',columns='sal',values='sd').loc[A,B].values
    a,b=M.shape; gm=M.mean()
    ssA=n*b*((M.mean(1)-gm)**2).sum(); ssB=n*a*((M.mean(0)-gm)**2).sum()
    ssC=n*((M-gm)**2).sum(); ssAB=ssC-ssA-ssB
    ssE=((n-1)*S**2).sum(); dfE=a*b*(n-1)
    msE=ssE/dfE
    res={}
    for k,ss,dff in [('inoc',ssA,a-1),('sal',ssB,b-1),('inter',ssAB,(a-1)*(b-1))]:
        F=(ss/dff)/msE; p=stats.f.sf(F,dff,dfE)
        res[k]=dict(F=float(F),df=f'{dff},{dfE}',p=float(p),pe2=float(ss/(ss+ssE)))
    q=qsturng(0.95,a*b,dfE); res['HSD']=float(q*np.sqrt(msE/n)); res['MSE']=float(msE)
    return res
for exp in ['iso','con']:
    for trait in ['root_cm','shoot_cm','chla','chlb','protein','sugar','phenol','dpph']:
        r=anova_summary(exp,trait)
        if r: out[f'{exp}_{trait}_anova']=r
json.dump(out,open('stats.json','w'),indent=1)
for k,v in out.items():
    if 'anova' in k:
        print(k, {kk:(round(vv['F'],1),vv['df'],'%.1e'%vv['p'],round(vv['pe2'],3)) for kk,vv in v.items() if isinstance(vv,dict)}, 'HSD',round(v['HSD'],3))
    else: print(k,v)
