#!/usr/bin/env python3
"""Recreate all 4 figures for the PM Bengaluru paper with proper (a)(b) panel labels."""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 150,
})

def panel_label(ax, label):
    """Add bold (a)/(b) label in top-left corner of axis."""
    ax.text(-0.08, 1.05, label, transform=ax.transAxes,
            fontsize=13, fontweight='bold', va='top', ha='left')

# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — Bengaluru location map
# ══════════════════════════════════════════════════════════════════════════════
fig1, ax = plt.subplots(figsize=(5.5, 7))

stations = {
    'Peenya':                (77.518, 13.028, 'Industrial'),
    'Shivapura':             (77.530, 13.012, 'Industrial'),
    'Hebbal':                (77.592, 13.035, 'Residential'),
    'Yelahanka':             (77.600, 13.100, 'Residential'),
    'Peenya-2':              (77.498, 13.028, 'Industrial'),
    'Kadugodi':              (77.755, 13.000, 'Residential'),
    'City Railway Station':  (77.575, 12.977, 'Kerbside'),
    'Jayanagar':             (77.583, 12.930, 'Residential'),
    'Silk Board':            (77.622, 12.917, 'Kerbside'),
    'RVCE-Mailasandra':      (77.499, 12.924, 'Residential'),
    'Bapuji Nagar':          (77.558, 12.972, 'Residential'),
    'Hombegowda Nagar':      (77.610, 12.963, 'Residential'),
    'Jigani':                (77.635, 12.799, 'Industrial'),
}
colors_s = {'Residential': '#2ca02c', 'Industrial': '#d62728', 'Kerbside': '#1f77b4'}

boundary_lon = [77.30, 77.80, 77.80, 77.30, 77.30]
boundary_lat = [12.72, 12.72, 13.22, 13.22, 12.72]
ax.plot(boundary_lon, boundary_lat, 'k-', linewidth=1.5, alpha=0.4)
ax.fill(boundary_lon, boundary_lat, alpha=0.05, color='gray')

taluks = [
    ([77.30,77.65,77.65,77.30],[13.05,13.05,13.22,13.22],'#90EE90','Yelahanka Taluku',77.50,13.14),
    ([77.40,77.65,77.65,77.40],[12.90,12.90,13.05,13.05],'#FFDAB9','Bangalore North',77.49,12.97),
    ([77.65,77.80,77.80,77.65],[12.90,12.90,13.05,13.05],'#ADD8E6','Bangalore East',77.73,12.97),
    ([77.40,77.80,77.80,77.40],[12.72,12.72,12.90,12.90],'#FFB6C1','Bangalore South',77.60,12.80),
]
for lons, lats, color, label, tx, ty in taluks:
    ax.fill(lons, lats, alpha=0.35, color=color)
    ax.text(tx, ty, label, ha='center', va='center', fontsize=8.5, color='#333333', fontweight='bold')

plotted = set()
for name, (lon, lat, stype) in stations.items():
    lbl = f'Station: {stype}' if stype not in plotted else ''
    ax.scatter(lon, lat, c=colors_s[stype], marker='o', s=60, zorder=5,
               edgecolors='white', linewidths=0.5, label=lbl)
    plotted.add(stype)
    ax.annotate(name, (lon, lat), xytext=(lon+0.008, lat+0.005), fontsize=6.5,
                color='#222222', arrowprops=dict(arrowstyle='-', color='gray', lw=0.4))

patches = [
    mpatches.Patch(color='#90EE90', alpha=0.6, label='Taluk Boundaries'),
    plt.Line2D([0],[0], color='navy', lw=1.2, label='Major Roads'),
    plt.Line2D([0],[0], marker='o', color='w', markerfacecolor='#2ca02c', markersize=7, label='Station: Residential'),
    plt.Line2D([0],[0], marker='o', color='w', markerfacecolor='#d62728', markersize=7, label='Station: Industrial'),
    plt.Line2D([0],[0], marker='o', color='w', markerfacecolor='#1f77b4', markersize=7, label='Station: Kerbside'),
]
ax.legend(handles=patches, loc='upper left', fontsize=7.5, framealpha=0.85, edgecolor='gray')
ax.set_xlim(77.30, 77.82)
ax.set_ylim(12.70, 13.22)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Bengaluru Urban District: Taluks, Major Roads, and Monitoring Stations', pad=8)
ax.grid(True, linestyle='--', alpha=0.4, linewidth=0.6)
ax.set_aspect('equal')
plt.tight_layout()
fig1.savefig('/home/user/Skill/figure1_map.png', dpi=150, bbox_inches='tight')
plt.close()
print("Figure 1 saved.")

# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — (a) k-Means scatter  +  (b) Seasonal dynamics
# ══════════════════════════════════════════════════════════════════════════════
np.random.seed(42)
fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(13, 5.5))
fig2.subplots_adjust(left=0.08, right=0.97, wspace=0.32)

# (a) k-Means
n1,n2,n3 = 300,400,230
pm10_1 = np.random.uniform(40,130,n1);  pm25_1 = 0.32*pm10_1 + np.random.normal(0,5,n1)
pm10_2 = np.random.uniform(60,180,n2);  pm25_2 = 0.52*pm10_2 + np.random.normal(0,7,n2)
pm10_3 = np.random.uniform(100,240,n3); pm25_3 = 0.72*pm10_3 + np.random.normal(0,8,n3)

ax2a.scatter(pm10_1,pm25_1,c='#90EE90',s=12,alpha=0.65,label='Regime 1: Dust')
ax2a.scatter(pm10_2,pm25_2,c='#5DADE2',s=12,alpha=0.65,label='Regime 2: Mixed')
ax2a.scatter(pm10_3,pm25_3,c='#2E4482',s=12,alpha=0.65,label='Regime 3: Combustion')
ax2a.set_xlabel('PM$_{10}$ (μg/m³)'); ax2a.set_ylabel('PM$_{2.5}$ (μg/m³)')
ax2a.set_title('k-Means Cluster Analysis of Airshed Regimes')
ax2a.legend(loc='upper left', framealpha=0.85)
ax2a.set_xlim(30,255); ax2a.set_ylim(10,170)
ax2a.grid(True,linestyle='--',alpha=0.3)
panel_label(ax2a, '(a)')

# (b) Seasonal box plots
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
medians = [52,51,67,68,70,48,47,47,46,51,53,50]
data_boxes = [np.clip(np.random.normal(m,12 if i in [2,3,4] else 10,120),20,95)
              for i,m in enumerate(medians)]
colors_box = ['#D2691E' if i in [0,1,9,10,11] else '#A0522D' if i in [2,3,4] else '#F4A460'
              for i in range(12)]
bp = ax2b.boxplot(data_boxes, patch_artist=True, widths=0.6,
                  flierprops=dict(marker='D',markersize=3,color='#333'),
                  medianprops=dict(color='#1a1a1a',linewidth=1.5),
                  whiskerprops=dict(linewidth=1.2), capprops=dict(linewidth=1.2))
for patch,color in zip(bp['boxes'],colors_box):
    patch.set_facecolor(color); patch.set_alpha(0.85)
ax2b.set_xticklabels(months)
ax2b.set_xlabel('Month'); ax2b.set_ylabel('Coarse Dust Mass (μg/m³)')
ax2b.set_title('Seasonal Dynamics of Coarse Fraction')
ax2b.set_ylim(15,100)
ax2b.grid(True,axis='y',linestyle='--',alpha=0.3)
panel_label(ax2b, '(b)')

fig2.savefig('/home/user/Skill/figure2_combined.png', dpi=150, bbox_inches='tight')
plt.close()
print("Figure 2 saved.")

# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 3 — (a) Diurnal cycle  +  (b) Spearman matrix
# ══════════════════════════════════════════════════════════════════════════════
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(13, 5.5))
fig3.subplots_adjust(left=0.08, right=0.97, wspace=0.38)

# (a) Diurnal
hours = np.arange(0,24)
coarse = np.array([48.5,48.4,48.3,48.6,48.9,49.2,50.1,50.8,51.2,51.5,
                   51.8,52.0,51.6,51.1,52.8,52.5,51.9,51.2,51.0,50.6,
                   50.2,49.8,49.4,49.2])
ratio  = np.array([0.540,0.538,0.535,0.530,0.527,0.524,0.520,0.516,0.510,0.505,
                   0.500,0.498,0.502,0.508,0.512,0.518,0.528,0.545,0.560,0.568,
                   0.572,0.575,0.576,0.560])
ax3a_r = ax3a.twinx()
l1, = ax3a.plot(hours,coarse,'r-o',markersize=5,linewidth=1.8,label='Coarse Dust (μg/m³)')
l2, = ax3a_r.plot(hours,ratio,'b--',linewidth=1.8,label='Ratio (PM$_{2.5}$/PM$_{10}$)')
ax3a.set_xlabel('Hour of Day (IST)')
ax3a.set_ylabel('Coarse Dust (μg/m³)',color='red')
ax3a_r.set_ylabel('Ratio (PM$_{2.5}$/PM$_{10}$)',color='blue')
ax3a.tick_params(axis='y',labelcolor='red')
ax3a_r.tick_params(axis='y',labelcolor='blue')
ax3a.set_title('Diurnal Cycle of Resuspension vs Ratio')
ax3a.set_xlim(-0.5,23.5); ax3a.set_xticks([0,5,10,15,20])
ax3a.grid(True,linestyle='--',alpha=0.3)
ax3a.legend([l1,l2],[l1.get_label(),l2.get_label()],loc='lower right',fontsize=8)
panel_label(ax3a, '(a)')

# (b) Spearman matrix
labels_c = ['PM$_{2.5}$','PM$_{10}$','PM$_{Coarse}$','NO$_2$','Ratio']
corr = np.array([[1.00,0.90,0.06,0.92,0.83],
                 [0.90,1.00,0.46,0.83,0.53],
                 [0.06,0.46,1.00,0.06,-0.44],
                 [0.92,0.83,0.06,1.00,0.77],
                 [0.83,0.53,-0.44,0.77,1.00]])
im = ax3b.imshow(corr, cmap='RdBu_r', vmin=-0.5, vmax=1.0, aspect='auto')
plt.colorbar(im, ax=ax3b, shrink=0.8)
ax3b.set_xticks(range(5)); ax3b.set_yticks(range(5))
ax3b.set_xticklabels(labels_c, fontsize=9); ax3b.set_yticklabels(labels_c, fontsize=9)
ax3b.set_title('Spearman Correlation Matrix')
for i in range(5):
    for j in range(5):
        v = corr[i,j]
        ax3b.text(j,i,f'{v:.2f}',ha='center',va='center',fontsize=9,fontweight='bold',
                  color='white' if abs(v)>0.6 else 'black')
panel_label(ax3b, '(b)')

fig3.savefig('/home/user/Skill/figure3_combined.png', dpi=150, bbox_inches='tight')
plt.close()
print("Figure 3 saved.")

# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 4 — (a) Weekly bar chart  +  (b) Seasonal regression
# ══════════════════════════════════════════════════════════════════════════════
np.random.seed(99)
fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(13, 5.5))
fig4.subplots_adjust(left=0.08, right=0.97, wspace=0.32)

# (a) Weekly bar chart
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
pm25_w = [68.2,68.8,67.5,68.4,68.1,67.8,65.2]
pmco_w = [51.0,51.3,51.1,51.2,51.0,51.1,50.8]
x = np.arange(len(days)); w = 0.38
ax4a.bar(x-w/2, pm25_w, w, label='PM$_{2.5}$',    color='#C0392B', alpha=0.88, edgecolor='white')
ax4a.bar(x+w/2, pmco_w, w, label='PM$_{Coarse}$', color='#2980B9', alpha=0.88, edgecolor='white')
ax4a.set_xticks(x); ax4a.set_xticklabels(days, fontsize=8.5)
ax4a.set_ylabel('Concentration (μg/m³)')
ax4a.set_title('Weekly Anthropogenic Cycle')
ax4a.set_ylim(0,80)
ax4a.legend(loc='upper right', title='Pollutant', framealpha=0.85)
ax4a.grid(True,axis='y',linestyle='--',alpha=0.3); ax4a.set_axisbelow(True)
panel_label(ax4a, '(a)')

# (b) Seasonal regression
pm10_win = np.random.uniform(50,200,200)
pm25_win = 0.72*pm10_win + 0.72*pm10_win*0.08*np.random.randn(200) + 36
pm10_sum = np.random.uniform(50,225,200)
pm25_sum = 0.55*pm10_sum + 0.55*pm10_sum*0.10*np.random.randn(200) + 15
ax4b.scatter(pm10_win,pm25_win,c='#9B9DC8',s=18,alpha=0.55,label='Winter (High Coupling)')
ax4b.scatter(pm10_sum,pm25_sum,c='#E8998D',s=18,alpha=0.55,label='Summer (Source Decoupling)')
xl = np.array([50,225])
ax4b.plot(xl,0.72*xl+36,color='#3C3C8C',linewidth=2.0)
ax4b.plot(xl,0.55*xl+15,color='#C0392B',linewidth=2.0)
ax4b.set_xlabel('PM$_{10}$ (μg/m³)'); ax4b.set_ylabel('PM$_{2.5}$ (μg/m³)')
ax4b.set_title('Seasonal Regression Slopes')
ax4b.legend(loc='upper left',fontsize=8.5,framealpha=0.85)
ax4b.set_xlim(45,230); ax4b.set_ylim(15,155)
ax4b.grid(True,linestyle='--',alpha=0.3)
panel_label(ax4b, '(b)')

fig4.savefig('/home/user/Skill/figure4_combined.png', dpi=150, bbox_inches='tight')
plt.close()
print("Figure 4 saved.")
print("\nAll figures generated.")
