import pandas as pd, numpy as np, json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
plt.rcParams.update({'mathtext.fontset':'custom','mathtext.rm':'Liberation Serif','mathtext.it':'Liberation Serif:italic','font.family':'Liberation Serif','font.size':10,'axes.edgecolor':'#52514e','axes.linewidth':0.8,
    'xtick.color':'#0b0b0b','ytick.color':'#0b0b0b','text.color':'#0b0b0b','axes.labelcolor':'#0b0b0b',
    'savefig.dpi':600,'figure.facecolor':'white','axes.facecolor':'white','legend.frameon':False})
BLUE,ORANGE,AQUA,YELLOW,MAG='#2a78d6','#eb6834','#1baf7a','#eda100','#e87ba4'
GRAY='#52514e'; GRID='#e1e0d9'
SAL=['#86b6ef','#3987e5','#1c5cab','#0d366b']
df=pd.read_csv('data_long.csv')
def P(exp,trait,col='mean'):
    d=df[(df.exp==exp)&(df.trait==trait)]
    return d.pivot(index='inoc',columns='sal',values=col)
ISO=['Control','IS-01','IS-02','IS-03','IS-04','IS-05','IS-06']
CON=['Control','C1-3','C1-5','C2-3','C2-5','C4-5']
S=[0,50,100,150]
# ---------- derived traits ----------
der={}
for exp,order in [('iso',ISO),('con',CON)]:
    G=P(exp,'germ_n')/P(exp,'seeds')*100
    R=P(exp,'root_cm'); Sh=P(exp,'shoot_cm')
    der[exp]=dict(germ=G.loc[order,S],root=R.loc[order,S],shoot=Sh.loc[order,S],
        svi=(G*(R+Sh)).loc[order,S],chla=P(exp,'chla').loc[order,S],chlb=P(exp,'chlb').loc[order,S],
        totchl=(P(exp,'chla')+P(exp,'chlb')).loc[order,S],car=P(exp,'car').loc[order,S],
        protein=P(exp,'protein').loc[order,S],sugar=P(exp,'sugar').loc[order,S],dpph=P(exp,'dpph').loc[order,S])
der['con']['phenol']=P('con','phenol').loc[CON,S]
# lab SVI recomputed
lab={}
for exp,order in [('lab_iso',ISO),('lab_con',CON)]:
    g=df[(df.exp==exp)]
    t=g.pivot(index='inoc',columns='trait',values='mean').loc[order]
    sd=g.pivot(index='inoc',columns='trait',values='sd').loc[order]
    t['G']=t.germ_n/t.seeds*100; t['SVI']=t.G*(t.root_mm+t.shoot_mm)/10
    t['root_sd']=sd.root_mm; t['shoot_sd']=sd.shoot_mm
    lab[exp]=t
pd.concat(lab).to_csv('lab_table.csv')
# ---------- indices ----------
TR=['germ','root','shoot','svi','chla','car','protein','sugar','dpph']
TRL={'germ':'Germination','root':'Root length','shoot':'Shoot length','svi':'Vigour index','chla':'Chl a','car':'Carotenoids',
     'protein':'Soluble protein','sugar':'Soluble sugars','dpph':'DPPH scavenging'}
# mitigation % vs salinity-matched uninoculated control
mit=[]
for exp in ['iso','con']:
    for tr in TR:
        M=der[exp][tr]
        for inoc in M.index[1:]:
            for s in [50,100,150]:
                c=M.loc['Control',s]; mit.append(dict(inoc=inoc,sal=s,trait=tr,mit=(M.loc[inoc,s]-c)/c*100))
mit=pd.DataFrame(mit); mit.to_csv('mitigation.csv',index=False)
sir={tr:{s:float((der['iso'][tr].loc['Control',0]-der['iso'][tr].loc['Control',s])/der['iso'][tr].loc['Control',0]*100) for s in [50,100,150]} for tr in TR}
sir['phenol']={s:float((20.56-v)/20.56*100) for s,v in zip([50,100,150],[9.50,7.27,6.15])}
# retention (salt tolerance index) at 150 mM relative to own 0 mM
sti={}
for exp in ['iso','con']:
    for tr in TR:
        M=der[exp][tr]; sti.setdefault(tr,{})
        for inoc in M.index: sti[tr][inoc]=float(M.loc[inoc,150]/M.loc[inoc,0]*100)
# combined matrix (48 treatment combinations, controls once)
rows=[]
for exp,order in [('iso',ISO),('con',CON[1:])]:
    for inoc in order:
        for s in S:
            rows.append(dict(inoc=inoc,sal=s,grp='Uninoculated' if inoc=='Control' else ('Single isolate' if exp=='iso' else 'Consortium'),
                             **{tr:der[exp][tr].loc[inoc,s] for tr in TR}))
X=pd.DataFrame(rows)
mm=(X[TR]-X[TR].min())/(X[TR].max()-X[TR].min())
X['CMI']=mm.mean(1)
X.to_csv('matrix.csv',index=False)
# PCA
Z=(X[TR]-X[TR].mean())/X[TR].std(ddof=1)
U,sv,Vt=np.linalg.svd(Z.values,full_matrices=False)
ev=sv**2/(len(Z)-1); expl=ev/ev.sum()
scores=U*sv; load=Vt.T*np.sqrt(ev)
# sign convention: PC1 positive = better performance (protein loading positive)
if load[TR.index('protein'),0]<0: scores[:,0]*=-1; load[:,0]*=-1
if load[TR.index('dpph'),1]<0: scores[:,1]*=-1; load[:,1]*=-1
X['PC1']=scores[:,0]; X['PC2']=scores[:,1]
corr=X[TR].corr()
res=dict(sir=sir,sti=sti,pca=dict(expl=expl[:4].tolist(),eig=ev[:4].tolist(),load={tr:load[i,:2].tolist() for i,tr in enumerate(TR)}),
         cmi150=X[X.sal==150].sort_values('CMI',ascending=False)[['inoc','CMI']].values.tolist(),
         cmi_all=X.groupby('inoc').CMI.mean().sort_values(ascending=False).to_dict(),
         corr=corr.round(3).to_dict(),
         mit150=mit[mit.sal==150].pivot(index='inoc',columns='trait',values='mit').round(1).to_dict())
json.dump(res,open('indices.json','w'),indent=1)
json.dump({e:{k:v.round(3).to_dict() for k,v in der[e].items()} for e in der},open('derived.json','w'),indent=1,default=str)
print('PCA expl',np.round(expl[:4],3),'eig',np.round(ev[:4],2))
print('loadings',{tr:np.round(load[i,:2],2).tolist() for i,tr in enumerate(TR)})
print('CMI150',[(a,round(b,3)) for a,b in res['cmi150']])
print('SIR',{k:{s:round(v,1) for s,v in d.items()} for k,d in sir.items()})

def save(fig,name):
    fig.savefig(name+'.png',bbox_inches='tight',dpi=600); plt.close(fig)

# ---------- FIGURE 1: methodology infographic ----------
fig,ax=plt.subplots(figsize=(7.2,9.6)); ax.set_xlim(0,100); ax.set_ylim(0,130); ax.axis('off')
def box(x,y,w,h,title,lines,fc,ec,num=None,tsize=10.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.4,rounding_size=2.2',fc=fc,ec=ec,lw=1.2))
    ax.add_patch(FancyBboxPatch((x,y+h-6.2),w,6.2,boxstyle='round,pad=0.4,rounding_size=2.2',fc=ec,ec=ec,lw=1.2))
    ax.text(x+w/2+(2.5 if num and len(num)>1 else 0),y+h-3.1,title,ha='center',va='center',fontsize=tsize,fontweight='bold',color='white')
    if num: 
        ax.add_patch(plt.Circle((x+1.5,y+h-3.1),2.6,fc='white',ec=ec,lw=1.2,zorder=5))
        ax.text(x+1.5,y+h-3.1,num,ha='center',va='center',fontsize=10,fontweight='bold',color=ec,zorder=6)
    for i,l in enumerate(lines):
        ax.text(x+2.2,y+h-9.6-i*3.55,l,ha='left',va='center',fontsize=8.6)
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=14,lw=1.6,color=GRAY))
C1,C2,C3,C4,C5='#1c5cab','#b24a1e','#0f7a55','#8a6100','#4a3aa7'
T1,T2,T3,T4,T5='#eef4fc','#fdf0ea','#e9f7f1','#fdf5e3','#efedfa'
box(4,108,92,20,'STAGE 1  |  Endophyte inoculum and consortium preparation',
    ['Six rice endophytes (IS-01 to IS-06) grown separately in nutrient broth to exponential phase',
     'Five dual-strain consortia (C1-3, C1-5, C2-3, C2-5, C4-5) mixed 1:1 (v/v) and vortexed',
     'Purity and compatibility checked by quadrant streaking on nutrient agar (37 ± 1 °C, 12-24 h)'],T1,C1,'1')
arrow(50,107,50,103.5)
box(4,86,92,16.5,'STAGE 2  |  Seed preparation and bacterization (rice cv. IR-64)',
    ['Surface sterilization: 95% ethanol (30-60 s) then 5% NaOCl (5-10 min); 2-3 sterile water rinses',
     'Seeds soaked 30 min in bacterial suspension (about 10$^{8}$ CFU mL$^{-1}$); uninoculated seeds as control'],T2,C2,'2')
arrow(28,85,28,80.5); arrow(72,85,72,80.5)
box(4,55,44,25,'Laboratory assay',
    ['Petri plates, Whatman No. 1 paper',
     '25 seeds per treatment, 25 ± 2 °C',
     'Isolates and consortia, 0 mM NaCl',
     'Germination (radicle ≥ 2 mm)',
     'Root and shoot length, vigour index'],T3,C3,'3A')
box(52,55,44,25,'Polyhouse pot trial',
    ['Soil : cocopeat 1:2 (w/w), 2.5 kg pot$^{-1}$',
     'NaCl 0, 50, 100, 150 mM from 15 DAS',
     '500 mL on alternate days for 30 days',
     'CRD, three replicates; 30 seeds',
     'Harvest at 45 DAS'],T3,C3,'3B')
arrow(72,54,72,50.5)
ax.text(26,52.3,'germination data → Stage 5',ha='center',fontsize=8,style='italic',color='#3a3935')
box(4,27,92,23,'STAGE 4  |  Leaf physiological and biochemical assays (0.5 g fresh leaf)',[],T4,C4,'4')
assays=[('Chlorophyll a, b\n& carotenoids','DMSO, 60 °C\nA$_{663}$ / A$_{645}$'),('Total phenolics','Folin-Ciocalteu\nA765, gallic acid'),
        ('Soluble protein','Lowry method\nA660, BSA'),('Soluble sugars','Anthrone\nA620, glucose'),('DPPH assay','0.1 mM DPPH\nA517, ascorbate')]
for i,(a,b) in enumerate(assays):
    x=6.2+i*17.8
    ax.add_patch(FancyBboxPatch((x,29.5),15.6,13.2,boxstyle='round,pad=0.3,rounding_size=1.5',fc='white',ec=C4,lw=1))
    ax.text(x+7.8,39.3,a,ha='center',va='center',fontsize=8.2,fontweight='bold')
    ax.text(x+7.8,33.0,b,ha='center',va='center',fontsize=7.6,color='#3a3935')
arrow(50,26,50,22.5)
box(4,1,92,21.5,'STAGE 5  |  Statistical analysis and indices',
    ['Germination: χ² test (laboratory); binomial GLM with likelihood-ratio tests (polyhouse)',
     'Continuous traits: two-way ANOVA (inoculant × NaCl) from replicate means and SDs; Tukey HSD',
     'Indices: salinity-induced reduction, inoculation-mediated mitigation, retention index, CMI',
     'Multivariate: Pearson correlation and principal component analysis of nine standardized traits'],T5,C5,'5')
save(fig,'Fig1_workflow')

# ---------- FIGURE 2: grouped bars, germination ----------
fig,axs=plt.subplots(2,1,figsize=(7.2,6.4),sharey=True)
for ax,exp,order,lab_ in [(axs[0],'iso',ISO,'(a) Single isolates'),(axs[1],'con',CON,'(b) Dual-strain consortia')]:
    G=der[exp]['germ']; x=np.arange(len(order)); w=0.2
    for j,s in enumerate(S):
        ax.bar(x+(j-1.5)*w,G[s].values,w*0.9,color=SAL[j],label=f'{s} mM NaCl',zorder=3)
    ax.set_xticks(x); ax.set_xticklabels(['Uninoculated' if o=='Control' else o for o in order])
    ax.set_ylabel('Germination (%)'); ax.set_ylim(0,100); ax.yaxis.grid(True,color=GRID,lw=0.6,zorder=0)
    ax.spines[['top','right']].set_visible(False); ax.text(-0.6,103,lab_,fontsize=10.5,fontweight='bold',ha='left')
axs[0].legend(ncol=4,loc='upper center',bbox_to_anchor=(0.5,1.25),fontsize=9)
fig.tight_layout(); save(fig,'Fig2_germination')

# ---------- FIGURE 3: dose-response lines ----------
series=[('iso','Control','Uninoculated',GRAY,'o','-'),('iso','IS-06','IS-06',BLUE,'s','-'),('iso','IS-05','IS-05',ORANGE,'^','-'),
        ('con','C4-5','C4-5',AQUA,'D','--'),('con','C2-5','C2-5',YELLOW,'v','--')]
panels=[('chla','Chlorophyll a (mg g$^{-1}$ FW)'),('protein','Soluble protein (µg mL$^{-1}$)'),
        ('sugar','Soluble sugars (µg mL$^{-1}$)'),('root','Root length (cm)')]
fig,axs=plt.subplots(2,2,figsize=(7.2,6.2))
for k,(ax,(tr,yl)) in enumerate(zip(axs.flat,panels)):
    for exp,inoc,lab_,c,mk,ls in series:
        y=der[exp][tr].loc[inoc,S].values
        sdname={'chla':'chla','protein':'protein','sugar':'sugar','root':'root_cm'}[tr]
        e=P(exp,sdname,'sd').loc[inoc,S].values if tr!='sugar' or exp=='iso' else None
        ax.errorbar(S,y,yerr=e,color=c,marker=mk,ms=5.5,lw=1.6,ls=ls,capsize=2.5,mec='white',mew=0.6,label=lab_)
        if k==0: pass
    ax.set_xticks(S); ax.set_xlabel('NaCl (mM)'); ax.set_ylabel(yl)
    ax.yaxis.grid(True,color=GRID,lw=0.6); ax.spines[['top','right']].set_visible(False)
    ax.text(0.02,1.04,'(%s)'%'abcd'[k],transform=ax.transAxes,fontsize=10.5,fontweight='bold')
h,l=axs[0,0].get_legend_handles_labels()
fig.legend(h,l,ncol=5,loc='upper center',bbox_to_anchor=(0.5,1.03),fontsize=9)
fig.tight_layout(rect=(0,0,1,0.96)); save(fig,'Fig3_doseresponse')

# ---------- FIGURE 4: heatmap of mitigation ----------
ORD=['IS-01','IS-02','IS-03','IS-04','IS-05','IS-06','C1-3','C1-5','C2-3','C2-5','C4-5']
TRH=['germ','root','shoot','chla','car','protein','sugar','dpph']
cols=[(s,t) for s in [50,100,150] for t in TRH]
M=np.array([[mit[(mit.inoc==i)&(mit.sal==s)&(mit.trait==t)].mit.values[0] for s,t in cols] for i in ORD])
cmap=LinearSegmentedColormap.from_list('div',['#9c2a2a','#e34948','#f0efec','#3987e5','#0d366b'])
fig,ax=plt.subplots(figsize=(7.4,4.4))
norm=TwoSlopeNorm(vmin=-100,vcenter=0,vmax=300)
im=ax.imshow(np.clip(M,-100,300),cmap=cmap,norm=norm,aspect='auto')
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        v=M[i,j]; ax.text(j,i,f'{v:.0f}',ha='center',va='center',fontsize=5.6,color='white' if (v>150 or v<-60) else '#0b0b0b')
short={'germ':'Germ.','root':'Root','shoot':'Shoot','chla':'Chl a','car':'Car.','protein':'Protein','sugar':'Sugar','dpph':'DPPH'}
ax.set_xticks(range(len(cols))); ax.set_xticklabels([short[t] for s,t in cols],rotation=90,fontsize=7.5)
ax.set_yticks(range(len(ORD))); ax.set_yticklabels(ORD,fontsize=8.5)
for k,s in enumerate([50,100,150]):
    ax.text(k*8+3.5,-1.3,f'{s} mM NaCl',ha='center',fontsize=9,fontweight='bold')
    if k: ax.axvline(k*8-0.5,color='white',lw=2.5)
ax.axhline(5.5,color='white',lw=2.5)
ax.set_xticks(np.arange(-.5,len(cols),1),minor=True); ax.set_yticks(np.arange(-.5,len(ORD),1),minor=True)
ax.grid(which='minor',color='white',lw=0.6); ax.tick_params(which='minor',length=0)
for sp in ax.spines.values(): sp.set_visible(False)
cb=fig.colorbar(im,ax=ax,fraction=0.03,pad=0.02); cb.set_label('Change vs. salinity-matched uninoculated control (%)',fontsize=8.5)
cb.ax.tick_params(labelsize=7.5)
save(fig,'Fig4_heatmap')

# ---------- FIGURE 5: radar at 150 mM ----------
Xn=X.copy(); 
for tr in TR: Xn[tr]=(X[tr]-X[tr].min())/(X[tr].max()-X[tr].min())
def rowv(inoc,s): return Xn[(Xn.inoc==inoc)&(Xn.sal==s)][TR].values[0]
rad=[('Uninoculated, 0 mM',rowv('Control',0),'#898781','-'),('Uninoculated, 150 mM',rowv('Control',150),GRAY,'--'),
     ('IS-06, 150 mM',rowv('IS-06',150),BLUE,'-'),('C4-5, 150 mM',rowv('C4-5',150),ORANGE,'-')]
ang=np.linspace(0,2*np.pi,len(TR),endpoint=False).tolist(); ang+=ang[:1]
fig=plt.figure(figsize=(6.2,5.6)); ax=fig.add_subplot(111,polar=True)
for lab_,v,c,ls in rad:
    vv=v.tolist()+[v[0]]; ax.plot(ang,vv,color=c,lw=1.8,ls=ls,marker='o',ms=4,label=lab_); ax.fill(ang,vv,color=c,alpha=0.07)
ax.set_xticks(ang[:-1]); ax.set_xticklabels([TRL[t] for t in TR],fontsize=9)
ax.set_rlabel_position(100); ax.tick_params(axis='x',pad=10); ax.set_ylim(0,1); ax.set_yticks([0.25,0.5,0.75,1]); ax.set_yticklabels(['0.25','0.50','0.75','1.00'],fontsize=7,color='#52514e')
ax.grid(color=GRID,lw=0.7); ax.spines['polar'].set_color('#c3c2b7')
ax.legend(loc='upper center',bbox_to_anchor=(0.5,-0.07),ncol=2,fontsize=9)
save(fig,'Fig5_radar')

# ---------- FIGURE 6: PCA biplot ----------
fig,ax=plt.subplots(figsize=(7.0,5.8))
gc={'Uninoculated':(GRAY,'o'),'Single isolate':(BLUE,'s'),'Consortium':(ORANGE,'^')}
sz={0:28,50:44,100:62,150:84}
for g,(c,mk) in gc.items():
    d=X[X.grp==g]
    ax.scatter(d.PC1,d.PC2,s=[sz[s] for s in d.sal],c=c,marker=mk,edgecolor='white',lw=0.8,label=g,zorder=3)
for _,r in X.iterrows():
    if r.inoc in ('IS-06','C4-5','Control') :
        dy=-9 if (r.inoc=='Control' and r.sal==0) else (-12 if (r.inoc=='C4-5' and r.sal==0) else 3)
        ax.annotate(f"{'Unin.' if r.inoc=='Control' else r.inoc}-{r.sal}",(r.PC1,r.PC2),xytext=(4,dy),textcoords='offset points',fontsize=7,color='#3a3935')
sc=3.2
for i,tr in enumerate(TR):
    ax.annotate('',xy=(load[i,0]*sc,load[i,1]*sc),xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color='#0b0b0b',lw=0.9))
    tx,ty=load[i,0]*sc,load[i,1]*sc
    spec={'dpph':(-0.08,0.12,'right'),'root':(0.08,0.10,'left'),'shoot':(0.10,-0.08,'left'),'sugar':(0.10,0.10,'left'),
          'protein':(0.10,-0.14,'left'),'car':(0.10,0.0,'left'),'germ':(0.10,-0.05,'left'),'svi':(0.10,0.05,'left'),'chla':(0.10,0.0,'left')}[tr]
    ax.text(tx+spec[0],ty+spec[1],TRL[tr],fontsize=7.8,ha=spec[2],va='center',
            bbox=dict(fc='white',ec='none',alpha=0.8,pad=0.4))
ax.axhline(0,color='#c3c2b7',lw=0.7,zorder=0); ax.axvline(0,color='#c3c2b7',lw=0.7,zorder=0)
ax.set_xlabel(f'PC1 ({expl[0]*100:.1f}% of variance)'); ax.set_ylabel(f'PC2 ({expl[1]*100:.1f}% of variance)')
ax.spines[['top','right']].set_visible(False)
l1=ax.legend(loc='upper left',fontsize=8.5,title='Inoculation',title_fontsize=8.5)
from matplotlib.lines import Line2D
hs=[Line2D([],[],marker='o',ls='',color='#898781',ms=np.sqrt(sz[s])*0.9,mec='white') for s in S]
ax.add_artist(l1); ax.legend(hs,[f'{s} mM' for s in S],loc='lower left',fontsize=8,title='NaCl',title_fontsize=8.5)
save(fig,'Fig6_pca')
print('figures done')
