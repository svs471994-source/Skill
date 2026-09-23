import re, json, pandas as pd
L=open('../src/report.txt').read().split('\n')
tables={};cur=None
for l in L:
    m=re.match(r'<<TABLE (\d+)>>',l)
    if m: cur=int(m.group(1)); tables[cur]=[]; continue
    if l.startswith('<<END'): cur=None; continue
    if cur: tables[cur].append([c.strip() for c in l.split('|')])
def ms(s):
    s=s.replace('SD','').strip()
    p=[x.strip() for x in s.split('±')]
    m=float(p[0]); sd=float(p[1]) if len(p)>1 and p[1] else None
    return m,sd
def tr(name):
    name=name.strip()
    sal=0; inoc='Control'
    m=re.match(r'^(IS-0\d|C\d-\d)\s*\+\s*(\d+) mM$',name)
    if m: return m.group(1),int(m.group(2))
    m=re.match(r'^(\d+) mM$',name)
    if m: return 'Control',int(m.group(1))
    return name,0
rows=[]
def add(exp,tab,cols,start=1):
    hdr=tables[tab][0]
    for r in tables[tab][1:]:
        inoc,sal=tr(r[0])
        for ci,trait in cols.items():
            m,sd=ms(r[ci]); rows.append(dict(exp=exp,inoc=inoc,sal=sal,trait=trait,mean=m,sd=sd))
# lab germination
for t,exp in [(1,'lab_iso'),(2,'lab_con')]:
    for r in tables[t][1:]:
        rows+= [dict(exp=exp,inoc=r[0],sal=0,trait='germ_n',mean=float(r[1]),sd=None),
                dict(exp=exp,inoc=r[0],sal=0,trait='seeds',mean=float(r[2]),sd=None)]
        for ci,trait in {4:'root_mm',5:'shoot_mm',6:'SVI_reported'}.items():
            m,sd=ms(r[ci]); rows.append(dict(exp=exp,inoc=r[0],sal=0,trait=trait,mean=m,sd=sd))
for t,exp in [(3,'iso'),(4,'con')]:
    for r in tables[t][1:]:
        inoc,sal=tr(r[0])
        rows+= [dict(exp=exp,inoc=inoc,sal=sal,trait='germ_n',mean=float(r[1]),sd=None),
                dict(exp=exp,inoc=inoc,sal=sal,trait='seeds',mean=float(r[2]),sd=None)]
        for ci,trait in {4:'root_cm',5:'shoot_cm',6:'SVI_reported'}.items():
            m,sd=ms(r[ci]); rows.append(dict(exp=exp,inoc=inoc,sal=sal,trait=trait,mean=m,sd=sd))
add('iso',5,{4:'chla',5:'chlb',6:'totchl_reported',7:'car'})
add('con',6,{4:'chla',5:'chlb',6:'totchl_reported',7:'car'})
add('con',9,{1:'phenol'})
add('iso',11,{1:'protein'}); add('con',12,{1:'protein'})
add('iso',14,{1:'sugar'}); add('con',15,{1:'sugar'})
add('iso',17,{2:'dpph'}); add('con',18,{2:'dpph'})
# isolate phenolics: only values stated in text of section 3.5.2 (Table 8 in report duplicates Table 9)
for inoc,sal,v in [('Control',0,20.56),('Control',50,9.50),('Control',100,7.27),('Control',150,6.15),
                   ('IS-06',0,25.26),('IS-06',50,24.03),('IS-06',100,24.03),('IS-06',150,20.67),
                   ('IS-05',50,21.79),('IS-05',100,16.21),('IS-05',150,15.09),('IS-01',0,11.74),('IS-01',150,2.80)]:
    rows.append(dict(exp='iso',inoc=inoc,sal=sal,trait='phenol',mean=v,sd=None))
df=pd.DataFrame(rows)
df.to_csv('data_long.csv',index=False)
print(df.groupby(['exp','trait']).size())
